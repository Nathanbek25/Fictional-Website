from flask import Flask, render_template, request

app = Flask(__name__)





# the homepage for your site will be at the route below
@app.route('/')
def hello_world():
    return render_template("index.html")


# Rendering a html template
@app.route('/about')
def home():
    return render_template("about.html")


# Rendering a html template with the Bootstrap framework
@app.route('/product')
def bootstrap_grid():
    return render_template("product.html")

@app.route('/contact')
def bootstrap_form():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    email = request.args.get('email')
    address = request.args.get('address')
    props = {
       "name": name,
       "email": email,
        "address": address

    }
    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True, port=5050)

