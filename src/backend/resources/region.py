from backend.models import Region
from backend.schema import RegionSchema
from .api_resource import ApiResource


class RegionResource(ApiResource):
    MODEL = Region
    SCHEMA = RegionSchema()
    SCHEMA_NESTED = RegionSchema()
    SCHEMA_MANY = RegionSchema(many=True)
    SCHEMA_MANY_NESTED = RegionSchema(many=True)
