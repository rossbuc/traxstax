from app import db
from models.user import User
from models.song import Song

import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext

def seed():
    User.query.delete()
    Song.query.delete()

    user1 = User(username="rosbuc", password="12345678", profile_image="z", bio="The first user")
    user2 = User(username="jerrysmith", password="iamlame", profile_image="p", bio="The second user")
    user3 = User(username="mp3daddy", password="123thethe", profile_image="p", bio="The third user")
    user4 = User(username="waxnotflacs", password="123$moothoperator", profile_image="p", bio="The fourth user")

    song1 = Song(name="How High", artist="The Salsoul Orchestra", album="How High", genre="Disco")
    song2 = Song(name="Young Hearts Run Free", artist="Candi Staton", album="Young Hearts Run Free", genre="Disco")
    song3 = Song(name="Respect", artist="Aretha Franklin", album="Aretha Now", genre="Soul")
    song4 = Song(name="Time To Move", artist="Carmen", album="Time To Move", genre="Boogie")
    song5 = Song(name="Always", artist="Brief Encounter", album="Always", genre="Gospel")
    song6 = Song(name="Find Your Love", artist="Mary Stevens", album="Find Your Love", genre="Boogie")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)

    db.session.commit()