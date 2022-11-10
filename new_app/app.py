from flask import Flask
from flask import render_template
from models import get_db

from datetime import date

api = Flask(__name__)
 
@api.route('/')
def index():
    context = {'first_name' : 'bob', 'last_name' : 'marly', 'date_of_birth': date(2020,11,30)}
    # cherecter = Cherecter('ido') 
    # context = {'name': cherecter.name}
    return render_template('init.html', context=context)    
 
@api.route('/new_route/')
def new_route():
    return 'new_route'                           


if __name__ == '__main__':
    api.run(debug=True)
