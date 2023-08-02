from app import db

class Tracklist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    cover_image = db.Column(db.String(128), default="Enter cover image URL")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    public = db.Column(db.Boolean)
    songs = db.relationship('Tracklists', backref='tracklist')