from flask_marshmallow import Marshmallow

ma = Marshmallow()

class MachineAndRegionsSchema(ma.Schema):
    id = ma.Str()
    machine_id = ma.Str()
    region_id = ma.Str()

    machine = ma.Nested(MachineSchema)
    region = ma.Nested(RegionsSchema)
