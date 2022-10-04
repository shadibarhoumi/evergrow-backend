import os
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    if test_config:
        app.config.from_mapping(test_config)

    @app.route('/')
    def hello():
        return 'Hello, world!'

    from . import pdf_generation
    app.register_blueprint(pdf_generation.bp)

    return app

myapp = create_app()