# TraxStax

## MVP

The Traxstax site is a community in which users can keep track of the songs they're playing at the moment in the form of tracklists, to enable this the _User_ will be able to:

- Create a new **Tracklist**.
- Add a **Song** to the **Tracklist**.
- Remove a **Song** from the **Tracklist**.
- Delete a **Tracklist**.
- Add a **Song** to the database.

## Possible Extensions

Once the basic functionality of the app is achieved, possible enhancements include:

- Enable **Users** to follow eachothers **Tracklists**.
  - This will assign the **Tracklist** to the **User** but the user will not be able to edit the **Tracklist**.
- Emable **Users** to delete a **Song** from the database if their id is the user_id associated with the **Song**.
- Include a comments section at the bottom of each **Tracklist** in which **User** can discuss what they think of the songs.

## How to run the app

Ensure you're in the root directory and first you will need to install the necessary modules. To do this run the following commmands:

- `pip install Flask`
- `pip install Flask-SQLAlchemy`
- `pip install Flask-Migrate`

Then you will have to run the seeds which you can do using the command:

- `flask run seeds`

Then you are ready to run the app, using the command below, and open it on the browser. Once you start the app it should be running on _http://localhost:4999_.

- `flask run`
