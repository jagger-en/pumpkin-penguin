from flask_marshmallow import Marshmallow
from .gender import GenderSchema
ma = Marshmallow()


class PatientSchema(ma.Schema):
    id = ma.Str()
    first_name = ma.Str()
    last_name = ma.Str()
    email = ma.Str()
    gender = ma.Nested(GenderSchema)
    date_of_birth = ma.Str()
    weight = ma.Float()
    height = ma.Float()
