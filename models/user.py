from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    profile_image = db.Column(db.String(64))
    bio = db.Column(db.Text())
    tracklists = db.relationship("Tracklist", backref="tracklist")