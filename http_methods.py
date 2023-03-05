from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
def do_the_login():
    return "this is from do_the_login"

def show_the_login_form():
    return "this is from show the login form"