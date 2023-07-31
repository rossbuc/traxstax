from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rossbuchan@localhost:5432/traxstax"
# app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.user_controller import users_blueprint, User
from controllers.song_controller import songs_blueprint
from controllers.tracklist_controller import tracklist_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(songs_blueprint)
app.register_blueprint(tracklist_blueprint)


@app.route('/')
def home():
    return render_template("index.jinja")

@app.route('/traxstax/login')
def login():
    return render_template('login.jinja')

@app.route('/traxstax/login', methods=['POST'])
def login_user():
    user_username = request.form['username']
    users = User.query.all()
    for user in users:
        if user.username == user_username:
            return redirect(f"/traxstax/{user.id}")