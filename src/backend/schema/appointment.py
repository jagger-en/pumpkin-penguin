from flask_marshmallow import Marshmallow

from .machine import MachineSchema
from .patient import PatientSchema
from .priority import PrioritySchema

ma = Marshmallow()


class AppointmentSchemaNested(ma.Schema):
    id = ma.Str()
    machine = ma.Nested(MachineSchema)
    patient = ma.Nested(PatientSchema)
    priority = ma.Nested(PrioritySchema)

    start_time = ma.Str()
    end_time = ma.Str()

class AppointmentSchema(ma.Schema):
    id = ma.Str()
    machine_id = ma.Str()
    patient_id = ma.Str()
    priority_id = ma.Str()

    start_time = ma.Str()
    end_time = ma.Str()