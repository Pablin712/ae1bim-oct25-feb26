"""
Configuración de la base de datos SQLite usando SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear el motor de la base de datos SQLite
# El archivo se llamará 'investigacion.db' y se creará en el directorio actual
engine = create_engine('sqlite:///investigacion.db', echo=True)

# Crear la clase base para las entidades
Base = declarative_base()

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()
