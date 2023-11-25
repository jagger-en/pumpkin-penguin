from flask_marshmallow import Marshmallow
from .region import RegionSchema
from .machine import MachineSchema

ma = Marshmallow()

class MachineAndRegionSchema(ma.Schema):
    id = ma.Str()
    machine_id = ma.Str()
    region_id = ma.Str()

    machine = ma.Nested(MachineSchema)
    region = ma.Nested(RegionSchema)
