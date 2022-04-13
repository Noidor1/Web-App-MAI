from . import app
from flask import render_template, render_template_string, url_for, redirect
from pydantic import BaseModel
import logging


@app.route('/')
@app.route('/hello_world')
def get_hello_world() -> str:
    return render_template('hello_world.html')
