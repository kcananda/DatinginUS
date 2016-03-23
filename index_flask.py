


from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
#	return "hello world"
   return render_template("index.html")

@app.route('/signup')
def sign():
   return render_template("signup.html")

@app.route('/contact',methods=["GET","POST"])
def contactus():
	if request.method == 'POST':
		name = request.form['fname']
		return render_template("contact.html",fname=name)
	else:
		return render_template("contact.html",fname="YOU")


if __name__ == '__main__':
    app.run(debug=True)