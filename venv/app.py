from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/product-catalog.html')
def render_static():
    return render_template('product-catalog.html')

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
