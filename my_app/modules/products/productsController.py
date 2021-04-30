from my_app import app,db,ALLOWED_EXTENSION_FIELDS
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint

from werkzeug.wrappers import BaseRequest
from werkzeug.utils import secure_filename
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

from my_app.modules.products.model.Product import Product, ProductForm
from my_app.modules.products.model.Category import Category, CategoryForm

import os




productsBP = Blueprint('products',__name__)




def check_extension_file(filename):
   return ('.' in filename and filename.lower().rsplit('.')[1] in ALLOWED_EXTENSION_FIELDS)



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
        p = Product(request.form['sku'],request.form['name'],request.form['description'],request.form['brand'],request.form['price'],request.form['category_id'],"",0)
        # Validar extension del archivo
        if form.file.data:
            file = form.file.data
            if check_extension_file(file.filename):
                filename= secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
                p.file = filename 
            else:
                flash('Archivo invalido (extensiones permitidas: jpg, jpeg, png, pdf)','danger')
                return redirect(url_for('products.create'))
        db.session.add(p)
        db.session.commit()
        flash('Producto guardado satisfactoriamente','success')
        return redirect(url_for('products.products'))
    if form.errors:
        # Mostrar flash de error
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
        product               = Product.query.get_or_404(id)
        product.sku           = form.sku.data
        product.name          = form.name.data
        product.description   = form.description.data
        product.brand         = form.brand.data
        product.price         = form.price.data
        product.category_id   = form.category_id.data
        # Validar extension del archivo
        if form.file.data:
            file = form.file.data
            if check_extension_file(file.filename):
                filename= secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
                product.file = filename
            else:
                flash('Archivo invalido (extensiones permitidas: jpg, jpeg, png, pdf)','danger')
                return redirect(url_for('products.update',id=product.id))
        db.session.add(product)
        db.session.commit()
        flash('Producto actualizado satisfactoriamente','success')
        return redirect(url_for('products.products'))
    if form.errors:
        # Mostrar flash de error
        flash(form.errors,'danger')

    return render_template('products/update.html', product=product, form=form)


# Delete product
@productsBP.route('/Luuna/delete-product/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)
    # p = Product(product.sku,product.name,product.description,product.brand,product.price,product.category_id,"",product.created,1)
    # db.session.add(p)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado satisfactoriamente','success')
    return redirect(url_for('products.products'))



    
