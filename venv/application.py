from flask import Flask, render_template, request
import Model.product as product

application = Flask(__name__)

@application.route('/products',methods=['GET'])
def get_product_by_id():
    id_name = request.args.get('id')
    result = product.get_product_details(id_name)
    return render_template('product-details.html', product=result, len=len(result))

@application.route('/products/all',methods=['GET'])
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
    result = product.get_products()
    url=""
    return render_template('product-catalog.html', product=result, len=len(result), url=url)

@application.route('/basic-layout.html')
def render_basic_layout():
    return render_template('basic-layout.html')

@application.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')

@application.route('/Login.html')
def render_login():
    return render_template('Login.html')

@application.route('/logout.html')
def render_logout():
    return render_template('logout.html')

@application.route('/about-us.html')
def render_about_us():
    return render_template('about-us.html')

@application.route('/Occasion1.html')
def render_occasion():
    return render_template('Occasion1.html')

@application.route('/Signup.html')
def render_signup():
    return render_template('Signup.html')

@application.route('/woodworker.html')
def render_woodworker():
    return render_template('woodworker.html')

if __name__ == '__main__':
    application.debug = True
    application.run()
