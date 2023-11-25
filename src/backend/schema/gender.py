from flask_marshmallow import Marshmallow

ma = Marshmallow()


class GenderSchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
