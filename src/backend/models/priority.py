import uuid
import sqlalchemy as sa
from .database import db


class Priority(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column(sa.String(150), nullable=False)
    description = sa.Column(sa.String(1000), nullable=False)
    appointments = db.relationship('Appointment', backref='priority')
