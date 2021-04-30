from my_app import app 

# app.config.from_pyfile('config.py')
# app.config.from_object('configuration.DevelopmentConfig')
# print(app.config['SECRET_KEY'])

#app.run(ssl_context='adhoc') # Para ejecutar con certificado ssl para recaptcha
app.run(host='0.0.0.0')

# app.config['debug']=True
# app.debug=True