from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Team-8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .model import User

    @login_manager.user_loader
    def load_user(userId):
        return User.query.get(int(userId))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app