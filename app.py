import os

from flask import send_from_directory
from btasks import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


@app.route('/static/<filename>')
def static_files(filename):
    return send_from_directory('static', filename)
