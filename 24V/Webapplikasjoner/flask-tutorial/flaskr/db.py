import sqlite3

import click
from flask import current_app, g

# init_app runs when the server is started
def init_app(app):
    # close_db is run every time when Flask is done handling a request
    app.teardown_appcontext(close_db)
    # add_command adds a new command that can be called with the flask command by typing 'flask --app flaskr init-db'
    app.cli.add_command(init_db_command)

# init_db runs the script in schema.sql. 
# It is run when the init-db cli command is used
def init_db():
    db = get_db()
    # current_app is a special variable that points to the Flask application.
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Every time the database is used, get_db is called.
def get_db():
    # g is a special variable that stores information that can be used by many functions during a request
    # g is unique for each request
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    # The database connection is stored in g so that if multiple functions call get_db, 
    # you only need to connect to the database once.
    return g.db

# close_db is called after each requets.
# it closes the database connection, if g.db was set.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()