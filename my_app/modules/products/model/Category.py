from my_app import db
# Importaciones para WTF
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, HiddenField
from wtforms.validators import InputRequired, ValidationError

class Category (db.Model):
    __tablename__ = 'categories'
    id              = db.Column (db.Integer, primary_key=True)
    name            = db.Column (db.String(200))
    description     = db.Column (db.String(200))
    deleted         = db.Column (db.Integer,default=0)
    products        = db.relationship('Product', backref='category', lazy='select')

    def __init__(self, name, description, deleted):
        self.name        = name
        self.description = description
        self.deleted     = 0

    # Psra que cuando traiga un category sea con el formato '[<Category 'category1'>, <Category 'category2'>]'
    def __repr__(self):
        return '<Category %r>' %(self.name)
        #return '<Category %d>' %(self.id)

# Validacion personalizada para evitar categorias repetidas
def checkCategory(form,field):
    res = Category.query.filter_by(name = field.data).first()
    if res:
        raise ValidationError('La categoria %s ya existe' %field.data)

# Validacion personalizada para evitar cateorias repetida y/o que el nombre no este contenida en otra categoria
def checkCategoryName(contain=True):
    def _checkCategoryName(form,field):
        if contain:
            res = Category.query.filter(Category.name.like("%"+field.data+"%")).first()
            if res:
                raise ValidationError('La categoría %s tiene un nombre que esta contenido dentro de otra categoría' %field.data)
        else:
            res = Category.query.filter(Category.name.like(field.data)).first()
            if res:# and form.id.data and res.id != int(form.id.data):
                raise ValidationError('La categoría %s ya existe' %field.data)
    return _checkCategoryName

# Clase para formulario WTF
class CategoryForm(FlaskForm):
    name = StringField('Nombre de la Categoría', validators=[InputRequired(),checkCategoryName(contain=False)])
    description = StringField('Descripccion de la Categoría', validators=[InputRequired()])
    id = HiddenField('Id')
    #recaptcha = RecaptchaField()