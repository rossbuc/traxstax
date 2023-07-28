from flask import Flask, render_template, Blueprint, redirect
from models.user import User

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/<id>")
def user(id):
    user = User.query.get(id)
    return render_template("users/user.jinja", user=user)