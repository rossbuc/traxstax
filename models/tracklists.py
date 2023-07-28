from app import db

class Tracklists(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    tracklist_id = db.Column(db.Integer, db.ForeignKey('tracklist.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))