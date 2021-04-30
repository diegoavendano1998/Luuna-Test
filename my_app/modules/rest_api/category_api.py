from flask.views import MethodView
from flask import request, abort
# from werkzeug import abort
from my_app.modules.products.model.Category import Category, Category
from my_app.modules.rest_api.helper.request import responseJSON
from my_app import app, db
import json


class CategoryAPI(MethodView):
    # Find all categories
    def get(self,id=None):
        if id:
            category = Category.query.get(id)
            if not category:
               return responseJSON(None,"Parametros invalidos (id)",403)
            else:
               res = categoryToJSON(category)
        else:
            categories = Category.query.all()
            res=[]
            for p in categories:
                res.append(categoryToJSON(p))
        return responseJSON(res,None,200)

    
    # Add category
    def post(self):
        # NAME
        if not request.form:
            return responseJSON(None,"Sin parametros (name)",403)
        if not "name" in request.form:
            return responseJSON(None,"Parametros invalidos (name)",403)
        # Check for name not null
        if len(request.form['name']) < 1:
            return responseJSON(None,"Nombre invalido",403)
        # DESCRIPTION
        if not "description" in request.form:
            return responseJSON(None,"Parametros invalidos (description)",403)
        if len(request.form['description']) < 1:
            return responseJSON(None,"Descripcción invalida",403)
        

        # Add category
        c = Category(request.form['name'],request.form['description'],0)
        db.session.add(c)
        db.session.commit()
        return responseJSON("categoryToJSON(c)",None,200) 


    # Edit category
    def put(self, id):
        if id:
            category = Category.query.get(id)
            if not category:
                return responseJSON(None,"Parametros invalidos (id)",403)

            # NAME
            if not request.form:
                return responseJSON(None,"Sin parametros (name)",403)
            if not "name" in request.form:
                return responseJSON(None,"Parametros invalidos (name)",403)
            # Check for name not null
            if len(request.form['name']) < 1:
                return responseJSON(None,"Nombre invalido",403)
            # DESCRIPTION
            if not "description" in request.form:
                return responseJSON(None,"Parametros invalidos (description)",403)
            if len(request.form['description']) < 1:
                return responseJSON(None,"Descripcción invalida",403)

            # Crear categoria
            category.name        = request.form['name']
            category.description = request.form['description']
            db.session.add(category)
            db.session.commit()
            return responseJSON(categoryToJSON(category),None,200)
            
        return responseJSON(None,"Id invalido",403)


    # Delete a category
    def delete(self, id):
        if id:
            category = Category.query.get(id)
            if not category:
                return responseJSON(None,"Parametros invalidos (id)",403)
            db.session.delete(category)
            db.session.commit()
            return responseJSON("Categoría eliminada",None,200)
        return responseJSON(None,"Id invalido",403)


# Convertir query de sqlalchemy a JSON
def categoryToJSON(category: Category):
    return {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }

# Tambien se puede guarder en la base de datos
api_username="luuna"
api_password="test2021"

# Metodo para proteger API
def protectAPI(f):
    def categoryDecorated(*args,**kwargs):
        auth = request.authorization
        # print (auth.username+","+api_username)
        # print (auth.password+","+api_password)
        if api_username == auth.username and api_password == auth.password:
            return f(*args, **kwargs)
        # Regresar error unauthorized
        return abort(401)
    return categoryDecorated


### Rutas ###
# category_view = CategoryAPI.as_view('category_view')
category_view = protectAPI(CategoryAPI.as_view('category_view'))
# GET
app.add_url_rule('/api/categories/', view_func=category_view, methods=['GET','POST'])
# CRUD
app.add_url_rule('/api/categories/<int:id>', view_func=category_view, methods=['GET','POST','PUT','DELETE'])
# # POST
# category_view = CategoryAPI.as_view('category_view')
# app.add_url_rule('/api/categories', view_func=category_view, methods=['GET'])
# # PUT
# category_view = CategoryAPI.as_view('category_view')
# app.add_url_rule('/api/categories', view_func=category_view, methods=['GET'])
