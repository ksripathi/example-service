from flask import Flask
from api import api
import logging, os
from config import config
def create_app():
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    app.register_blueprint(api)
    file_handler = logging.FileHandler(config.LOG_FILE_PATH)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(config.LOG_LEVEL)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', threaded=True)
