from backend.models import Appointment
from backend.schema import AppointmentSchema
from backend.schema import AppointmentSchemaNested
from .api_resource import ApiResource


class AppointmentResource(ApiResource):
    MODEL = Appointment
    SCHEMA = AppointmentSchema()
    SCHEMA_NESTED = AppointmentSchemaNested()
    SCHEMA_MANY = AppointmentSchema(many=True)
    SCHEMA_MANY_NESTED = AppointmentSchemaNested(many=True)
