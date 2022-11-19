from flask import Blueprint, redirect, url_for

root_service = Blueprint('root_service', __name__)

@root_service.route('/')
def redirect_user():
    """
    Redirect the user to the login page if they are not signed in,
    the home page if they are signed in
    """
    return redirect(url_for('home_service.get_home_page'))   # FIXME: hardcoded magic string
