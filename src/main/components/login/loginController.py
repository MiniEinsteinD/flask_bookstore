from flask import Blueprint

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login')
def get_login_page():
    return "Welcome to login page"