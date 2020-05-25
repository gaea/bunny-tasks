from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    CORS(app, resources={r'/*': {'origins': '*'}})

    with app.app_context():
        db.init_app(app)

        from .routes import api
        from .helpers import errors

        app.register_blueprint(api)
        db.create_all()

        errors.register_error_handlers(app)

        return app
