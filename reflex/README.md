# PRIMER CV ONLINE CON REFLEX

# Informacion para inatalar Reflex

# Primero creamos nuestro entorno Virtual en Windows.
  * python.exe -m venv venv   

# Primero creamos nuestro entorno Virtual en MAC/LINUX.
  * python312 -m venv venv   

# Activamos nuestro entorno Virtual en Windows.
  * ./venv/Scripts/activate

# Activamos nuestro entorno Virtual en MAC/LINUS.
  * source venv/bin/activate

# Install reflex using pip con en venv Activado.
  * pip install pip --upgrade    //aqui actializamos nuestro pip
  * pip install reflex

# Creamos la carpeta de nuestro Proyecto.
  md my_project
  cd my_project
  reflex init  //inicializamos nuestro proyecto Reflex
  luego seleccionamos la opcion 0 => Blank page opcion 0
 

* Import the reflex library to get started.

  import reflex as rx  //dentro de nuestra aplicacion reflex debemos importar libreria de relfex como rx siempre

# Ejecutamos nuestra aplicacion.
  reflex run   // automaticamente ejecutara con puerto 3000
