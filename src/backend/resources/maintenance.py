from backend.models import Maintenance
from backend.schema import MaintenanceSchema
from backend.schema import MaintenanceSchemaNested
from .api_resource import ApiResource


class MaintenanceResource(ApiResource):
    MODEL = Maintenance
    SCHEMA = MaintenanceSchema()
    SCHEMA_NESTED = MaintenanceSchemaNested()
    SCHEMA_MANY = MaintenanceSchema(many=True)
    SCHEMA_MANY_NESTED = MaintenanceSchemaNested(many=True)
