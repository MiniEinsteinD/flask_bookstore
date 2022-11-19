from flask import Blueprint

home_service = Blueprint('home_service', __name__)

@home_service.route('/home', methods=['GET'])
def get_home_page():
    return 'Welcome home'