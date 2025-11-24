"""
Definición de las entidades del sistema de gestión académica educativa
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from configuracion import Base, engine


class Institucion(Base):
    """
    Entidad Institución
    Atributos: id, nombre, ciudad, país
    """
    __tablename__ = 'instituciones'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)
    
    # Relación: Una institución tiene muchos departamentos
    departamentos = relationship("Departamento", back_populates="institucion")
    
    def __repr__(self):
        return f"<Institucion(id={self.id}, nombre='{self.nombre}', ciudad='{self.ciudad}', pais='{self.pais}')>"


class Departamento(Base):
    """
    Entidad Departamento
    Atributos: id, nombre, código
    Relación: Un departamento pertenece a una institución (clave foránea)
    """
    __tablename__ = 'departamentos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    institucion_id = Column(Integer, ForeignKey('instituciones.id'), nullable=False)
    
    # Relaciones
    institucion = relationship("Institucion", back_populates="departamentos")
    investigadores = relationship("Investigador", back_populates="departamento")
    
    def __repr__(self):
        return f"<Departamento(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}')>"


class Investigador(Base):
    """
    Entidad Investigador
    Atributos: id, nombre, apellido, email, area_investigacion
    Relación: Un investigador pertenece a un departamento (clave foránea)
    """
    __tablename__ = 'investigadores'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    area_investigacion = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'), nullable=False)
    
    # Relaciones
    departamento = relationship("Departamento", back_populates="investigadores")
    publicaciones = relationship("Publicacion", back_populates="investigador")
    
    def __repr__(self):
        return f"<Investigador(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')>"


class Publicacion(Base):
    """
    Entidad Publicación
    Atributos: id, titulo, fecha_publicacion, doi, tipo_publicacion
    Relación: Una publicación pertenece a un investigador (clave foránea)
    """
    __tablename__ = 'publicaciones'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)  # Formato 'YYYY-MM-DD'
    doi = Column(String(100), nullable=False, unique=True)
    tipo_publicacion = Column(String(50), nullable=False)  # "Artículo", "Tesis", "Conferencia"
    investigador_id = Column(Integer, ForeignKey('investigadores.id'), nullable=False)
    
    # Relación
    investigador = relationship("Investigador", back_populates="publicaciones")
    
    def __repr__(self):
        return f"<Publicacion(id={self.id}, titulo='{self.titulo}', tipo='{self.tipo_publicacion}')>"


# Crear todas las tablas en la base de datos
if __name__ == "__main__":
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(engine)
    print("¡Tablas creadas exitosamente!")
