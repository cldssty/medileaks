import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from medileaks.db import get_db

bp = Blueprint('guidelines', __name__, url_prefix='/guidelines')