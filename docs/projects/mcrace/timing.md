---
authors:
    - mona
---

# McRace Timing System


## Authentication

All features except viewing the results should be restricted to club execs/tech team.
Users without authorization will be directed to the results page.

Create a file `backend/.env` with the values `ADMIN_USER` and `ADMIN_PASS`.
This corresponds to the username and password to be entered in the login screen.
These values should be known by execs only.

Upon starting the frontend, navigate to the login screen at `/secure-portal-X9a2q`.

## Backend

The backend is built using Flask and Flask-SQLAlchemy.

For venv, etc. users:

```shell
cd backend
python -m venv venv
pip install -r requirements.txt
python main.py
```

## Frontend

The frontend is built using React and Bootstrap.

```shell
cd frontend
npm install
npm run dev
```

## App architecture

There are four pages for different tasks:

- `/assign` - pair bib numbers with RFID tags. This should be run only one instance at a time to avoid write/overwrite issues
- `/pair` - assign RFID numbers to participants (runners) using their bib number.
- `/timer` - detect tags and store in a database. **This is what should be run during the race.**
- `/results` - view and filter participant times by age and gender.

Each page has a corresponding frontend and backend URL.
The relevant files are under `frontend/src/routes` and `backend/app/routes` respectively.

**Requests and socket events should be sent between each page's frontend URL and backend URL.** 
This way the tasks can be separated somewhat easily.

For example, `http://frontend/assign` should send requests to `http://backend/assign/get`, etc. 
And those should send responses back to `http://frontend/assign`. 
Similarly, sockets should emit to `http://frontend/assign`.

The backend handles this using Flask Blueprints (for the requests) and SocketIO Namespaces (for the socket events).

## Requests vs Socket events

**SocketIO events are used for the scanner and for logging error messages.**

The scanner needs to use the socket for constantly sending detections. Additionally, the socket only emits events from the backend to the frontend. 

**HTTP requests are used for everything else.**

There are frontend functions to handle user events (e.g. click button to start the timer). 
These functions send requests to a specific backend URL, which receives it and runs the relevant backend function.

Longer backend functions are found in `processing.py` and `reader/`.

## Hardware

For both `/assign` and `/timer`, it works like this:

1. User presses *Start* button.
2. Request backend to start detection loop.
3. Detection loop runs in a background task using SocketIO. 
    - It sends information to the frontend using the socket and/or directly to the database using Flask-SQLAlchemy.
4. Frontend receives socket events and displays them as necessary.
    - For `/assign`, the tags must be displayed so that the user can enter a bib number to associate with it.
    - For `/timer`, the tags are not necessarily displayed but it is useful.
5. User presses *Stop* button.
6. Request backend to stop detection.

To start and stop the detection loop, the backend calls `detect_tags_assign` and `detect_tags_timer` from `processing.py`.

`detect_tags_assign` should emit the UUID of a tag if only one tag is detected at a time. Otherwise, it should indicate that there are too many/too less tags being deteted.

Please note that `detect_tags_assign` relies on RFID Reader no.1 . It doesn't matter if the second reader is also plugged in. 

`detect_tags_timer` should process detections and update Participant records in the database according to which tag is detected. It should also save the detections as RaceDetection events in the database, for backup. It should also emit some information to the frontend to indicate that it is working.

Please make sure to have both readers connected through USB when using `detect_tags_timer`. 

See below for database models.


## Database

There are two types of records in the database:

- `Participant`: represents one runner. Has name, age, gender, bib number, RFID tag, and race times (elapsed time stored in seconds).
- `RaceDetection`: represents a RFID detection event. Has RFID tag and time.

The `/results` page queries the database on load and when the user filters by age and/or gender.


## Helpful links

- [flask.palletsprojects.com](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)
- [flask-socketio.readthedocs.io](https://flask-socketio.readthedocs.io/en/latest/api.html#)
- [socket.io/docs/](https://socket.io/docs/v4/server-api/)
- [flask-sqlalchemy.readthedocs.io](https://flask-sqlalchemy.readthedocs.io/en/stable/queries/)
- [docs.sqlalchemy.org](https://docs.sqlalchemy.org/en/21/core/selectable.html#selectable-foundational-constructors)
- [react-bootstrap-v2-bs5.netlify.app/docs](https://react-bootstrap-v2-bs5.netlify.app/docs/forms/overview)
- [getbootstrap.com/docs](https://getbootstrap.com/docs/5.3/forms/overview/)


## Oscar's notes

If npm fails or neads cleanup, `rm -rf node_modules package-lock.json` then `npm install` again.

To visualize the detection results data while the frontend is revamped, you can run `datasette backend/instance/database.db` and go to `http://localhost:8001/` to see the database tables and query them.

Make SURE TO DELETE THE DATABASE BEFORE TESTING THE TIMER. Otherwise, the timer will update the existing Participant records instead of creating new ones, which can mess up testing. You can delete the database by deleting `backend/instance/database.db` and restarting the backend.

Right now the only way to differentiate between the two readers is to check the USB port they are plugged into. In Pyserial we can use port.position to check the address of the reader. So make sure to update the `mapping_readers` dictionnary in `ReaderQueue` by associating the correct port to each reader. For this run `identification_tags.ipynb`