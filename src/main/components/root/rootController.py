from flask import Blueprint, redirect, url_for

root_controller = Blueprint('root_controller', __name__)

@root_controller.route('/')
def redirect_user():
    """
    Redirect the user to the login page if they are not signed in,
    the home page if they are signed in
    """
    return redirect('/login')   # FIXME: hardcoded magic string
