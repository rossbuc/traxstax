from flask import Flask, render_template, Blueprint, redirect, request
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

songs_blueprint  = Blueprint("songs", __name__)

@songs_blueprint.route("/users/<id>/upload/new")
def create_upload(id):
    return render_template("upload.jinja")

@songs_blueprint.route("/users/<id>/upload/new", methods=['POST'])
def add_upload(id):
    name = request.form['name']
    artist = request.form['artist']
    album = request.form['album']
    genre = request.form['genre']
    artwork = request.form['artwork']

    song_to_add = Song(name=name, artist=artist, album=album, genre=genre, artwork=artwork)

    db.session.add(song_to_add)
    db.session.commit()

    return redirect("/users/1")