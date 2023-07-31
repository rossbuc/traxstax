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
    cover_image = request.form['cover_image']
    user_id = id
    public = "on" in request.form['private_public']
    tracklist_to_create =  Tracklist(name=name, cover_image=cover_image, user_id=user_id, public=public)
    print(tracklist_to_create)
    db.session.add(tracklist_to_create)
    db.session.commit()
    return redirect("/users/1/tracklists")

@tracklist_blueprint.route("/users/<id>/tracklists/<tracklist_id>")
def show_tracklist(id, tracklist_id):
    tracklist = Tracklist.query.get(tracklist_id)
    return render_template("tracklists/tracklist_show.jinja", tracklist=tracklist, id=id)

@tracklist_blueprint.route("/users/<id>/tracklists/edit/<tracklist_id>")
def edit_tracklist(id, tracklist_id):
    tracklist = Tracklist.query.get(tracklist_id)
    return render_template("tracklists/tracklist_edit.jinja", tracklist=tracklist, id=id)

@tracklist_blueprint.route("/users/<id>/tracklists/<tracklist_id>", methods=['POST'])
def update_tracklist(id, tracklist_id):
    name = request.form['title']
    cover_image = request.form['cover_image']
    user_id = id
    public = "on" in request.form['private_public']
    
    tracklist = Tracklist.query.get(tracklist_id)

    tracklist.name = name
    tracklist.cover_image = cover_image
    tracklist.user_id = user_id
    tracklist.public = public

    db.session.commit()
    return redirect(f"/users/{id}/tracklists/{tracklist_id}")