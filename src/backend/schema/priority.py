from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PrioritySchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
    description = ma.Str()
