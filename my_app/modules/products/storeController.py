from my_app import app, db, check_admin
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint
from flask_login import login_required, current_user
from flask_user import roles_required

from werkzeug.wrappers import BaseRequest
from werkzeug.utils import secure_filename
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from my_app.modules.products.model.Product import Product
from my_app.modules.products.model.Track import Track

import os
from requests.auth import HTTPBasicAuth
import requests
import json


storeBP = Blueprint('store',__name__)



@app.errorhandler(401)
def notAuthorized(e):
    return render_template('handler/401.html'),401
@app.errorhandler(413)
def notAuthorized(e):
    return render_template('handler/413.html'),413

@storeBP.before_request
@login_required
def contstructor(code=1):
    pass




@storeBP.route('/Luuna/store/')
def store():
    r = json.loads(requests.get('http://0.0.0.0:5000/api/products/',auth = HTTPBasicAuth('luuna', 'test2021')).content)
    return render_template('products/store.html',products=r['data'])


@storeBP.route('/Luuna/store/<int:id>')
def show(id):
    p = Product.query.get_or_404(id)
    # Add to tracking the request
    track = Track(current_user.id,str(current_user.username),id,p.name)
    db.session.add(track)
    db.session.commit()
    r = json.loads(requests.get('http://0.0.0.0:5000/api/products/'+str(id),auth = HTTPBasicAuth('luuna', 'test2021')).content)
    return render_template('products/show.html',product=r['data'])



