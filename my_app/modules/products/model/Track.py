from my_app import db

from datetime import datetime



class Track (db.Model):
    __tablename__ = 'tracks'
    id            = db.Column (db.Integer, primary_key=True)
    idUser        = db.Column (db.Integer)
    user          = db.Column (db.String(200))
    idProduct     = db.Column (db.Integer)
    product       = db.Column (db.String(200))
    view_at       = db.Column (db.DateTime(timezone=False), nullable=False, default=datetime.utcnow())

    def __init__(self, idUser, user, idProduct, product):
        self.idUser          = idUser
        self.user            = user
        self.idProduct       = idProduct
        self.product         = product

    def __repr__(self):
        return '<Track %r>' %(self.name)

