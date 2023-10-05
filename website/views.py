from flask import Blueprint, render_template

#setup blueprints for all the urls 
views = Blueprint('views', __name__)

#decorator
@views.route('/')
#will run whenever we go to the / roots
def home():
    return render_template("home.html")


