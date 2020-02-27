from flask import Flask, render_template, request
import Model.product as product

app = Flask(__name__)

@app.route('/products',methods=['GET'])
def get_product_by_id():
    id_name = request.args.get('id')
    result = product.get_product_details(id_name)
    return render_template('product-details.html', product=result, len=len(result))

@app.route('/products/all',methods=['GET'])
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

    

@app.route('/')
@app.route('/product-catalog.html')
def render_static():
    result = product.get_products()
    url=""
    return render_template('product-catalog.html', product=result, len=len(result), url=url)

@app.route('/basic-layout.html')
def render_basic_layout():
    return render_template('basic-layout.html')

@app.route('/prodct-details.html')
def render_product_details():
    return render_template('prodct-details.html')

@app.route('/Login.html')
def render_login():
    return render_template('Login.html')

@app.route('/logout.html')
def render_logout():
    return render_template('logout.html')

@app.route('/about-us.html')
def render_about_us():
    return render_template('about-us.html')

@app.route('/Occasion1.html')
def render_occasion():
    return render_template('Occasion1.html')

@app.route('/Signup.html')
def render_signup():
    return render_template('Signup.html')

@app.route('/woodworker.html')
def render_woodworker():
    return render_template('woodworker.html')

if __name__ == '__main__':
    app.run()
