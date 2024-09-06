import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# url_prefix means /auth is added to the start of all URLs in this blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    # when the form in the register page is filled, it is sent with the request method POST.
    # All the pages with forms work this way. GET is used to get the page and
    # POST is used to submit a form.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        # Even though the HTML form says username and password are required, 
        # you can never trust what is sent from a user so you should always validate user inputs.
        # Anyone can send any kind of request to the server.
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                # Question marks are replaced with the value in the tuple.
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                # If an account was successfully registered, redirect the user to the login page
                return redirect(url_for("auth.login"))
        # If there were any errors while registering, flash() sends the 
        # error to the next request so it can be shown on the web page
        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        
        if error is None:
            # If the user is able to log in, the user id is stored in session
            # The session data is stored in a cookie and sent to the browser.
            # The cookie is sent to the server every time the browser sends a request.
            # This lets flask know if the user is logged in and who is sending the request.
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    # The session cookie is cleared
    session.clear()
    return redirect(url_for('index'))

# Every time a request is sent to flask, this function is called to load a logged in user if
# the user has a cookie with a user_id.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# This is a decorator that can be added to other functions.
# It is added to views that require the user to be logged in.
# When a function with this decorator is called, it checks if the user is logged in.
# If the user is not logged in, redirect them to the login page.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view