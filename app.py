from flask import Flask
from flask import render_template
from models import get_db
api = Flask(__name__)
 
@api.route('/')
def index():
    car = get_db().cursor()
    context = car
    print(car)
    # cherecter = Cherecter('ido') 
    # context = {'name': cherecter.name}
    return render_template('init.html', context=context)    
 
@api.route('/new_route/')
def new_route():
    return 'new_route'                           


if __name__ == '__main__':
    api.run(debug=True)
