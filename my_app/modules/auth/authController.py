from flask import Blueprint, session, render_template, request, redirect, url_for, flash, get_flashed_messages
from my_app.modules.auth.model.user import User, LoginForm, RegisterForm, ForgotPassword, Role, RolUser
from my_app import db
from flask_login import login_user, logout_user, current_user, login_required
from my_app import login_manager

import atexit
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

auth = Blueprint('auth',__name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Registrar usuario
@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(meta={'csrf':False})
    if (request.method == "POST"):
        if form.validate_on_submit():
            # Validar que el usuraio no exista
            if User.query.filter_by(username=form.username.data).first():
                flash('El usuario ya existe','danger')
                return redirect(url_for('auth.register'))
            if User.query.filter_by(email=form.mail.data).first():
                flash('El correo ya esta registrado','danger')
                return redirect(url_for('auth.register'))
            else:
                p = User(form.username.data,form.password.data,form.mail.data)
                db.session.add(p)
                db.session.commit()
                os.mkdir("/media/diego/ADATA HV620S/"+form.username.data)
                flash('Usuario creado satisfactoriamente','success')
                return redirect(url_for('auth.login'))
    if form.errors:
            value = str(sorted(form.errors.values()))
            msgs = value.split(",")
            for msg in msgs:
                msg = msg.replace("[",'')
                msg = msg.replace("]",'')
                msg = msg.replace("'","")
                flash(msg,'danger')

    return render_template('auth/register.html', form=form)


# Logear usuario
@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('Sesion actual activa','danger')
        return redirect (url_for('cld.index'))
    form = LoginForm(meta={'csrf':False})
    if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            password = User.query.filter_by(password=form.password.data).first()
            # Validar credenciales
            if user and password:
                login_user(user)
                flash('Bienvenido '+user.username,'success')
                next = request.form['next']
                # Revisar que la ruta de redireccoin sea segura
                # if not is_safe_url(next):
                #     return abort(400)
                return redirect (next or url_for('cld.index'))
            else:
                flash(u'El usuario no existe o la contraseña es incorrecta','danger')
                return render_template('auth/login.html', form=form)   
    if form.errors:
        flash(form.errors,'danger')

    return render_template('auth/login.html', form=form) 

# Cerrar session del usuario
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def SendMail(reciver,passwd):
        sender_email = "diegoavendano1998a@gmail.com"
        receiver_email = reciver
        password = "th4t$ Life"
        message = MIMEMultipart("alternative")
        message["Subject"] = "My cloud: Recuperacion Contraseña"
        message["From"] = sender_email
        message["To"] = receiver_email
        # Create the plain-text and HTML version of your message
        text = " Tu contraseña es :      "+passwd
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")

        message.attach(part1)
        # message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    

# Recuperar contraseña
@auth.route('/forgot', methods=['GET','POST'])
@auth.route('/forgot')
def forgotPassword():
    form = ForgotPassword(meta={'csrf':False})
    if (request.method == "POST"):
        if form.validate_on_submit():
            # Validar que el usuraio no exista
            if User.query.filter_by(username=form.username.data).first():
                # try:
                user = User.query.filter_by(username=form.username.data).first()
                SendMail(user.email,user.password)
                flash('Correo de recuperacion enviado','success')
                return redirect(url_for('auth.forgotPassword'))
                # except:
                #     flash('Por favor, intentalo mas tarde','danger')

            elif User.query.filter_by(email=form.username.data).first():
                flash('Correo de recuperacion enviado','success')
                return redirect(url_for('auth.forgotPassword'))
            else:
                flash('El userio o correo no estan registrados','danger')
                return redirect(url_for('auth.forgotPassword'))
    return render_template('auth/forgotPassword.html', form=form)

