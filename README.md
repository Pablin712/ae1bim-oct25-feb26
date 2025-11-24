# Actividad Experimental - ORM con SQLAlchemy

## 📋 Descripción
Sistema de gestión académica educativa utilizando ORM (Object Relational Mapper) con SQLAlchemy en Python y base de datos SQLite.

## 🏗️ Estructura del Proyecto

### Entidades Implementadas:
1. **Institución**: id, nombre, ciudad, país
2. **Departamento**: id, nombre, código, institución_id (FK)
3. **Investigador**: id, nombre, apellido, email, area_investigacion, departamento_id (FK)
4. **Publicación**: id, titulo, fecha_publicacion, doi, tipo_publicacion, investigador_id (FK)

## 📁 Archivos del Proyecto

- `configuracion.py` - Configuración de la conexión a la base de datos SQLite
- `crear_base_entidades.py` - Definición de modelos/entidades usando SQLAlchemy ORM
- `poblar_base.py` - Script para insertar datos de prueba en las tablas
- `consulta_all.py` - Consultas usando el método `.all()`
- `consulta_filter.py` - Consultas usando el método `.filter()`
- `consulta_and.py` - Consultas usando el operador `AND`
- `consulta_or.py` - Consultas usando el operador `OR`
- `consulta_order_by.py` - Consultas usando el método `.order_by()`
- `gestion_academica.db` - Archivo de base de datos SQLite (generado automáticamente)

## 🚀 Instrucciones de Ejecución

### 1. Instalar SQLAlchemy
```bash
pip install sqlalchemy
```

### 2. Crear las tablas de la base de datos
```bash
python crear_base_entidades.py
```
Este comando genera el archivo `gestion_academica.db` con las 4 tablas relacionadas.

### 3. Poblar la base de datos con información
```bash
python poblar_base.py
```
Inserta datos de prueba:
- 5 Instituciones (institutos, colegios, ministerios)
- 6 Departamentos
- 8 Investigadores
- 12 Publicaciones

### 4. Ejecutar consultas

#### Consultas con .all() - Recuperar todos los registros
```bash
python consulta_all.py
```

#### Consultas con .filter() - Aplicar filtros específicos
```bash
python consulta_filter.py
```

#### Consultas con AND - Combinar condiciones
```bash
python consulta_and.py
```

#### Consultas con OR - Condiciones alternativas
```bash
python consulta_or.py
```

#### Consultas con .order_by() - Ordenar resultados
```bash
python consulta_order_by.py
```

## 📊 Ejemplos de Consultas

### Obtener todas las instituciones
```python
session.query(Institucion).all()
```

### Filtrar investigadores por área específica
```python
session.query(Investigador).filter(Investigador.area_investigacion == "Desarrollo de Software").all()
```

### Publicaciones tipo "Artículo" de 2023
```python
session.query(Publicacion).filter(
    and_(
        Publicacion.tipo_publicacion == "Artículo",
        Publicacion.fecha_publicacion >= date(2023, 1, 1),
        Publicacion.fecha_publicacion <= date(2023, 12, 31)
    )
).all()
```

### Ordenar investigadores por apellido
```python
session.query(Investigador).order_by(Investigador.apellido).all()
```

## 🛠️ Tecnologías Utilizadas
- **Python 3.13**
- **SQLAlchemy** - ORM para Python
- **SQLite** - Sistema de base de datos relacional

## ✅ Requisitos Cumplidos
- ✅ Configuración y conexión a base de datos
- ✅ Definición de entidades usando ORM
- ✅ Implementación de relaciones entre entidades (claves foráneas)
- ✅ Poblado de base de datos con información de prueba
- ✅ Consultas: all, filter, and, or, order_by