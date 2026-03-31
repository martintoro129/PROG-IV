# PRIMER LOGIN

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
  * Instalar Requerimientos.txt ya que alli estan los modulos iniciales a usar

# Creamos la carpeta de nuestro Proyecto.
  md applogin
  cd applogin
  1. Inicialización (Solo la primera vez)
Antes de usar cualquier funcionalidad de base de datos en una aplicación nueva, debes inicializar el entorno de migraciones.

Bash.
* reflex db init

Qué hace: Configura Alembic en tu proyecto y crea un script de migración inicial basado en tus modelos actuales. 
reflex.dev

2. Generar una migración (Cada vez que cambies el modelo)
Cada vez que añadas, elimines o modifiques una clase rx.Model en tu código, debes generar un script que describa esos cambios.

Bash.
* reflex db makemigrations --message "descripción del cambio"

Qué hace: Compara tus modelos de Python con el estado actual de la base de datos y crea un archivo en la carpeta alembic/versions.
Nota importante: Tus modelos deben estar importados en tu aplicación para que este comando los detecte. 
reflex.dev

3. Aplicar la migración
Una vez generado el script, debes ejecutarlo para que los cambios se reflejen realmente en la base de datos (por ejemplo, en el archivo reflex.db o tu DB externa). 
bash
* reflex db migrate
  
* Import the reflex library to get started.

  import reflex as rx  //dentro de nuestra aplicacion reflex debemos importar libreria de relfex como rx siempre

# Ejecutamos nuestra aplicacion.
  reflex run   // automaticamente ejecutara con puerto 3000
