from flask import Flask, render_template, request, session, jsonify
import itertools
import Model.product as product
import Model.user as user
import Model.order as order
import Model.customization as preview
import Model.wood as wood

application = Flask(__name__)

@application.route('/products', methods=['GET'])
def get_product_by_id():
    id_name = request.args.get('id')
    result = product.get_product_details(id_name)
    return render_template('product-details.html', product=result, len=len(result))

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
def render_static():
    page = request.args.get('page')
    result = product.get_products()
    url = ""
    total_pages = (len(result) % 12) + 1

    if(page == None or int(page) == 1):
        result = list(itertools.islice(result, 0, 12, 1))
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)
    else:
        page = int(page)
        result = result[12*(page-1):12*page]
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages)


@application.route('/login', methods=['POST'])
def login():
    if not request.form or not 'username' in request.form or not 'password' in request.form:
        return render_template('login.html'),400
    user_details = user.login(request.form['username'], request.form['password'])
    if(user_details):
        url=""
        session['user_name'] =  request.form['username']
        if user_details['Role'] == "Carpenter":
            orders = order.get_all_orders()
            return render_template('woodworker.html', orders=orders, len=len(orders), url=url),200
        elif user_details['Role'] == "Admin":
            orders = order.get_all_orders()
            return render_template('woodworker.html', orders=orders, len=len(orders), url=url),200
        result = product.get_products()
        total_pages = (len(result) % 12) + 1
        return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200
    else:
        return render_template('login.html'),401

@application.route('/signup', methods=['POST'])
def signup():
    if not request.form:
        return render_template('signup.html'),400
    else:
        user_details = user.signup(request.form['lastname'], request.form['firstname'], request.form['emailid'], request.form['password'])
        if(user_details):
            url=""
            result = product.get_products()
            total_pages = (len(result) % 12) + 1
            return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200
        else:
            return render_template('signup.html'),401


@application.route('/account', methods=['GET'])
def get_user_by_id():
    user_name = session['user_name']
    user_result = user.get_user_details(user_name)
    order_result = order.get_order_details_for_user(user_name)
    return render_template('my-account.html', user=user_result, order=order_result, order_len=len(order_result))


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

@application.route('/manage-products.html')
def manage_prods():
    return render_template('manage-products.html')

@application.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')

@application.route('/logout')
def render_logout():
    session.clear()
    url=""
    result = product.get_products()
    total_pages = (len(result) % 12) + 1
    return render_template('product-catalog.html', product=result, len=len(result), url=url, total_pages=total_pages),200

@application.route('/Occasion1.html')
def render_occasion():
    return render_template('Occasion1.html')

@application.route('/woodworker.html')
def render_woodworker():
    return render_template('woodworker.html')

@application.route('/preview')
def show_preview():
    model_id = request.args.get('model_id')
    wood_id = request.args.get('wood_id')
    mask = product.get_products_mask(model_id)
    wood_type = wood.get_wood(wood_id)

    preview_image = preview.mask_loop(mask[0]['model_mask'], wood_type['image'])

    return jsonify({
        "preview_image": preview_image.decode('utf-8')
    })


if __name__ == '__main__':
    application.secret_key = 'super secret key'
    application.debug = True
    application.run()
