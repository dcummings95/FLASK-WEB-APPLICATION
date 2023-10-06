from flask import Blueprint, render_template

#setup blueprints for all the urls 
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template("login.html", text="Testing", user="Tim")

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
  return render_template("sign_up.html")

