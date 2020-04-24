import itertools

import datetime
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, session, jsonify, redirect

import model.customization as preview
import model.order as order
import model.product as product
import model.user as user
import model.wood as wood

application = Flask(__name__)


@application.route('/products', methods=['GET'])
def get_product_by_id():
    id_name = request.args.get('id')
    result = product.get_product_details(id_name)
    wood_type = wood.get_wood()
    wood_design = wood.get_design()
    default_image = preview.show_preview(result['model_id'], 1, 6, "")

    return render_template('product-details.html', product=result, len=len(result), wood_type=wood_type,
                           wood_design=wood_design, default_image=default_image)

@application.route('/')
def render_static():
    page = request.args.get('page')
    result = product.get_products()
    details = get_pages(page, result)
    return render_template('product-catalog.html', product=details[0], len=len(details[0]), url="",
                               total_pages=details[1])


@application.route('/login', methods=['POST'])
def login():
    if 'customer' in session and session['customer']:
        return redirect(request.url_root)
    elif 'manager' in session and session['manager']:
        return redirect(request.url_root+"manager")
    else:
        session.clear()
    page = request.args.get('page')
    if not request.form or not 'username' in request.form or not 'password' in request.form:
        return render_template('login.html'), 400
    user_details = user.login(request.form['username'], request.form['password'])
    if (user_details):
        url = ""
        session['user_name'] = request.form['username']
        session['fname'] = user_details['FirstName']
        session['lname'] = user_details['LastName']
        if user_details['Role'] == "Carpenter":
            session['carpenter'] = True
            result = order.get_all_orders()
            if len(result) > 0:
                for orders in result:
                    orders['order_date'] = orders['order_date'].strftime('%m-%d-%Y')
                    result.reverse()
            return render_template('woodworker.html', orders=result, len=len(orders), url=url), 200
        elif user_details['Role'] == "Admin":
            session['manager'] = True
            return redirect(request.url_root+"manager")
        else:
            session['customer'] = True
            return redirect(request.url_root)
    else:
        return render_template('login.html', error="Invalid credentials. Try again!!!"), 401


@application.route('/manager', methods=['GET'])
def display_home_manager():
    if session and session['manager']:
        page = request.args.get('page')
        result = product.get_products()
        details = get_pages(page, result)
        return render_template('product-catalog-manager.html', product=details[0], len=len(details[0]), url="",
                               total_pages=details[1]),200
    else:
        return render_template('error.html', error="You are not authorized to access this page!!"), 401


@application.route('/signup', methods=['POST'])
def signup():
    page = request.args.get('page')
    if not request.form:
        return render_template('signup.html'), 400
    else:
        user.signup(request.form['lastname'], request.form['firstname'], request.form['emailid'],
                                   request.form['password'])
        return redirect(request.url_root)


@application.route('/account', methods=['GET'])
def get_user_by_id():
    user_name = session['user_name']
    fname = session['fname']
    lname = session['lname']
    order_result = order.get_order_details_for_user(user_name)
    if len(order_result) > 0:
        for orders in order_result:
            orders['order_date'] = orders['order_date'].strftime('%m-%d-%Y')
        order_result.reverse()
    return render_template('my-account.html', email=user_name, fname=fname, lname=lname, order=order_result, order_len=len(order_result)), 200


@application.route('/cart', methods=['GET'])
def load_cart_page():
    user_name = session['user_name']
    result = order.load_cart(user_name)
    product_result = []
    for entry in result:
        prod = product.get_product_details_cart(entry['product_id'])
        entry['title'] = prod['title']
        entry['price'] = prod['price']
        wood_type = wood.get_wood_by_id(entry['woodtype_id'])
        entry['wood_type'] = wood_type['name']
        design_type = wood.get_design_by_id(entry['woodpattern_id'])
        entry['wood_pattern'] = design_type['name']
        product_result.append(entry)
    return render_template('cart.html', product=product_result, product_len=len(product_result)), 200


@application.route('/remove-cart', methods=['GET'])
def remove_from_cart_page():
    id_name = request.args.get('id')
    order.remove_cart(id_name)
    user_name = session['user_name']
    result = order.load_cart(user_name)
    product_result = []
    for entry in result:
        prod = product.get_product_details_cart(entry['product_id'])
        entry['title'] = prod['title']
        entry['price'] = prod['price']
        res_img = entry['image']
        entry['image'] = res_img.decode('utf-8')
        wood_type = wood.get_wood_by_id(entry['woodtype_id'])
        entry['wood_type'] = wood_type['name']
        design_type = wood.get_design_by_id(entry['woodpattern_id'])
        entry['wood_pattern'] = design_type['name']
        product_result.append(entry)
    return jsonify({
        "product": product_result
    })


@application.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    user_name = session['user_name']
    id_name = request.args.get('id')
    image = request.form['image']
    page = request.args.get('page')
    quantity = request.form['quantity']
    wood_id = request.form['wood']
    pattern_id = request.form['pattern']
    result = product.get_product_details_cart(id_name)
    price = result['price']
    total_cost = price * float(quantity)
    cart_details = order.add_to_cart(id_name, image, quantity, wood_id, pattern_id, user_name, total_cost)
    return redirect('/cart')


