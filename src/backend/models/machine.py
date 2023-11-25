import uuid
import sqlalchemy as sa
from .database import db


class Machine(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    machine_name = sa.Column(sa.String(150), nullable=False)
    machine_and_regions = db.relationship('MachineAndRegion', backref='machine')
    appointments = db.relationship('Appointment', backref='machine')
