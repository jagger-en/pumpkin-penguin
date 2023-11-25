from flask_marshmallow import Marshmallow

from .machine import MachineSchema
from .patient import PatientSchema
from .priority import PrioritySchema

ma = Marshmallow()


class AppointmentSchema(ma.Schema):
    id = ma.Str()
    machine = ma.Nested(MachineSchema)
    patient = ma.Nested(PatientSchema)
    priority = ma.Nested(PrioritySchema)

    start_time = ma.Str()
    end_time = ma.Str()