from flask_restful import Resource
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from app_name.chicken.schemas.chickens import ChickenResponseSchema, ChickenPostSchema
from app_name.chicken.models.chicken import Chicken
from app_name.chicken.models.css_color import CSSColor

class Chickens(MethodResource, Resource):
    
    @doc(
        description="get all chickens in the barn!",
        tags=["chickens"]
    )
    @marshal_with(ChickenResponseSchema(many=True), code=200)
    def get(self, **kwargs):
        chickens = Chicken.query.all()
        return chickens, 200

    @doc(
        description="add a chicken to the barn!",
        tags=["chickens"]
    )
    @use_kwargs(ChickenPostSchema, location="json")
    @marshal_with(ChickenResponseSchema, code=201)
    def post(self, **kwargs):
        chicken = Chicken.create(
            name=kwargs.get("name"),
            color=CSSColor.get_by_color_name(
                kwargs.get("color")
            )
        )
        return chicken, 201
