from flask.views import MethodView
from flask import request, abort
# from werkzeug import abort
from my_app.modules.auth.model.user import User
from my_app.modules.rest_api.helper.request import responseJSON
from my_app import app, db
import json


class UserAPI(MethodView):
    # Find all users
    def get(self,id=None):
        if id:
            user = User.query.get(id)
            if not user:
               return responseJSON(None,"Parametros invalidos (id)",403)
            else:
               res = userToJSON(user)
        else:
            users = User.query.all()
            res=[]
            for p in users:
                res.append(userToJSON(p))
        return responseJSON(res,None,200)


    # Add user
    def post(self):
        # NAME
        if not request.form:
            return responseJSON(None,"Sin parametros",403)
        if not "username" in request.form:
            return responseJSON(None,"Parametros invalidos (username)",403)
        # Check for name not null
        if len(request.form['username']) < 1:
            return responseJSON(None,"Nombre invalido",403)
        # PASSWORD
        if not "password" in request.form:
            return responseJSON(None,"Parametros invalidos (password)",403)
        if len(request.form['password']) < 1:
            return responseJSON(None,"Constraseña invalida",403)
        # ROLE
        if not "rol" in request.form:
            return responseJSON(None,"Parametros invalidos (rol)",403)
        if len(request.form['rol']) < 1:
            return responseJSON(None,"Rol invalida",403)   
        # MAIL
        if not "email" in request.form:
            return responseJSON(None,"Parametros invalidos (email)",403)
        if len(request.form['email']) < 1:
            return responseJSON(None,"Email invalida",403)   
        

        # Add user
        u = User(request.form['username'],request.form['password'],request.form['rol'],request.form['email'])
        db.session.add(u)
        db.session.commit()
        return responseJSON("userToJSON(p)",None,200) 


    def put(self, id):
        if id:
            u = User.query.get(id)
            if not u:
                return responseJSON(None,"Parametros invalidos (id)",403)

            # NAME
            if not request.form:
                return responseJSON(None,"Sin parametros",403)
            if not "username" in request.form:
                return responseJSON(None,"Parametros invalidos (username)",403)
            # Check for name not null
            if len(request.form['username']) < 1:
                return responseJSON(None,"Nombre invalido",403)
            # PASSWORD
            if not "password" in request.form:
                return responseJSON(None,"Parametros invalidos (password)",403)
            if len(request.form['password']) < 1:
                return responseJSON(None,"Constraseña invalida",403)
            # ROLE
            if not "rol" in request.form:
                return responseJSON(None,"Parametros invalidos (rol)",403)
            if len(request.form['rol']) < 1:
                return responseJSON(None,"Rol invalida",403)   
            # MAIL
            if not "email" in request.form:
                return responseJSON(None,"Parametros invalidos (email)",403)
            if len(request.form['email']) < 1:
                return responseJSON(None,"Email invalida",403)   

            
            # Crear producto
            u.username        = request.form['username']
            u.password        = request.form['password']
            u.rol             = request.form['rol']
            u.email           = request.form['email']
            db.session.add(u)
            db.session.commit()
            return responseJSON(userToJSON(u),None,200)
            
        return responseJSON(None,"Id invalido",403)


    # Delete a user
    def delete(self, id):
        if id:
            user = User.query.get(id)
            if not user:
                return responseJSON(None,"Parametros invalidos (id)",403)
            db.session.delete(user)
            db.session.commit()
            return responseJSON("Usuario eliminado",None,200)
        return responseJSON(None,"Id invalido",403)


    

# Convertir query de sqlalchemy a JSON
def userToJSON(user: User):
    return {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'rol': user.rol
            }

# Tambien se puede guarder en la base de datos
api_username="luuna"
api_password="test2021"

# Metodo para proteger API
def protectAPI(f):
    def userDecorated(*args,**kwargs):
        auth = request.authorization
        # print (auth.username+","+api_username)
        # print (auth.password+","+api_password)
        if api_username == auth.username and api_password == auth.password:
            return f(*args, **kwargs)
        # Regresar error unauthorized
        return abort(401)
    return userDecorated


### Rutas ###
# user_view = UserAPI.as_view('user_view')
user_view = protectAPI(UserAPI.as_view('user_view'))
# GET
app.add_url_rule('/api/users/', view_func=user_view, methods=['GET','POST'])
# CRUD
app.add_url_rule('/api/users/<int:id>', view_func=user_view, methods=['GET','POST','PUT','DELETE'])
# # POST
# user_view = UserAPI.as_view('user_view')
# app.add_url_rule('/api/users', view_func=user_view, methods=['GET'])
# # PUT
# user_view = UserAPI.as_view('user_view')
# app.add_url_rule('/api/users', view_func=user_view, methods=['GET'])
