import os
#Capital F indicates class name, 
from flask import Flask, render_template

#this is a variable that we have stored in app
app = Flask(__name__)

#route decorator in python decorater start with @
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")

#reference built in variable, if name is equal to main which is default module in python
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
         port=int(os.environ.get('PORT', 8000)),
            debug=True)

            #enviro.get is a set template
            #debug should never be set to true only good for testing, as security flaw