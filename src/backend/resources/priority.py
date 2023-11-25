from backend.models import Priority
from backend.schema import PrioritySchema
from .api_resource import ApiResource


class PriorityResource(ApiResource):
    MODEL = Priority
    SCHEMA = PrioritySchema()
    SCHEMA_NESTED = PrioritySchema()
    SCHEMA_MANY = PrioritySchema(many=True)
    SCHEMA_MANY_NESTED = PrioritySchema(many=True)
