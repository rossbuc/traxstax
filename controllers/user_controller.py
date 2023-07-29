from flask import Flask, render_template, Blueprint, redirect
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/<id>")
def user(id):
    user = User.query.get(id)
    return render_template("users/user.jinja", user=user)

@users_blueprint.route("/users/<id>/tracklists")
def user_tracklits(id):
    # user = User.query.get(id)
    # tracklists = Tracklists.query.all().filter(user.id == id)
    return render_template("users/user_tracklists.jinja")
