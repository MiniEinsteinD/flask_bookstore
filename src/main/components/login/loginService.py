from flask import session

def set_login_session(username):
    session['username'] = username

def remove_login_session():
    session.pop('username', None)