
# FIXME: make and put in DTO obj dir?
class UserInfo:
    def __init__(self, username, name=None):
        self.username = username
    
    def get_username(self):
        return self.username