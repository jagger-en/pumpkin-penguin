import uuid
import sqlalchemy as sa
from .database import db


class Region(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column(sa.String(150), nullable=False)
    machine_and_regions = db.relationship('MachineAndRegion', backref='region')
    avg_frac = sa.Column(sa.Float, nullable=False)
