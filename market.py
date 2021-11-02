from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/about')
def about_page():
    return '<h1>About page</h1>'

@app.route('/about/<user>')
def fun(user):
    return f"<h1>this is about of {user}</h1>"
@app.route('/product')
def product_page():
    return render_template('product.html')
