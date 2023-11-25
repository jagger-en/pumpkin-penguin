from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PatientSchema(ma.Schema):
    id = ma.Str()
    first_name = ma.Str()
    last_name = ma.Str()
    weight = ma.Float()
