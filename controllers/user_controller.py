from flask import Flask, render_template, Blueprint, redirect
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/traxstax/<id>")
def user(id):
    user = User.query.get(id)
    return render_template("users/user.jinja", user=user)

@users_blueprint.route("/users/<id>/tracklists")
def user_tracklits(id):
    tracklists = Tracklist.query.filter(Tracklist.user_id == id).all()
    print(tracklists)
    return render_template("users/user_tracklists.jinja", tracklists=tracklists)
