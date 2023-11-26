import uuid
import sqlalchemy as sa
from .database import db


class Maintenance(db.Model):
    id = sa.Column(sa.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    machine_id = db.Column(db.String(36), db.ForeignKey('machine.id'), nullable=False)

    comments = sa.Column(sa.String(500), nullable=False)
    start_time = sa.Column(sa.String(150), nullable=False)
    end_time = sa.Column(sa.String(150), nullable=False)
