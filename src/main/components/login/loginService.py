from flask import Blueprint

login_service = Blueprint('login_service', __name__)

@login_service.route('/login')
def get_login_page():
    return "Welcome to login page"