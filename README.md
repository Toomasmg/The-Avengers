# The-Avengers  
**--------modelo parcial--------**

## Integrantes:
- Gomez Mateo  
- Muñoz Tomas

## Participación:
**Back**  
Principal: Gomez Mateo  
Secundario: Muñoz Tomas

---

**Front**  
Principal: Muñoz Tomas  
Secundario: Gomez Mateo

## Desarrollo:

Este proyecto fue realizado como parte de un modelo parcial. El objetivo fue desarrollar una aplicación web sencilla usando **Flask** y **MySQL**, para gestionar los registros de miembros de los Avengers.

### ¿Qué hicimos?
- Armamos la estructura del proyecto desde cero
- Creamos un modelo llamado `Avenger` con los siguientes datos: nombre, alias, habilidades y actor
- Usamos UUID para generar los IDs automáticamente.
- Configuramos la conexión a la base de datos desde un archivo `.env`.
- Creamos rutas para agregar, listar, editar y eliminar avengers.
- Todo el backend se probó primero y después hicimos las vistas en HTML.
- El diseño fue muy simple, usando formularios para cargar los datos.

### Tecnologías:
- Python 3
- Flask
- MySQL
- SQLAlchemy
- HTML (Jinja templates)


### Estructura:
- `models/`: contiene el modelo `Avenger`.
- `routes/`: tiene las rutas para manejar las vistas y lógica del sistema.
- `templates/`: contiene los archivos HTML para el frontend.
- `config.py`, `database.py`, `app.py`: archivos principales del sistema.




