import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from flask_backend.routes.classification import classification_blueprint

load_dotenv()


class AppWrapper:
    def __init__(self):
        self._app = Flask(__name__, instance_relative_config=True)
        self._app.config.from_mapping(
            SECRET_KEY=os.getenv('SECRET_KEY')
        )
        CORS(self._app)

    def run(self):
        self._app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=True)

    def register_blueprint(self, blueprint, prefix=None):
        self._app.register_blueprint(blueprint, prefix=prefix)

    @property
    def app(self):
        return self._app


if __name__ == '__main__':
    app = AppWrapper()
    app.register_blueprint(classification_blueprint, prefix='classification')
    app.run()
