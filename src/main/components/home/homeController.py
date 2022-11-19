from flask import Blueprint

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/home', methods=['GET'])
def get_home_page():
    return 'Welcome home'