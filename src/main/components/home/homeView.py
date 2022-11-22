
# FIXME: get username from session/login service
def get_logged_in_view(username):
    form_action = '/logout'
    form_method = 'POST'
    form_id = 'signout-form'
    return f"""
    <div>
        <h1>WELCOME {username}</h1><br>
        <b>Do stuff</b><br>
        <form id={form_id} action={form_action} method={form_method}>
            <input type='submit' value='Log Out!'>
        </form>
    </div>
    """