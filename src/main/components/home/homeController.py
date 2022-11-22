from flask import Blueprint, session, redirect, url_for

from components.home.homeView import get_logged_in_view

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/home', methods=['GET'])
def get_home_page():
    if session and 'username' in session:     # FIXME: hardcoded string, use enum?
        username = session['username']
        #return f'Welcome home {username}'
        return get_logged_in_view(username)    # FIXME: get session username from session service?
    return redirect(url_for('login_controller.get_login_page'))