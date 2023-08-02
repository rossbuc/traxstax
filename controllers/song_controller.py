from flask import Flask, render_template, Blueprint, redirect, request
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

songs_blueprint  = Blueprint("songs", __name__)

@songs_blueprint.route("/traxstax/<id>/upload/new")
def create_upload(id):
    user = User.query.get(id)
    return render_template("upload.jinja", user=user)

@songs_blueprint.route("/traxstax/<id>/upload/new", methods=['POST'])
def add_upload(id):
    name = request.form['name']
    artist = request.form['artist']
    album = request.form['album']
    genre = request.form['genre']
    artwork = request.form['artwork']
    user_id = id

    song_to_add = Song(name=name, artist=artist, album=album, genre=genre, artwork=artwork, user_id=user_id)

    db.session.add(song_to_add)
    db.session.commit()

    return redirect(f"/traxstax/{id}")

@songs_blueprint.route("/traxstax/<id>/upload/delete/<song_id>", methods=['POST'])
def delete_upload(id, song_id):
    song_to_delete = Song.query.get(song_id)

    db.session.delete(song_to_delete)
    db.session.commit()

    return redirect(f'/traxstax/{id}/uploads')