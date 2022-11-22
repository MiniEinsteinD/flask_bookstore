
# TODO: replace with constants in a separate file, for single source of truth
form_id='login-form'
uname_id = 'username'
uname_label = 'Username:'
pwd_id = 'password'
pwd_label = 'Password:'
action = '/login'
method = 'post'

def get_login_form():
    return f"""
    <form id={form_id}action={action} method={method}>
        <label for={uname_id}>{uname_label}</label><br>
        <input type='text' id={uname_id} name={uname_id}><br>
        <label for={pwd_id}>{pwd_label}</label><br>
        <input type='text' id={pwd_id} name={pwd_id}><br>
        <input type='submit' value='Submit'>
    </form>
    """