from . import app
from flask import (
    render_template,
    url_for,
    redirect,
    request,
)

from pydantic import BaseModel
import logging


@app.route('/index')
def index() -> str:
    return render_template('users.html')


class User(BaseModel):
    first_name: str
    last_name: str


USERS = [
        User(
            first_name='Rodion',
            last_name='Petrov'
        ),
    ]


@app.route('/users')
def get_users_profile() -> str:
    return render_template('users.html', users=USERS)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user_profile():
    args = request.args.to_dict()
    if args:
        USERS.append(
            User(
                first_name=args.get("first_name"),
                last_name=args.get("last_name")
            )
        )

    return redirect(url_for('get_users_profile'))
