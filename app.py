from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def my_shop():
	products = ["lipsticks", "mascaras","eyeshadows"]
	return render_template(
		"shop.html" ,
		products=products)

if __name__ == '__main__':
   app.run(debug = True)