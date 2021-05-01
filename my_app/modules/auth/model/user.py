from my_app import db
# Importaciones para WTF
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Email
from sqlalchemy import Enum
from werkzeug.security import check_password_hash, generate_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user 
from flask_user import UserMixin

import enum

class RolUser(enum.Enum):
    regular = 1
    admin = 6


class User (db.Model, UserMixin):
    __tablename__       = 'users'
    id                  = db.Column (db.Integer, primary_key=True)
    username            = db.Column (db.String(200))
    # Se guarda el password hasehado
    password            = db.Column (db.String(255))
    rol                 = db.Column (db.String(255))
    active              = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email               = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at  = db.Column(db.DateTime())
    #birthday = db.Column(db.Date)
    # Relationships
    roles = db.relationship('Role', secondary='user_roles')

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)


    def __init__(self, username, password, rol, email):
        self.username = username
        self.password = password
        self.rol      = rol
        self.email    = email

    # Psra que cuando traiga un User sea con el formato '[<User 'User1'>, <User 'User2'>]'
    def __repr__(self):
        return '<User %r>' %(self.username)
    
    # Al hacer referencia al self es como si se estuvira haciendo refencia al password
    def check_password(self, password):
        # Hace una comparacion etre el hash del password ingresado contra el de la BD
        return check_password_hash(self.password, password)


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id            = db.Column(db.Integer(), primary_key=True)
    name          = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id            = db.Column(db.Integer(), primary_key=True)
    user_id       = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id       = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return "<h1>Usuario no autenticado</h1>"


class UserModelView(AdminModelView):
    #can_edit = False
    create_modal = True
    edit_modal = True
    can_export = True
    export_max_rows = 15
    column_searchable_list = ['username', 'rol']
    column_filters = ['rol']
    column_exclude_list = ['password']
    # form_choices = {
    #     'username': [
    #         ('MR', 'Mr'),
    #         ('MRS', 'Mrs'),
    #         ('MS', 'Ms'),
    #         ('DR', 'Dr'),
    #         ('PROF', 'Prof.')
    #     ]
    # }
    form_args = {
        'username': {
            'label': 'Usuario',
            'validators': [InputRequired()]
        },
        'password': {
            'label': 'Contraseña',
            'validators': [InputRequired()]
        },
        'rol': {
            'label': 'Rol',
            'validators': [InputRequired()]
        }
    }

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)

    def edit_form(self, obj=None):
        form = super(UserModelView, self).edit_form(obj)
        form.password.data = ""
        return form


# Clase para formulario WTF
class LoginForm(FlaskForm):
    username    = StringField('Usuario', validators=[InputRequired()])
    password    = PasswordField('Contraseña', validators=[InputRequired()])
    next        = HiddenField('next')


class RegisterForm(FlaskForm):
    username    = StringField('Usuario', validators=[InputRequired()])
    password    = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('confirm', message='Las contraseñas deben ser iguales')])
    confirm     = PasswordField('Confirmar contraseña')
    mail        = EmailField('E-Mail', validators=[InputRequired(),Email()])

class UserForm(FlaskForm):
    username    = StringField('Usuario', validators=[InputRequired()])
    password    = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('confirm', message='Las contraseñas deben ser iguales')])
    confirm     = PasswordField('Confirmar contraseña')
    rol         = SelectField('Rol', coerce=int)
    mail        = EmailField('E-Mail', validators=[InputRequired(),Email()])

class ForgotPassword(FlaskForm):
    username = StringField('Usuario o correo electronico', validators=[InputRequired()])