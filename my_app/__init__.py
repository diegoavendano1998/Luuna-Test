from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ----------------------------------------------------------------------
# -------------------------- Start App Configs -------------------------
# ----------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://diego:Diegox10*@localhost/dms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = '/home/diego/webApps/DMS/static/img/uploads'
app.config['UPLOAD_FOLDER'] = '/home/diego/Documents/DMS/static/img/uploads'
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
from my_app.modules.auth.authController import auth
app.register_blueprint(productsBP)
app.register_blueprint(auth)
# ----------------------------------------------------------------------
# -------------------------- End Blueprints --------------------------
# ----------------------------------------------------------------------