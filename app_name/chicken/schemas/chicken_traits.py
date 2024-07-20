from marshmallow import Schema, fields

class ChickenTraitResponseSchema(Schema):
    id = fields.Integer()
    order = fields.Integer()
    chicken_id = fields.Integer()
    trait = fields.String()
