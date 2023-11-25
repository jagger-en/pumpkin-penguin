import uuid
import sqlalchemy as sa
from .database import db


class Patient(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    first_name = sa.Column(sa.String(150), nullable=False)
    last_name = sa.Column(sa.String(150), nullable=False)
    email = sa.Column(sa.String(150), nullable=False)
    gender_id = db.Column(db.String(36), db.ForeignKey('gender.id'), nullable=False)
    date_of_birth = sa.Column(sa.String(150), nullable=False)
    weight = sa.Column(sa.Float, nullable=False)
    height = sa.Column(sa.Float, nullable=False)
    appointments = db.relationship('Appointment', backref='patient')
