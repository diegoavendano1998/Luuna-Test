from my_app import app
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Blueprint

from werkzeug.wrappers import BaseRequest
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound

productsBP = Blueprint('products',__name__)


@productsBP.route('/Luuna')
def products():
    return render_template('products/products.html')
