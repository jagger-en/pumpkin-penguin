import uuid
import sqlalchemy as sa
from .database import db


class MachineAndRegion(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    machine_id = db.Column(db.String(36), db.ForeignKey('machine.id'), nullable=False)
    region_id = db.Column(db.String(36), db.ForeignKey('region.id'), nullable=False)
