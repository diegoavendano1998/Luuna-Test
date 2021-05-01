from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ----------------------------------------------------------------------
# -------------------------- Start App Configs -------------------------
# ----------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = 'Secret Key'





#cargar las configuraciones, incliuyendo las de la bd
app.config.from_object('configuration.DevelopmentConfig')
ALLOWED_EXTENSION_FIELDS = set(['pdf','jpg','jpeg','png'])

# # # # # DB instance # # # # #
db = SQLAlchemy(app)
# ######### Crear las tablas en la base de datos ##########
#     En python : 
#     > python
#     > from app import db
#     > db.create_all()

# # # # # Login Manager # # # # #
login_manager=LoginManager()
login_manager.init_app(app)
# ----------------------------------------------------------------------
# -------------------------- End App Configs ---------------------------
# ----------------------------------------------------------------------






# ----------------------------------------------------------------------
# -------------------------- Start Blueprints --------------------------
# ----------------------------------------------------------------------
from my_app.modules.products.productsController import productsBP
from my_app.modules.products.categoriesController import categoriesBP
from my_app.modules.auth.usersController import usersBP
from my_app.modules.auth.authController import auth
app.register_blueprint(productsBP)
app.register_blueprint(categoriesBP)
app.register_blueprint(usersBP)
app.register_blueprint(auth)
# ----------------------------------------------------------------------
# -------------------------- End Blueprints --------------------------
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# -------------------------- Start APIs --------------------------
# ----------------------------------------------------------------------
from my_app.modules.rest_api.product_api import product_view
from my_app.modules.rest_api.category_api import category_view
from my_app.modules.rest_api.user_api import user_view
# ----------------------------------------------------------------------
# -------------------------- End APIs --------------------------
# ----------------------------------------------------------------------

