from backend.models import MachineAndRegion
from backend.schema import MachineAndRegionSchema
from .api_resource import ApiResource


class MachineAndRegionResource(ApiResource):
    MODEL = MachineAndRegion
    SCHEMA = MachineAndRegionSchema()
    SCHEMA_NESTED = MachineAndRegionSchema()
    SCHEMA_MANY = MachineAndRegionSchema(many=True)
    SCHEMA_MANY_NESTED = MachineAndRegionSchema(many=True)
