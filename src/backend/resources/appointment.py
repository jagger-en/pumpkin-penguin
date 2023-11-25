from backend.models import Appointment
from backend.schema import AppointmentSchema
from .api_resource import ApiResource


class AppointmentResource(ApiResource):
    MODEL = Appointment
    SCHEMA = AppointmentSchema()
    SCHEMA_NESTED = AppointmentSchema()
    SCHEMA_MANY = AppointmentSchema(many=True)
    SCHEMA_MANY_NESTED = AppointmentSchema(many=True)
