import uuid
import sqlalchemy as sa
from .database import db


class Appointment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    machine_id = db.Column(db.String(36), db.ForeignKey('machine.id'), nullable=False)
    patient_id = db.Column(db.String(36), db.ForeignKey('patient.id'), nullable=False)
    priority_id = db.Column(db.String(36), db.ForeignKey('priority.id'), nullable=False)

    start_time = sa.Column(sa.DateTime, nullable=False)
    end_time = sa.Column(sa.DateTime, nullable=False)
