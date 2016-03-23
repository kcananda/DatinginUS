


from flask import Flask
from flask import url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
#	return "hello world"
   return render_template("hello.html")

@app.route('/signup')
def sign():
#	return "uname %s " % uname
   return render_template("sign.html")

@app.route('/contact/<name>')
def contactus(name):
    #return 'welcome to contact page!-- Enter the detail for %s'%name
    return render_template("contact.html", fname=name)

if __name__ == '__main__':
    app.run(debug=True)