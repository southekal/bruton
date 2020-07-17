from flask import (
    flash,
    Blueprint,
    redirect,
    render_template,
    url_for
)

from flask_login import (
    current_user,
    login_user,
    logout_user
)

from app import app, db
from app.mod_auth.models import BaseUser
from app.mod_auth.forms import LoginForm, RegisterForm

from helper import db as db_helper


mod_auth = Blueprint('auth', __name__, url_prefix="")


@mod_auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if current_user.is_authenticated:
        flash("you are already logged in")
        return redirect(url_for('home.index'))

    if form.validate_on_submit():
        user = BaseUser(
            name = form.name.data,
            email = form.email.data,
            org = form.org.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)

        flash(f"welcome {form.name.data}!")
        return redirect(url_for('home.index'))

    return render_template(
        "auth/register.html",
        form=form
    )


@mod_auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        flash("you are already logged in")
        return redirect(url_for('home.index'))

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db_helper.get_user(email=email)

        if user is None or user.check_password(password):
            flash("invalid email/password")
            return redirect(url_for('auth.login'))

        login_user(user)
        flash("you are logged in")
        return redirect(url_for('home.index'))
    return render_template(
        "auth/login.html",
        form=form
    )


@mod_auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()

    form = LoginForm()
    flash("you are logged out!")
    return render_template(
                "auth/login.html",
                form=form
    )

