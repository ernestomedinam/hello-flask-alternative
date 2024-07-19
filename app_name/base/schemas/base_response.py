from marshmallow import Schema, fields

class BaseResponseSchema(Schema): 
    message = fields.String()
