from flask.views import MethodView
from flask import request, abort
from flask_login import LoginManager, login_required, current_user
# from werkzeug import abort
from my_app.modules.products.model.Product import Product, ProductForm
from my_app.modules.products.model.Alert import Alert
from my_app.modules.rest_api.helper.request import responseJSON
from my_app import app, db
import json


class ProductAPI(MethodView):
    # Find all products
    def get(self,id=None):
        if id:
            product = Product.query.get(id)
            if not product:
               return responseJSON(None,"Parametros invalidos (id)",403)
            else:
               res = productToJSON(product)
        else:
            products = Product.query.all()
            res=[]
            for p in products:
                res.append(productToJSON(p))
        return responseJSON(res,None,200)

    # Delete a product
    def delete(self, id):
        if id:
            product = Product.query.get(id)
            alert = Alert(product.name+" ha sido eliminado",0)
            if not product:
                return responseJSON(None,"Parametros invalidos (id)",403)
            db.session.add(alert)
            db.session.delete(product)
            db.session.commit()
            return responseJSON("Prodcuto eliminado",None,200)
        return responseJSON(None,"Id invalido",403)

    # Add product
    def post(self):
        # NAME
        if not request.form:
            return responseJSON(None,"Sin parametros (name)",403)
        if not "name" in request.form:
            return responseJSON(None,"Parametros invalidos (name)",403)
        # Check for name not null
        if len(request.form['name']) < 1:
            return responseJSON(None,"Nombre invalido",403)
        # SKU
        if not "sku" in request.form:
            return responseJSON(None,"Parametros invalidos (sku)",403)
        if len(request.form['sku']) < 1:
            return responseJSON(None,"SKU invalido",403)
        # DESCRIPTION
        if not "description" in request.form:
            return responseJSON(None,"Parametros invalidos (description)",403)
        if len(request.form['description']) < 1:
            return responseJSON(None,"Descripcción invalida",403)
        # BRAND
        if not "brand" in request.form:
            return responseJSON(None,"Parametros invalidos (brand)",403)
        if len(request.form['brand']) < 1:
            return responseJSON(None,"Marca invalida",403)   
        # PRICE
        if not "price" in request.form:
            return responseJSON(None,"Sin parametros (price)",403)
        # Cast price to float
        try:
            float(request.form['price'])
            # Price > 0
            if float(request.form['price']) <= 0:
                return responseJSON(None,"Precio invalido",403)
        except ValueError:
            return responseJSON(None,"Parametros invalidos (price)",403)
        # CATEGORY
        if not "category_id" in request.form:
            return responseJSON(None,"Sin parametros (category_id)",403)
        # Cast to int
        try:
            int(request.form['category_id'])
        except ValueError:
            return responseJSON(None,"Parametros invalidos (category_id)",403)

        # Add product
        p = Product(request.form['sku'],request.form['name'],request.form['description'],request.form['brand'],request.form['price'],request.form['category_id'],request.form['file'],0)
        alert = Alert(request.form['name']+" ha sido añadido.",0)
        db.session.add(p)
        db.session.add(alert)
        db.session.commit()
        return responseJSON(productToJSON(p),None,200) 

    # Edit product
    def put(self, id):
        if id:
            product = Product.query.get(id)
            if not product:
                return responseJSON(None,"Parametros invalidos (id)",403)

            # NAME
            if not request.form:
                return responseJSON(None,"Sin parametros (name)",403)
            if not "name" in request.form:
                return responseJSON(None,"Parametros invalidos (name)",403)
            # Check for name not null
            if len(request.form['name']) < 1:
                return responseJSON(None,"Nombre invalido",403)
            # SKU
            if not "sku" in request.form:
                return responseJSON(None,"Parametros invalidos (sku)",403)
            if len(request.form['sku']) < 1:
                return responseJSON(None,"SKU invalido",403)
            # DESCRIPTION
            if not "description" in request.form:
                return responseJSON(None,"Parametros invalidos (description)",403)
            if len(request.form['description']) < 1:
                return responseJSON(None,"Descripcción invalida",403)
            # BRAND
            if not "brand" in request.form:
                return responseJSON(None,"Parametros invalidos (brand)",403)
            if len(request.form['brand']) < 1:
                return responseJSON(None,"Marca invalida",403)   
            # PRICE
            if not "price" in request.form:
                return responseJSON(None,"Sin parametros (price)",403)
            # Cast price to float
            try:
                float(request.form['price'])
                # Price > 0
                if float(request.form['price']) <= 0:
                    return responseJSON(None,"Precio invalido",403)
            except ValueError:
                return responseJSON(None,"Parametros invalidos (price)",403)
            # CATEGORY
            if not "category_id" in request.form:
                return responseJSON(None,"Sin parametros (category_id)",403)
            # Cast to int
            try:
                int(request.form['category_id'])
            except ValueError:
                return responseJSON(None,"Parametros invalidos (category_id)",403)


            
            #Check for changes
            if product.sku != request.form['sku']:
                alertSku=Alert(product.name+" cambio el sku a "+request.form['sku'],0)
                db.session.add(alertSku)
                db.session.commit()
            if product.name != request.form['name']:
                alertName=Alert(product.name+" cambio el nombre a "+request.form['name'],0)
                db.session.add(alertName)
                db.session.commit()
            if product.description != request.form['description']:
                alertDesc=Alert(product.name+" cambio ls descripcción a "+request.form['description'],0)
                db.session.add(alertDesc)
                db.session.commit()
            if product.brand != request.form['brand']:
                alertBrand=Alert(product.name+" cambio la marca a "+request.form['brand'],0)
                db.session.add(alertBrand)
                db.session.commit()
            if product.price != request.form['price']:
                alertPrice=Alert(product.name+" cambio el precio a $"+request.form['price'],0)
                db.session.add(alertPrice)
                db.session.commit()
            if product.category_id != request.form['category_id']:
                alertCategory=Alert(product.name+" cambio la categoría a "+request.form['category_id'],0)
                db.session.add(alertCategory)
                db.session.commit()
            
            # Create product
            product.sku         = request.form['sku']
            product.name        = request.form['name']
            product.description = request.form['description']
            product.brand       = request.form['brand']
            product.price       = request.form['price']
            product.category_id = request.form['category_id']
            product.file        = request.form['file']
            db.session.add(product)
            db.session.commit()
            return responseJSON(productToJSON(product),None,200)
            
        return responseJSON(None,"Id invalido",403)

