from flask_marshmallow import Marshmallow

ma = Marshmallow()


class RegionsSchema(ma.Schema):
    id = ma.Str()
    region_name = ma.Str()
