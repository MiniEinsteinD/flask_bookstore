from flask import Flask

from components.root.rootService import root_service
from components.home.homeService import home_service

app = Flask(__name__)
app.register_blueprint(root_service)
app.register_blueprint(home_service)

if __name__ == "__main__":
    app.run()