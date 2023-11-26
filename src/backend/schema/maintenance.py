from flask_marshmallow import Marshmallow
from .machine import MachineSchema
ma = Marshmallow()


class MaintenanceSchemaNested(ma.Schema):
    id = ma.Str()
    start_time = ma.Str()
    end_time = ma.Str()
    comments = ma.Str()
    machine = ma.Nested(MachineSchema)


class MaintenanceSchema(ma.Schema):
    id = ma.Str()
    start_time = ma.Str()
    end_time = ma.Str()
    comments = ma.Str()
    machine_id = ma.Str()
