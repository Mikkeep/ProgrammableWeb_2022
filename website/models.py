from . import db

class People(db.Model):
    __tablename__ = "Testihommeli"
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color

class User(db.Model):
    "Model for users accounts"

    __tablename__ = "testi"
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=True,
        unique=True,
        nullable=False
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=True,
        nullable=False
    )
