from my_app import app,db,ALLOWED_EXTENSION_FIELDS
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint

from werkzeug.wrappers import BaseRequest
from werkzeug.utils import secure_filename
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from my_app.modules.products.model.Product import Product, ProductForm
from my_app.modules.products.model.Category import Category, CategoryForm

import os
from requests.auth import HTTPBasicAuth
import requests
import json




productsBP = Blueprint('products',__name__)




def check_extension_file(filename):
   return ('.' in filename and filename.lower().rsplit('.')[1] in ALLOWED_EXTENSION_FIELDS)


@productsBP.route('/Luuna/test/')
def get_data():
    pDict = ({'sku':'0000','name':'test','description':'test desc','brand':'test brand','price':44,'category_id':2,'file':"",'deleted':0})
    # GET
    r = json.loads(requests.get('http://0.0.0.0:5000/api/products/',auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # POST
    # r = json.loads(requests.post('http://0.0.0.0:5000/api/products/',data=pDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
    # print (r['code'])
    print (r)
    return str(r)




# List all products
@productsBP.route('/Luuna/products/')
@productsBP.route('/Luuna/products/<int:page>')
def products(page=1):
    products = Product.query.all()
    return render_template('products/products.html',products=Product.query.paginate(page,4))


# Create product
@productsBP.route('/Luuna/create-product/', methods=['GET','POST'])
def create():
    form = ProductForm(meta={'csrf':False})#meta={'csrf':False}
    categories = [(c.id,c.name) for c in Category.query.all()]
    form.category_id.choices = categories
    # Mostrar los valores actuales en la vista del formulario
    if request.method == 'GET':
        return render_template('products/create.html', form=form) 
    elif form.validate_on_submit():
        pDict = ({'sku':request.form['sku'],'name':request.form['name'],'description':request.form['description'],'brand':request.form['brand'],'price':request.form['price'],'category_id':request.form['category_id'],'deleted':0})
        # Validar extension del archivo
        if form.file.data:
            file = form.file.data
            if check_extension_file(file.filename):
                filename= secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
                pDict["file"]=("some file")
            else:
                flash('Archivo invalido (extensiones permitidas: jpg, jpeg, png, pdf)','danger')
                return redirect(url_for('products.create'))
        else:
            pDict["file"]=("")
        # Send request to API
        r = json.loads(requests.post('http://0.0.0.0:5000/api/products/',data=pDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Producto guardado satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('products/create.html',form=form) 
        return redirect(url_for('products.products'))
    if form.errors:
        # Show flash error
        flash(form.errors,'danger')
    return render_template('products/create.html',form=form) 


# Edit product
@productsBP.route('/Luuna/update-product/<int:id>', methods=['GET','POST'])
def update(id):
    form = ProductForm(meta={'csrf':False})#meta={'csrf':False}
    categories = [(c.id,c.name) for c in Category.query.all()]
    form.category_id.choices = categories
    product = Product.query.get_or_404(id)
    # Mostrar los valores actuales en la vista del formulario
    if request.method == 'GET':
        form.sku.data         = product.sku
        form.name.data        = product.name
        form.description.data = product.description
        form.brand.data       = product.brand
        form.price.data       = product.price
        form.category_id.data = product.category_id
        form.file.data        = product.file
    elif form.validate_on_submit():
        pDict = ({'sku':request.form['sku'],'name':request.form['name'],'description':request.form['description'],'brand':request.form['brand'],'price':request.form['price'],'category_id':request.form['category_id'],'deleted':0})
        # Validar extension del archivo
        if form.file.data:
            file = form.file.data
            if check_extension_file(file.filename):
                filename= secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
                pDict["file"]=("some file")
            else:
                flash('Archivo invalido (extensiones permitidas: jpg, jpeg, png, pdf)','danger')
                return redirect(url_for('products.create'))
        else:
            pDict["file"]=("")
        
        # Send request to API
        r = json.loads(requests.put('http://0.0.0.0:5000/api/products/'+str(id),data=pDict,auth = HTTPBasicAuth('luuna', 'test2021')).content)
        if r['code'] == 200:
            flash('Producto actualizado satisfactoriamente','success')
        else:
            flash(r['message'],'danger')
            return render_template('products/update.html', product=product, form=form)
        return redirect(url_for('products.products'))
    if form.errors:
        # Mostrar flash de error
        flash(form.errors,'danger')

    return render_template('products/update.html', product=product, form=form)


# Delete product
@productsBP.route('/Luuna/delete-product/<int:id>')
def delete(id):
    # Send request to API
    r = json.loads(requests.delete('http://0.0.0.0:5000/api/products/'+str(id),auth = HTTPBasicAuth('luuna', 'test2021')).content)
    if r['code'] == 200:
        flash('Producto eliminado satisfactoriamente','success')
    else:
        flash(r['message'],'danger')
    return redirect(url_for('products.products'))



    
