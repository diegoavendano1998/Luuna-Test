from my_app import app,db,ALLOWED_EXTENSION_FIELDS
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint

from werkzeug.wrappers import BaseRequest
from werkzeug.utils import secure_filename
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from my_app.modules.products.model.Category import Category, CategoryForm

import os
from requests.auth import HTTPBasicAuth
import requests
import json




categoriesBP = Blueprint('categories',__name__)





@categoriesBP.route('/Luuna/test/')
def get_data():
    cDict = ({'sku':'0000','name':'test','description':'test desc','brand':'test brand','price':44,'category_id':2,'file':"",'deleted':0})
    # GET
    r = json.loads(requests.get('http://0.0.0.0:5000/api/categories/',auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # POST
    # r = json.loads(requests.post('http://0.0.0.0:5000/api/categories/',data=cDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # print (r['code'])
    print (r)
    return str(r)




# List all categories
@categoriesBP.route('/Luuna/categories/')
@categoriesBP.route('/Luuna/categories/<int:page>')
def categories(page=1):
    return render_template('categories/categories.html',categories=Category.query.paginate(page,6))


# Create category
@categoriesBP.route('/Luuna/create-category/', methods=['GET','POST'])
def create():
    form = CategoryForm(meta={'csrf':False})
    categories = [(c.id,c.name) for c in Category.query.all()]
    if request.method == 'GET':
        return render_template('categories/create.html', form=form) 
    elif form.validate_on_submit():
        cDict = ({'name':request.form['name'],'description':request.form['description'],'deleted':0})
        # Send request to API
        r = json.loads(requests.post('http://0.0.0.0:5000/api/categories/',data=cDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Categoría guardada satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('categories/create.html',form=form) 
        return redirect(url_for('categories.categories'))
    if form.errors:
        # Show flash error
        flash(form.errors,'danger')
    return render_template('categories/create.html',form=form) 


# Edit category
@categoriesBP.route('/Luuna/update-category/<int:id>', methods=['GET','POST'])
def update(id):
    form = CategoryForm(meta={'csrf':False})
    category = Category.query.get_or_404(id)
    # Mostrar los valores actuales en la vista del formulario
    if request.method == 'GET':
        form.name.data        = category.name
        form.description.data = category.description
    elif form.validate_on_submit():
        cDict = ({'name':request.form['name'],'description':request.form['description'],'deleted':0})
        # Send request to API
        r = json.loads(requests.put('http://0.0.0.0:5000/api/categories/'+str(id),data=cDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Categoría actualizada satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('categories/update.html', category=category, form=form)
        return redirect(url_for('categories.categories'))
    if form.errors:
        # Mostrar flash de error
        flash(form.errors,'danger')

    return render_template('categories/update.html', category=category, form=form)


# Delete category
@categoriesBP.route('/Luuna/delete-category/<int:id>')
def delete(id):
    # Send request to API
    r = json.loads(requests.delete('http://0.0.0.0:5000/api/categories/'+str(id),auth = HTTPBasicAuth('luuna', 'test2021')).content)
    if r['code'] == 200:
        flash('Categoría eliminada satisfactoriamente','success')
    else:
        flash(r['message'],'danger')
    return redirect(url_for('categories.categories'))



    
