from backend.models import Gender
from backend.schema import GenderSchema
from .api_resource import ApiResource


class GenderResource(ApiResource):
    MODEL = Gender
    SCHEMA = GenderSchema()
    SCHEMA_NESTED = GenderSchema()
    SCHEMA_MANY = GenderSchema(many=True)
    SCHEMA_MANY_NESTED = GenderSchema(many=True)
