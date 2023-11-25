from backend.models import Machine
from backend.schema import MachineSchema
from .api_resource import ApiResource


class MachineResource(ApiResource):
    MODEL = Machine
    SCHEMA = MachineSchema()
    SCHEMA_NESTED = MachineSchema()
    SCHEMA_MANY = MachineSchema(many=True)
    SCHEMA_MANY_NESTED = MachineSchema(many=True)
