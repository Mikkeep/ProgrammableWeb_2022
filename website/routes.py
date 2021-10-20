from flask import Flask, jsonify, render_template, Blueprint, request, make_response, redirect, url_for
from . import db
from .models import People, User
from datetime import datetime as dt
routes = Blueprint('routes', __name__)

@routes.route("/")
def hello():
    return render_template('users.jinja2')

@routes.route("/person", methods=['GET'])
def person():
    """Create a user via query string parameters."""
    username = request.args.get("user")
    email = request.args.get("email")
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(f"{username} ({email}) already created!")
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
            on the playground is where I spent most of my days",
            admin=False,
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for("person"))
    return render_template("users.jinja2", users=User.query.all(), title="Show Users")

@routes.route("/button")
def button():
    return '<a href="/addperson"><button> Click here </button></a>'
@routes.route("/addperson")
def addperson():
    return render_template("form.html")
@routes.route("/health")
def health():
    return jsonify({'status': 'ok'})
@routes.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()
    return render_template("index.html")
