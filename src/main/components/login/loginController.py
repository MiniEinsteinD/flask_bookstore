from flask import Blueprint, request, redirect, url_for

from components.login.loginView import get_login_form
from components.login.loginService import remove_login_session, set_login_session

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login', methods=['GET'])
def get_login_page():
    login_form = get_login_form()
    return login_form

@login_controller.route('/login', methods=['POST'])
def get_login_form_response():
    print(request.form)
    set_login_session(request.form['username']) # FIXME: hardcoded magic string
    return redirect(url_for('home_controller.get_home_page'))  # FIXME: hardcoded magic string

@login_controller.route('/logout', methods=['POST'])
def log_out_user():
    remove_login_session()
    return redirect(url_for('login_controller.get_login_page')) # FIXME: hardcoded magic string
    