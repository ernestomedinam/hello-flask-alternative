from marshmallow import Schema, fields, post_dump
from app_name.chicken.models.personality_trait import PersonalityTrait

class ChickenTraitResponseSchema(Schema):
    id = fields.Integer()
    order = fields.Integer()
    # chicken_id = fields.Integer()
    trait = fields.String()

    @post_dump
    def dress_trait(self, data, **kwargs):
        data["trait"] = PersonalityTrait[data["trait"].split(".")[1]].value
        return data
