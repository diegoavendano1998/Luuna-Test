from my_app import app,db
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint
from flask_login import login_required, current_user

from werkzeug.wrappers import BaseRequest
from werkzeug.utils import secure_filename
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from my_app.modules.auth.model.user import User, UserForm, Role
from my_app.modules.products.model.Alert import Alert

import os
from requests.auth import HTTPBasicAuth
import requests
import json




usersBP = Blueprint('users',__name__)


@app.errorhandler(401)
def notAuthorized(e):
    # note that we set the 401 status explicitly
    return render_template('handler/401.html'),401
@app.errorhandler(413)
def notAuthorized(e):
    return render_template('handler/413.html'),413

@usersBP.before_request
@login_required
def contstructor(code=1):
    # if response.status_code == 401:
    # print (current_user.username)
    pass



@usersBP.route('/Luuna/test/')
def get_data():
    uDict = ({'sku':'0000','name':'test','description':'test desc','brand':'test brand','price':44,'category_id':2,'file':"",'deleted':0})
    # GET
    r = json.loads(requests.get('http://0.0.0.0:5000/api/users/',auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # POST
    # r = json.loads(requests.post('http://0.0.0.0:5000/api/users/',data=uDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # print (r['code'])
    print (r)
    return str(r)




# List all users
@usersBP.route('/Luuna/users/')
@usersBP.route('/Luuna/users/<int:page>')
def users(page=1):
    alerts = Alert.query.order_by(Alert.id.desc()).all()
    return render_template('users/users.html',users=User.query.paginate(page,100),alerts=alerts)


# Create user
@usersBP.route('/Luuna/create-user/', methods=['GET','POST'])
def create():
    form = UserForm(meta={'csrf':False})
    roles = [(r.id,r.name) for r in Role.query.all()]
    form.rol.choices = roles
    if request.method == 'GET':
        return render_template('users/create.html', form=form) 
    elif form.validate_on_submit():
        rol="regular"
        if request.form['rol'] == "6":
            rol="admin"
        uDict = ({'username':request.form['username'],'password':request.form['password'],'rol':rol,'email':request.form['mail']})
        # Send request to API
        r = json.loads(requests.post('http://0.0.0.0:5000/api/users/',data=uDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Usuario guardado satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('users/create.html',form=form) 
        return redirect(url_for('users.users'))
    if form.errors:
        # Show flash error
        flash(form.errors,'danger')
    return render_template('users/create.html',form=form) 


# Edit user
@usersBP.route('/Luuna/update-user/<int:id>', methods=['GET','POST'])
def update(id):
    form = UserForm(meta={'csrf':False})
    user = User.query.get_or_404(id)
    roles = [(r.id,r.name) for r in Role.query.all()]
    form.rol.choices = roles
    # Mostrar los valores actuales en la vista del formulario
    if request.method == 'GET':
        form.username.data        = user.username
        form.password.data        = user.password
        form.rol.data             = user.rol
        form.mail.data            = user.email
    elif form.validate_on_submit():
        rol="regular"
        if request.form['rol'] == "6":
            rol="admin"
        uDict = ({'username':request.form['username'],'password':request.form['password'],'rol':rol,'email':request.form['mail']})
        # Send request to API
        r = json.loads(requests.put('http://0.0.0.0:5000/api/users/'+str(id),data=uDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Usuario actualizada satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('users/update.html', user=user, form=form)
        return redirect(url_for('users.users'))
    if form.errors:
        # Mostrar flash de error
        flash(form.errors,'danger')

    return render_template('users/update.html', user=user, form=form)


# Delete user
@usersBP.route('/Luuna/delete-user/<int:id>')
def delete(id):
    # Send request to API
    r = json.loads(requests.delete('http://0.0.0.0:5000/api/users/'+str(id),auth = HTTPBasicAuth('luuna', 'test2021')).content)
    if r['code'] == 200:
        flash('Usuario eliminada satisfactoriamente','success')
    else:
        flash(r['message'],'danger')
    return redirect(url_for('users.users'))



    
