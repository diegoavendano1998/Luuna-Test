class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234QWER@localhost:3306/pyalmacen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Tiempo de expiracion del token
    WTF_CSRF_TIME_LIMIT = 2000
    # RECAPTCHA_PUBLIC_KEY = '6Lf02a4ZAAAAANl94BBl3SMb8i_MMmwHzw27MF6e'
    # RECAPTCHA_PRIVATE_KEY = '6Lf02a4ZAAAAAF7pkUFULzmOpKz7Iv71wgxt-Uc4'
    BABEL_TRANSLATION_DIRECTORIES = r'C:\Users\Lenovo\Documents\Flask con Python 3 + integración con Vue y Bootstrap 4\flask\4 - flaskApp\flask_app\translations'
    USER_ENABLE_EMAIL = True
    USER_APP_NAME = "Flask-User Admin" 
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'Desarrollo key'
    # Servicio flask-mail
    MAIL_SUPPRESS_SEND = False
    MAIL_SERVER = "smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = '47d8e5888734e1' #fanipof786@brbqx.com
    MAIL_PASSWORD = 'abfc11af980f96'
    MAIL_DEFAULT_SENDER = ("FlaskApp","admin@FlaskApp.mx")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    USER_EMAIL_SENDER_EMAIL = "admin@FlaskApp.mx"
    CACHE_TYPE = "simple"
    DEBUG_TB_INTERCEPT_REDIRECTS = False