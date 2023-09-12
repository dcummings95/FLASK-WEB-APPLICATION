from flask import Blueprint

#setup blueprints for all the urls 
views = Blueprint('views', __name__)

#decorator
@views.route('/')
#will run whenever we go to the / roots
def home():
    return "<h1>Test</h1>"


