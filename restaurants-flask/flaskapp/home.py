from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskapp.auth import login_required
from flaskapp.db import get_db

bp = Blueprint('blog', __name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'