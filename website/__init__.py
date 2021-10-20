from flask import Flask#, app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize():
    app = Flask(__name__)
    app.config['SECRETS'] = 'jf8tu4uoifrIUNOUNuo8n'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vagrant:vagrant@127.0.0.1/vagrant'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app=app)
    db.create_all(app=app)
    db.init_app(app)

    from .routes import routes
    from .authentication import authentication

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    db.create_all(app=app)

    return app