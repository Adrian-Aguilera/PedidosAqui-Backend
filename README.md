# PedidiosAqui-BackEnd
PedidosAqui backend
 
## Ejecutar local 
  
Clonar el repositorio 
```bash
  git clone https://github.com/Adrian-Aguilera/PedidosAqui-Backend.git
```

Go to the project directory 

```bash
  cd /PedidosAqui-Backend
```

## Instalacion
 
Para poder instalar el proyecto, crearemos un .venv para instalar las dependencias

```bash
  python3 -m venv .venv
```
```bash
.venv\Scripts\activate
```
una vez instalado y corriendo la terminal del .venv, instalar las dependencias corriendo

```bash
  pip install -r requirements.txt
```

## Informacion Adicional

Crear una aplicacion con django

```bash
  python manage.py startapp {name_app}
```
(Solo al inicializar el proyecto)

 <hr>

 
Crear migraciones del proyecto

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Crear usuario administrador
```bash
  python manage.py createsuperuser
```

<hr>


## Instalacion de los temas para el panel admin de django
luego de hacer las migraciones instalar los temas de para django:

##### [Django](https://www.djangoproject.com/) theme (default): Run 

```bash
python manage.py loaddata admin_interface_theme_django.json
```
##### [Bootstrap](http://getbootstrap.com/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_bootstrap.json
```

##### [Foundation](http://foundation.zurb.com/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_foundation.json
```

##### [U.S. Web Design Standards](https://standards.usa.gov/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_uswds.json
```

<hr>

## Deployment

Ejecutar servidor local

```bash
  python manage.py runserver
```

Ejecutar servidor local  con certificado ssl (recomendado)

```bash
  python manage.py runsslserver
```
