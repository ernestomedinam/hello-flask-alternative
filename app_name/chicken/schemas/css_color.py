from marshmallow import fields, validate, Schema
from app_name.chicken.models.css_color import CSSColor

class CSSColorResponseSchema(Schema):
    label = fields.String()
    value = fields.String()
    rgb = fields.String()
