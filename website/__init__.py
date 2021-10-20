from sys import path
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from time import sleep
db = SQLAlchemy()


def initialize():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "jf8tu4uoifrIUNOUNuo8n"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://webbi:webbi@localhost/webbi"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #    db = SQLAlchemy(app)
    db.init_app(app)

    from .routes import views
    from .authentication import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    db.create_all(app=app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    @login_manager.unauthorized_handler
    def unauth():
        return redirect(url_for("auth.login"))
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
