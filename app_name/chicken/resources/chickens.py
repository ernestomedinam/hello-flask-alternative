from flask_restful import Resource
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from app_name.chicken.schemas.chickens import ChickenResponseSchema
from app_name.chicken.models.chicken import Chicken

class Chickens(MethodResource, Resource):
    
    @doc(
        description="get all chickens in the barn!",
        tags=["chickens"]
    )
    @marshal_with(ChickenResponseSchema(many=True), code=200)
    def get(self, **kwargs):
        chickens = Chicken.query.all()
        return chickens, 200
