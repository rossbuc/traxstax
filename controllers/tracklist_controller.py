from flask import Flask, render_template, Blueprint, redirect, request
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

tracklist_blueprint = Blueprint("tracklists", __name__)

@tracklist_blueprint.route("/users/<id>/tracklists/new")
def new_tracklist(id):
    songs = Song.query.all()
    return render_template("tracklists/tracklist_new.jinja", songs=songs, id=id)

@tracklist_blueprint.route("/users/<id>/tracklists", methods=['POST'])
def create_tracklist(id):
    name = request.form['title']
    cover_image = request.form['description']
    user_id = id
    # songs = request.form['songs']
    public = "on" in request.form['private_public']
    tracklist_to_create =  Tracklist(name=name, cover_image=cover_image, user_id=user_id, public=public)
    print(tracklist_to_create)
    db.session.add(tracklist_to_create)
    db.session.commit()
    return redirect("/users/1/tracklists")