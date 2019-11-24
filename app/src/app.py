from flask import Flask
from api import api
import logging, os


from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = "this is the secret key"
    app.register_blueprint(api)
    file_handler = logging.FileHandler('/tmp/app.log')
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.ERROR)
    #return app
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
    )


if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    #app.run()
    
    app.run(debug=True, host='0.0.0.0', threaded=True)
