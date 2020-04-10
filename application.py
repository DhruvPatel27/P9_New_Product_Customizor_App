from flask import Flask, render_template, request, session, jsonify, url_for, redirect
import itertools
import Model.product as product
import Model.user as user
import Model.order as order
import Model.customization as preview
import Model.wood as wood
import pandas as pd

application = Flask(__name__)


@application.route('/products', methods=['GET'])

def get_product_by_id():
    url = ""
    id_name = request.args.get('id')
    result = product.get_product_details(id_name)
    wood_type = wood.get_wood()
    wood_design = wood.get_design()
    return render_template('product-details.html', product=result, len=len(result), wood_type=wood_type, wood_design=wood_design)

@application.route('/products/all', methods=['GET'])
def get_products():
    category = request.args.get('category')
    occasion = request.args.get('occasion')
    result = product.get_products()
    url=""
    if category:
        result = product.get_products_by_category(category)
    elif occasion:
        result = product.get_products_by_occasion(occasion)
    return render_template('product-catalog.html', product=result, len=len(result), url=url)

@application.route('/')
@application.route('/product-catalog.html')
def render_static():
    page = request.args.get('page')
    
    result = product.get_products()
    url = ""
    total_pages = (int)(len(result) / 12) + 1

    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)


@application.route('/product-catalog-manager.html')
def product_catalog_manager():
    page = request.args.get('page')
    
    result = product.get_products()
    url = ""
    total_pages = (int)(len(result) / 12) + 1

    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog-manager.html', product=result, len=len(result), url=url, total_pages=total_pages)
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog-manager.html', product=result, len=len(result), url=url, total_pages=total_pages)


@application.route('/login', methods=['POST'])
def login():
    session.clear()
    page = request.args.get('page')
    if not request.form or not 'username' in request.form or not 'password' in request.form:
        return render_template('login.html'),400
    user_details = user.login(request.form['username'], request.form['password'])
    if(user_details):
        url=""
        session['user_name'] =  request.form['username']
        session['fname'] = user_details['FirstName']
        session['lname'] = user_details['LastName']
        if user_details['Role'] == "Carpenter":
            orders = order.get_all_orders()
            return render_template('woodworker.html', orders=orders, len=len(orders), url=url),200
        elif user_details['Role'] == "Admin":
            orders = order.get_all_orders()
            return render_template('manage-products.html'),200
        result = product.get_products()
        total_pages = (int)(len(result) / 12) + 1

        if(page == None or int(page) == 1):
            result = list(itertools.islice(result, 0, 12, 1))
            return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200
        else:
            page = int(page)
            result = result[12*(page-1):12*page]
            return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200
    else:
        return render_template('login.html'),401

@application.route('/signup', methods=['POST'])
def signup():
    page = request.args.get('page')
    if not request.form:
        return render_template('signup.html'),400
    else:
        user_details = user.signup(request.form['lastname'], request.form['firstname'], request.form['emailid'], request.form['password'])
        if(user_details):
            url=""
            result = product.get_products()

            total_pages = (int)(len(result) / 12) + 1

            if(page == None or int(page) == 1):
                result = list(itertools.islice(result, 0, 12, 1))
                return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200          
            else:
                page = int(page)
                result = result[12*(page-1):12*page]
                return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200            
        else:
            return render_template('signup.html'),401


@application.route('/account', methods=['GET'])
def get_user_by_id():
    user_name = session['user_name']
    user_result = user.get_user_details(user_name)
    order_result = order.get_order_details_for_user(user_name)
    return render_template('my-account.html', user=user_result, order=order_result, order_len=len(order_result)), 200


@application.route('/cart', methods=['GET'])
def load_cart_page():
    if 'product' in session or len(session['product']) > 0:
        data = session['product']
        product_result = []
        for dic in data:
            for prod_id, q in dic.items():
                result = product.get_product_details_cart(prod_id)
                result['quantity'] = q
                product_result.append(result)
        return render_template('cart.html', product=product_result, product_len=len(product_result)), 200
    else:
        return render_template('cart.html', product_len=0), 200

# @application.route('/preview', methods=['GET'])
# def show_preview():
#     model_id = request.args.get('model_id')
#     wood_id = request.args.get('wood_id')
#     design_id = request.args.get('design_id')
#     mask = product.get_products_mask(model_id)
#     wood_type = wood.get_wood_by_id(wood_id)
#     design_type = wood.get_design_by_id(design_id)
#     preview_image = preview.mask_loop(mask[0]['model_mask'], wood_type['image'], design_type['mask'])
#
#     return jsonify({
#         "preview_image": preview_image.decode('utf-8')
#     })

