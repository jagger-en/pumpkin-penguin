import uuid
import sqlalchemy as sa
from .database import db


class Gender(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = sa.Column(sa.String(150), nullable=False)
    patients = db.relationship('Patient', backref='gender')
