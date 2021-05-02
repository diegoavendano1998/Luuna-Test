
[![N|Solid](https://www.eluniversal.com.mx/descuentos/static/shop/32021/logo/Luuna_Cupon.jpg)]()
# Backend Technical Test    
## REST API / Products aplication

#
El proyecto es un sistema para administrar un catálogo de productos. Existen dos tipos de usuario, uno administrador que tiene la capacidad de crear/actualizar/eliminar productos y usuarios. El otro es un usuario regular que solo puede ver los productos y su detalle.
El proyecto esta desarrollado con el lenguaje Python y utiliza como framework Flask. Otras tecnologías empleadas son SQLAchemy como ORM, MySQL como RDBMS, HTTPBasicAuth como administrador de autenticación de la API, etc.

## Features

- Implmentación de API REST protegida con credeciales HTTPBasicAuth
- Administracion de Productos, Categorias y Usuarios
- Sistema de alertas de modifiacion de catalogo de productos
- Tienda de productos
- Sistema de tracking de usuarios
- Sistema de autenticacion de usuarios



## Instalación
Despues de descargar o clonar el proyecto es recomendable crear un entorno virtual de Python 3 utilizando venv o Pipenv.
```sh
pipenv shell
```
Dentro del entorno para descargar las librerias necesarias, puedes ejecutar :

```sh
pip install -r requirements.txt
```
Ahora debes crear una base de datos dentro de MySQL con el nombre 'luunatest' y dentro de ella correr los querys que se encustran en el archivo my_app > msintenance > sql > LuunaDump.sql.
Con la base de datos lista, necesitaras agregar un primer usuario asignandole un rol 'admin'.
Con esto ya tienes lista la estructura en la base de datos, ahora debes actualizar el archivo 'configuration.py' cambiando tu usuario y contraseña de la configuración 'SQLALCHEMY_DATABASE_URI'. Antes de cerrar el archivo asegurate de cambiar la configuracion 'UPLOAD_FOLDER' por un folder dentro de tu sistema.
#
Por ultimo podras ejecutar el proyecto (dentro de la carpeta principal) con el comando:
```sh
python app.py
```
Ya puedes empezar a navegar y si es necesario iniciar sesion con el usuario que has creado previamente.



## Docker

Para contener la aplicacion dentro de un servicio de Docker, se debe crear un Dockerfile como el siguiente:

```sh
FROM python:3.6-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
```

Esto instalara las librerias necesarias y le dira a Docker que corra la aplicación por el puerto 5000.
> Note: `python 3.6` recomendado para evitar confictos con librerias.

Para crear la imagen:
```sh
docker image build -t luuna-image .
```
Docker compose:
```sh
version: "2"
services:
    app:
        build: ./app
        links:
        - db
        ports:
        - "5000:5000"
    db:
        image: mysql:5.7
        ports:
          - "32000:3306"
        environment:
          MYSQL_ROOT_PASSWORD: root
        volumes:
          - ./db:/docker-entrypoint-initdb.d/:ro
```
Por ultimo iniciamos el contenedor:
```sh
sudo docker run --name luuna-image -p 5001:5000 luuna-image
```
Verificamos el despliegue en el navegador

```sh
0.0.0.0:5000/Luuna/products
```


## Tech

Las librerias utilizadas son :

- bcrypt==3.2.0
- blinker==1.4
- certifi==2020.12.5
- cffi==1.14.5
- chardet==4.0.0
- click==7.1.2
- cryptography==3.4.7
- dnspython==2.1.0
- email-validator==1.1.2
- Flask==1.1.2
- Flask-Admin==1.5.8
- Flask-Login==0.5.0
- Flask-Mail==0.9.1
- Flask-SQLAlchemy==2.5.1
- Flask-User==1.0.2.2
- Flask-WTF==0.14.3
- greenlet==1.0.0
- idna==2.10
- importlib-metadata==4.0.1
- itsdangerous==1.1.0
- Jinja2==2.11.3
- MarkupSafe==1.1.1
- passlib==1.7.4
- pycparser==2.20
- PyMySQL==1.0.2
- requests==2.25.1
- six==1.15.0
- SQLAlchemy==1.4.12
- typing-extensions==3.7.4.3
- urllib3==1.26.4
- Werkzeug==1.0.1
- WTForms==2.3.3
- zipp==3.4.1


## Proyecto desplegado
Para ver el proyecto desplegado puedes entrar a la url: http://diegoab.ddns.net/Luuna/store/
### Usuarios:
- username : admin-luuna , password : ZeBrands$
- username : regular-luuna , password : ZeBrands$


#
## License

Diego Avendaño, 2021

**Free Software, Hell Yeah!**
