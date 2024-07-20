from marshmallow import Schema, fields
from .chicken_traits import ChickenTraitResponseSchema

class ChickenResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    color = fields.String()
    traits = fields.List(
        fields.Nested(ChickenTraitResponseSchema)
    )