# Convertir query de sqlalchemy a JSON
def productToJSON(product: Product):
    return {
                'id': product.id,
                'sku': product.sku,
                'name': product.name,
                'description': product.description,
                'brand': product.brand,
                'price': product.price,
                'category_id': product.category.id,
                'category': product.category.name,
                'file': product.file
            }

# Tambien se puede guarder en la base de datos
api_username="luuna"
api_password="test2021"

# Metodo para proteger API
def protectAPI(f):
    def productDecorated(*args,**kwargs):
        auth = request.authorization
        # print (auth.username+","+api_username)
        # print (auth.password+","+api_password)
        if api_username == auth.username and api_password == auth.password:
            return f(*args, **kwargs)
        # Regresar error unauthorized
        return abort(401)
    return productDecorated


### Rutas ###
# product_view = ProductAPI.as_view('product_view')
product_view = protectAPI(ProductAPI.as_view('product_view'))
# GET
app.add_url_rule('/api/products/', view_func=product_view, methods=['GET','POST'])
# CRUD
app.add_url_rule('/api/products/<int:id>', view_func=product_view, methods=['GET','POST','PUT','DELETE'])
# # POST
# product_view = ProductAPI.as_view('product_view')
# app.add_url_rule('/api/products', view_func=product_view, methods=['GET'])
# # PUT
# product_view = ProductAPI.as_view('product_view')
# app.add_url_rule('/api/products', view_func=product_view, methods=['GET'])
