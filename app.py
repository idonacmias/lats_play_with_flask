from flask import Flask
api = Flask(__name__)
 
@api.route('/')
def index():
    return 'Hello, World!'
 
@api.route('/new_route/')
def new_route():
    return 'new_route'                           


if __name__ == '__main__':
    api.run(debug=True)