@application.route('/removeCart', methods=['GET'])
def remove_from_cart_page():
    id_name = request.args.get('id')
    # if 'product' in session or len(session['product']) > 0:
    if 'product' in session:
        data = session['product']
        product_result = []
        for i in range(len(data)):
            if id_name in data[i]:
                del data[i]
                break
        session['product'] = data
        product_result = []
        for dic in data:
            for prod_id, q in dic.items():
                result = product.get_product_details_cart(prod_id)
                res_img = result['image']
                result['image'] = res_img.decode('utf-8')
                result['quantity'] = q
                product_result.append(result)
        return jsonify({
            "product": product_result
            })
    #     return render_template('cart.html', product=product_result, product_len=len(product_result)), 200
    # else:
    #     return render_template('cart.html', product_len=0), 200


@application.route('/addToCart', methods=['POST'])
def add_to_cart():
    id_name = request.args.get('id')
    page = request.args.get('page')
    quantity = request.form['quantity']
    if 'product' not in session.keys():
        session['product'] = [{id_name: quantity}]
    else:
        data = session['product']
        data.append({id_name: quantity})
        session['product'] = data
    url = ""
    result = product.get_products()
    total_pages = (int)(len(result) / 12) + 1
    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url,
                           total_pages=total_pages), 200
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url,
                           total_pages=total_pages), 200

@application.route('/checkoutSuccess')
def load_checkout_success():
    return render_template('checkout-success.html'), 200

@application.route('/login')
def load_login_page():
    return render_template('login.html'),200

@application.route('/signup')
def render_signup():
    return render_template('signup.html'),200

@application.route('/about')
def render_about_us():
    return render_template('about-us.html')

@application.route('/basic-layout.html')
def render_basic_layout():
    return render_template('basic-layout.html')
    
@application.route('/manage-products', methods=['POST', 'GET'])
def manage_products():
    if request.method == 'POST':
        new_products = request.files['new-products']
        data_xls = pd.read_excel(new_products)
        product.add_products(data_xls)
        return render_template('success.html'),200
    
    return render_template('manage-products.html'),200

@application.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')

@application.route('/logout')
def render_logout():
    session.clear()
    page = request.args.get('page')
    url=""
    result = product.get_products()

    total_pages = (int)(len(result) / 12) + 1
    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages), 200
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages), 200

@application.route('/occasions', methods=['GET'])
def render_occasion():
    occasion = str(request.args.get('occasion'))
    page = request.args.get('page')
    result = product.get_products()
    url=""
    if occasion:
        result = product.get_products_by_occasion(occasion)
    
    total_pages = (int)(len(result) / 12) + 1
    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages, occasion=occasion)
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages, occasion=occasion)

@application.route('/categories', methods=['GET'])
def render_category():
    category = str(request.args.get('category'))
    page = request.args.get('page')
    result = product.get_products()
    url=""
    if category:
        result = product.get_products_by_category(category)
        
    total_pages = (int)(len(result) / 12) + 1
    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)

@application.route('/woodworker.html')
def render_woodworker():
    return render_template('woodworker.html')

@application.route('/orderstatus', methods=['GET'])
def show_order_status():
    url = ""
    order_id = request.args.get('id')
    result = order.get_order_details_by_id(order_id)
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
def show_preview():
    model_id = request.args.get('model_id')
    wood_id = request.args.get('wood_id')
    design_id = request.args.get('design_id')

    mask = product.get_products_mask(model_id)
    wood_type = wood.get_wood_by_id(wood_id)

    if(design_id != 'undefined'):
        design_type = wood.get_design_by_id(design_id)
        preview_image = preview.mask_loop(mask[0]['model_mask'], wood_type['image'], design_type['mask'])
    else:
        preview_image = preview.mask_loop(mask[0]['model_mask'], wood_type['image'],0)
    return jsonify({
        "preview_image": preview_image.decode('utf-8')
    })

@application.route('/remove', methods=['POST'])
def remove_product():
    product_id = request.form['productid']
    product.remove(product_id)
    return render_template("success.html")

@application.route('/edit', methods=['POST','GET'])
def edit_product():
    if request.method == 'GET':
        id_name = request.args.get('id')
        result = product.get_product_details(id_name)
        return render_template('edit-product.html', product=result, len=len(result))
    
    if request.method == 'POST':
        p_id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        product.edit(p_id, title, description, price)
        return render_template('success.html')
    

if __name__ == '__main__':
    application.secret_key = 'super secret key'
    application.debug = True
    application.run()
   
