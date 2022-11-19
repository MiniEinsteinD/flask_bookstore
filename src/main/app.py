from flask import Flask

from components.root.rootController import root_controller
from components.home.homeController import home_controller

app = Flask(__name__)
app.register_blueprint(root_controller)
app.register_blueprint(home_controller)

if __name__ == "__main__":
    app.run()