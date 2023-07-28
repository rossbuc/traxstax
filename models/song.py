from app import db

class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    artist = db.Column(db.String(64))
    album = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    tracklists = db.relationship('Tracklists', backref='song')