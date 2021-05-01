from my_app import db

from flask_wtf import FlaskForm
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user 
from flask_user import UserMixin

from wtforms import StringField, PasswordField, HiddenField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Email

from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy import Enum
import enum

class RolUser(enum.Enum):
    regular = 1
    admin = 6


class User (db.Model, UserMixin):
    __tablename__       = 'users'
    id                  = db.Column (db.Integer, primary_key=True)
    username            = db.Column (db.String(200))
    # Hash the password
    password            = db.Column (db.String(255))
    rol                 = db.Column (db.String(255))
    active              = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email               = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at  = db.Column(db.DateTime())
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


    def __repr__(self):
        return '<User %r>' %(self.username)
    
    def check_password(self, password):
        # Check for the hashed password
        return check_password_hash(self.password, password)


# Define Role model
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


# Forms for login 
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