from flask import Flask, jsonify, render_template, Blueprint
from . import db
authentication = Blueprint('authentication', __name__)

@authentication.route('/login')
def login():
    return "<p> I guess we should add login... try /logout </p>"
@authentication.route('/logout')
def logout():
    return "<p> I guess we should add logout... try /login </p>"

@authentication.route('/sign-up')
def sign_up():
    return "<p> It would be awesome to be able to signup I guess... </p>"