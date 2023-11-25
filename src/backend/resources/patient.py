from backend.models import Patient
from backend.schema import PatientSchema
from .api_resource import ApiResource


class PatientResource(ApiResource):
    MODEL = Patient
    SCHEMA = PatientSchema()
    SCHEMA_NESTED = PatientSchema()
    SCHEMA_MANY = PatientSchema(many=True)
    SCHEMA_MANY_NESTED = PatientSchema(many=True)
