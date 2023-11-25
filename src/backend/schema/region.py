from flask_marshmallow import Marshmallow

ma = Marshmallow()


class RegionSchema(ma.Schema):
    id = ma.Str()
    name = ma.Str()
