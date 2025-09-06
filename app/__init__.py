
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    bcrypt.init_app(app)
    jwt.init_app(app)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
