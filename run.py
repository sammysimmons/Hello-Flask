import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About",company=data)

#crate route decorater for member name, creates new view about member, 
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    #creates empty object and opens the company.json file for reading
    with open("data/company.json", "r") as json_data:
      #variable that passes json data
        data = json.load(json_data)
        #iterates through if the url isequal to the member name, then the member object os equal to object
        for obj in data:
            if obj["url"] == member_name:
                member = obj
#if they match return out object
        return render_template("member.html", member=member) 

@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == '__main__':
           app.run(host=os.environ.get('IP', '127.0.0.1'),              
           port=int(os.environ.get('PORT', 5000)),
            debug=True)