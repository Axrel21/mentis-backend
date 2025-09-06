
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .questionnaire import questionnaire_blueprint
    app.register_blueprint(questionnaire_blueprint, url_prefix='/questionnaire')

    from .chatbot import chatbot_blueprint
    app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot')

    from .resources import resources_blueprint
    app.register_blueprint(resources_blueprint, url_prefix='/resources')

    with app.app_context():
        db.create_all()

    return app
