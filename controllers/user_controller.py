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
    user_add = User(username="rosbuc", password="12345678", profile_image="z", bio="The first user")
    db.session.add(user_add)
    db.session.commit()
    return render_template("users/user.jinja", user=user)