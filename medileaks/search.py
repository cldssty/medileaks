# -*- coding: utf-8 -*-
"""User inputs medical procedure and is returned
    1. summary of best practices.
    2. option to view full version of best practices.
    3. option to view full list of source urls.

    Todo:
        1. Fix import statements.
        2. Maybe don't use flash(error).
        3. How to link request forms to the UI?

"""

import functools

from flask import (
    flash, Blueprint, g, redirect, render_template, request, session, url_for
)

from spider.nice import get_raw_best_practices 

from summariser.extractive_summariser import summarise 

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST': 
        medical_procedure = request.form['procedure']
        error = None
    
        if medical_procedure is None:
            error = 'Please input a medical procedure.'
        else:
            content = get_raw_best_practices(https://www.nice.org.uk/guidance/ng87/chapter/Recommendations) 
            if content is None: 
                error = "No results found for {}.".format(medical_procedure)
        
        if error is None:
            summary = summarise(content)

        flash(error)

    return render_template('search.html', result=[content, summary, sources])
