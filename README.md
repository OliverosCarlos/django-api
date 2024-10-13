
# API Django

API basica desarrollada con Django


## Requisitos

- python 3.12.3
- postgresql


## Configuración

Instalar librarías de python
```bash
  python -m pip install requirements.txt
```
Migrar base de datos
```bash
  python manage.py migrate
```
Run servidor
```bash
  python manage.py runserver
```
## API Reference



#### API Autores

| Metodo | Ruta     | Descripción                |
| :-------- | :------- | :------------------------- |
| GET | `GET localhost:8000/autor` | Obtener todos los autores |
| GET | `GET localhost:8000/autor/${id}` | Obtener un autor por id |
| POST | `POST localhost:8000/autor` | Crear autor |
| PUT | `PUT localhost:8000/autor/${id}` | Actualizar un autor por id |
| DELETE | `DELETE localhost:8000/autor/${id}` | Eliminar un autor por id |


#### API Libros

| Metodo | Ruta     | Descripción                |
| :-------- | :------- | :------------------------- |
| GET | `GET localhost:8000/libro` | Obtener todos los libros |
| GET | `GET localhost:8000/libro/${id}` | Obtener un libro por id |
| POST | `POST localhost:8000/libro` | Crear un libro |
| PUT | `PUT localhost:8000/libro/${id}` | Actualizar un libro por id |
| DELETE | `DELETE localhost:8000/libro/${id}` | Eliminar un libro por id |
