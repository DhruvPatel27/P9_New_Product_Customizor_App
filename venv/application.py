from flask import Flask, render_template, request, session
import itertools
import Model.product as product
import Model.user as user

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
@application.route('/product-catalog.html')
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
    if(user.login(request.form['username'], request.form['password']) == "success"):
        url=""
        session['user_name'] =  request.form['username']
        result = product.get_products()
        return render_template('product-catalog.html', product=result, len=len(result), url=url),200
    else:
        return render_template('login.html'),401

# @application.route('/user', methods=['GET'])
# def get_product_by_id():
#     id_name = request.args.get('id')
#     result = user.get_user_details(id_name)
#     return render_template('my-account.html', user=result, len=len(result))

@application.route('/login')
def load_login_page():
    return render_template('login.html'),200
    
@application.route('/about')
def render_about_us():
    return render_template('about-us.html')

@application.route('/basic-layout.html')
def render_basic_layout():
    return render_template('basic-layout.html')

@application.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')

@application.route('/logout')
def render_logout():
    session.clear()
    url=""
    result = product.get_products()
    return render_template('product-catalog.html', product=result, len=len(result), url=url),200

@application.route('/Occasion1.html')
def render_occasion():
    return render_template('Occasion1.html')

@application.route('/signup')
def render_signup():
    return render_template('signup.html')

@application.route('/woodworker.html')
def render_woodworker():
    return render_template('woodworker.html')

if __name__ == '__main__':
    application.secret_key = 'super secret key'
    application.debug = True
    application.run()
