import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'medileaks.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # temporary code for home page
    @app.route('/home')
    def welcome_message():
        return 'Welcome to Medileaks!'

    from . import db
    db.init_app(app)

    from . import guidelines
    app.register_blueprint(guidelines.bp)

    from . import reports_and_ratings
    app.register_blueprint(reports_and_ratings.bp)

    from . import predictions
    app.register_blueprint(predictions.bp)

    return app

