from marshmallow import fields
from flask_restful import Resource
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from app_name.chicken.models.css_color import CSSColor
from ..schemas.css_color import CSSColorResponseSchema

class CSSColors(MethodResource, Resource):

    @doc(
        description="get all valid css color names to create livestock animals",
        tags=["barn"]
    )
    @marshal_with(CSSColorResponseSchema(many=True), code=200)
    def get(self, **kwargs):
        colors = CSSColor.build_colors_list()
        return colors, 200
