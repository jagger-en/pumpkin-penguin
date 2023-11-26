from backend.models import Maintenance
from backend.schema import MaintenanceSchema
from .api_resource import ApiResource


class MaintenanceResource(ApiResource):
    MODEL = Maintenance
    SCHEMA = MaintenanceSchema()
    SCHEMA_NESTED = MaintenanceSchema()
    SCHEMA_MANY = MaintenanceSchema(many=True)
    SCHEMA_MANY_NESTED = MaintenanceSchema(many=True)
