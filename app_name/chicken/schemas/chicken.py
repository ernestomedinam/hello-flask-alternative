from marshmallow import Schema, fields, validate, pre_load, post_dump
from .chicken_trait import ChickenTraitResponseSchema
from app_name.chicken.models.css_color import CSSColor

class ChickenResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    color = fields.String()
    traits = fields.List(
        fields.Nested(ChickenTraitResponseSchema)
    )

    @post_dump
    def dress_color(self, data, **kwargs):
        data["color"] = CSSColor[data["color"].split(".")[1]].value
        return data

class ChickenPostSchema(Schema):
    name = fields.String()
    color = fields.String(
        required=True,
        validate=validate.OneOf(
            CSSColor.list_color_names()
        )
    )
