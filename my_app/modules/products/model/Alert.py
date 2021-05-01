from my_app import db

from decimal import Decimal
from datetime import datetime

class Alert (db.Model):
    __tablename__ = 'alerts'
    id          = db.Column (db.Integer, primary_key=True)
    label       = db.Column (db.String(200))
    deleted     = db.Column (db.Integer, default=0)

    def __init__(self, label, deleted):
        self.label          = label
        self.deleted        = 0

    def __repr__(self):
        return '<Alert %r>' %(self.name)

