# authentication/login.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Sample user store for demonstration purposes
users = {
    'john_doe': {
        'password_hash': 'pbkdf2:sha256:150000$ynl6pMPT$8ce6a9f62cefa845511eedda55ac911efc5c2646c3b7857113b1f90a454d8943'
    }
}

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login_form():
    """ Renders the login form containing fields for username and password. """
    form = LoginForm()
    if form.validate_on_submit():
        # Handle form submission
        username = form.username.data
        password = form.password.data
        if authenticate_user(username, password):
            return redirect(url_for('success'))
        else:
            login_error_message()
    return render_template('login.html', form=form)

def authenticate_user(username, password):
    """ Validates the user credentials using the provided username and password. """
    user = users.get(username)
    if user and check_password_hash(user['password_hash'], password):
        return True
    return False

def login_error_message():
    """ Displays an error message if the entered credentials are invalid. """
    flash('Invalid username or password. Please try again.', 'danger')

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == "__main__":
    app.run(debug=True)
