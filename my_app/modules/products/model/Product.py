from my_app import db
# Importaciones para WTF
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange
from sqlalchemy import Column, Integer, DateTime

from decimal import Decimal
from datetime import datetime

class Product (db.Model):
    __tablename__ = 'products'
    id          = db.Column (db.Integer, primary_key=True)
    sku         = db.Column (db.String(200))
    name        = db.Column (db.String(200))
    description = db.Column (db.Text)
    brand       = db.Column (db.String(200))
    price       = db.Column (db.Float)
    category_id = db.Column (db.Integer, db.ForeignKey('categories.id'), nullable=False)
    file        = db.Column (db.String(200))
    created     = db.Column (db.DateTime(timezone=False), nullable=False, default=datetime.utcnow())
    deleted     = db.Column (db.Integer)

    def __init__(self, sku, name, description, brand, price, category_id, file, deleted):
        self.sku            = sku
        self.name           = name
        self.description    = description
        self.brand          = brand
        self.price          = price
        self.category_id    = category_id
        self.file           = file
        self.deleted        = deleted

    # Psra que cuando traiga un producto sea con el formato '[<Product 'producto1'>, <Product 'producto2'>]'
    def __repr__(self):
        return '<Product %r>' %(self.name)
        #return '<Product %d>' %(self.id)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'price': self.price,
            'name': self.name 
        }

# Clase para formulario WTF
class ProductForm(FlaskForm):
    sku                 = StringField('SKU del Producto', validators=[InputRequired()])
    name                = StringField('Nombre del Producto', validators=[InputRequired()])
    description         = StringField('Descripción del Producto', validators=[InputRequired()])
    brand               = StringField('Marca del Producto', validators=[InputRequired()])
    price               = DecimalField('Precio del Producto', validators=[InputRequired(), NumberRange(min=Decimal(0.0), max=Decimal(3000.0))])
    category_id         = SelectField('Categoria', coerce=int)
    file                = FileField('Subir archivo') #, validators=[FileRequired()])