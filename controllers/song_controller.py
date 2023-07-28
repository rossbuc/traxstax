from flask import Flask, render_template, Blueprint, redirect
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists
from app import db

songs_blueprint  = Blueprint("songs", __name__)