@application.route('/checkout', methods=['POST'])
def load_checkout():
    cost = request.form['total']
    return render_template('checkout.html', cost=cost), 200


@application.route('/checkout-success', methods=['POST'])
def load_checkout_success():
    price = request.form['cost']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']
    card_number = request.form['card']
    expiry = datetime.datetime.strptime(request.form['expiry'], "%m/%d/%Y").strftime("%Y-%m-%d")
    cvv = request.form['cvv']
    contact = request.form['contact']
    user_name = session['user_name']
    address = (','.join([address, city, state]))
    order.place_order(user_name, price, address, zipcode, card_number, expiry, cvv, contact)
    return render_template('checkout-success.html'), 200


@application.route('/login')
def load_login_page():
    return render_template('login.html'), 200


@application.route('/signup')
def render_signup():
    return render_template('signup.html'), 200


@application.route('/about')
def render_about_us():
    return render_template('about-us.html')


@application.route('/basic-layout.html')
def render_basic_layout():
    return render_template('basic-layout.html')

@application.route('/basic-layout-manager.html')
def render_basic_layout_manager():
    return render_template('basic-layout-manager.html')


@application.route('/add-products', methods=['POST', 'GET'])
def manage_products():
    if request.method == 'POST':
        new_products = request.files['new-products']
        data_xls_1 = pd.read_excel(new_products)
        data_xls = data_xls_1.replace(np.nan,'',regex=True)
        invalid = product.add_products(data_xls)
        if not invalid:
            return render_template('manager-success.html', success="Products added successfully"), 200
        else:
            return render_template('manager-success.html', success="Some products are added successfully. Please correct the details for the following products.", error=invalid), 200

    return render_template('manage-products.html'), 200


@application.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')


@application.route('/logout')
def render_logout():
    session.clear()
    return redirect(request.url_root)

@application.route('/occasions', methods=['GET'])
def render_occasion():
    occasion = str(request.args.get('occasion'))
    page = request.args.get('page')
    result = product.get_products()
    url = ""
    if occasion:
        result = product.get_products_by_occasion(occasion)
    details = get_pages(page, result)
    return render_template('product-catalog.html', product=details[0], len=len(details[0]), url="",
                               total_pages=details[1])

@application.route('/categories', methods=['GET'])
def render_category():
    category = str(request.args.get('category'))
    page = request.args.get('page')
    result = product.get_products()
    url = ""
    if category:
        result = product.get_products_by_category(category)

    details = get_pages(page, result)
    return render_template('product-catalog.html', product=details[0], len=len(details[0]), url="",
                               total_pages=details[1])

@application.route('/orderstatus', methods=['GET'])
def show_order_status():
    url = ""
    order_id = request.args.get('id')
    result = order.get_order_details_by_id(order_id)
    result['order_date'] = result['order_date'].strftime('%m-%d-%Y')
    wood_type = wood.get_wood_by_id(result['woodtype_id'])
    wood_design = wood.get_design_by_id(result['woodpattern_id'])
    products=product.get_product_details(result['product_id'])
    return render_template('order-status.html', url=url, orders=result,len=len(result), product=products, wood_type=wood_type, wood_design=wood_design),200

@application.route('/orderstatus/update', methods=['GET'])
def update_order_status():
    order_id = request.args.get('order_id')
    status = request.args.get('status')
    order.update_order_status_for_order(status, order_id)
    return jsonify({
        "status": status
    })


@application.route('/preview', methods=['GET'])
def show_message_preview():
    model_id = request.args.get('model_id')
    wood_id = request.args.get('wood_id')
    design_id = request.args.get('design_id')
    message = request.args.get('message')
    preview_image = preview.show_preview(model_id, wood_id, design_id, message)

    return jsonify({
        "preview_image": preview_image.decode('utf-8')
    })


@application.route('/remove', methods=['POST'])
def remove_product():
    product_id = request.form['productid']
    product.remove(product_id)
    return render_template('manager-success.html', success="Product Removed"), 200


@application.route('/edit', methods=['POST', 'GET'])
def edit_product():
    if request.method == 'GET':
        id_name = request.args.get('productid')
        result = product.get_product_details(id_name)
        return render_template('edit-product.html', product=result, len=len(result))

    if request.method == 'POST':
        p_id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        product.edit(p_id, title, description, price)
        return render_template('manager-success.html', success="Product Updated"),200


@application.route('/search', methods=['GET'])
def get_product_by_name():
    page = request.args.get('page')
    product_name = request.args.get('product_name')
    result = product.search_product_by_name(product_name)
    details = get_pages(page, result)
    return render_template('product-catalog.html', product=details[0], len=len(details[0]), url="",
                               total_pages=details[1])

# Returns results based on pages
def get_pages(page, result):
    total_pages = (int)(len(result) / 12) + 1
    if (page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
    else:
        page = int(page)
        result = result[12 * (page - 1):12 * page]
    
    return (result,total_pages)


if __name__ == '__main__':
    application.secret_key = 'super secret key'
    application.debug = True
    application.run()
   
