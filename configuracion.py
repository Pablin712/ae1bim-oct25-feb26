from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración del motor de base de datos SQLite
engine = create_engine('sqlite:///gestion_academica.db', echo=True)

# Crear la clase base para las entidades
Base = declarative_base()

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()
