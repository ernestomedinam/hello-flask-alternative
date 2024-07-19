from flask_restful import Api
from apispec import APISpec
from flask_apispec import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_jwt_extended import JWTManager
from webargs.flaskparser import abort, parser
from app_name.utils.thc import parse_error_response


rest_api = Api(prefix="/api")


jwt = JWTManager()
jwt_key_scheme = {
    "type": "apiKey", 
    "in": "header", 
    "name": "Authorization"
}


spec = APISpec(
    title="app name",
    version="v1",
    plugins=[MarshmallowPlugin(), ],
    openapi_version="2.0.0"
)
spec.components.security_scheme("jwt", jwt_key_scheme)


docs = FlaskApiSpec()

# class Parser(FlaskParser):
@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    response = parse_error_response(dict(**error.messages), error_status_code if error_status_code is not None else 400)
    abort(response)
