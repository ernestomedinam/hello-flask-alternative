from flask_restful import Resource
from flask_apispec import marshal_with, doc
from flask_apispec.views import MethodResource
from ..schemas.base_response import BaseResponseSchema

class Hello(MethodResource, Resource):

    @doc(description="check if api is up 😎", tags=["health"])
    @marshal_with(BaseResponseSchema, code=200)
    def get(self):
        """ says hello """
        return {
            "message": "hello app name 📊"
        }, 200
