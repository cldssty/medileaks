import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from medileaks.db import get_db

bp = Blueprint('reports_and_ratings', __name__, url_prefix='/reports_and_ratings')