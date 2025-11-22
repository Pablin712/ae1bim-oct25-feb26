# Actividad Experimental - ORM con SQLAlchemy

## 📋 Descripción
Sistema de gestión de investigación académica utilizando ORM (Object Relational Mapper) con SQLAlchemy en Python y base de datos SQLite.

## 🏗️ Estructura del Proyecto

### Entidades Implementadas:
1. **Institución**: id, nombre, ciudad, país
2. **Departamento**: id, nombre, código, institución_id (FK)
3. **Investigador**: id, nombre, apellido, email, area_investigacion, departamento_id (FK)
4. **Publicación**: id, titulo, fecha_publicacion, doi, tipo_publicacion, investigador_id (FK)

## 📁 Archivos del Proyecto

- `configuracion.py` - Configuración de la base de datos SQLite
- `crear_base_entidades.py` - Definición de entidades/modelos con SQLAlchemy
- `poblar_base.py` - Script para poblar la base de datos con datos de prueba
- `consulta_all.py` - Consultas usando `.all()`
- `consulta_filter.py` - Consultas usando `.filter()`
- `consulta_and.py` - Consultas usando operador `AND`
- `consulta_or.py` - Consultas usando operador `OR`
- `consulta_order_by.py` - Consultas usando `.order_by()`
- `investigacion.db` - Base de datos SQLite (se crea al ejecutar los scripts)

## 🚀 Instrucciones de Ejecución

### 1. Instalar SQLAlchemy
```bash
pip install sqlalchemy
```

### 2. Crear las tablas de la base de datos
```bash
python crear_base_entidades.py
```
Este comando crea el archivo `investigacion.db` con las 4 tablas.

### 3. Poblar la base de datos con información
```bash
python poblar_base.py
```
Inserta datos de prueba:
- 3 Instituciones
- 5 Departamentos
- 7 Investigadores
- 10 Publicaciones

### 4. Ejecutar consultas

#### Consultas con .all() - Obtener todos los registros
```bash
python consulta_all.py
```

#### Consultas con .filter() - Filtrar por condiciones
```bash
python consulta_filter.py
```

#### Consultas con AND - Combinar múltiples condiciones
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

### Todas las instituciones
```python
session.query(Institucion).all()
```

### Investigadores de un área específica
```python
session.query(Investigador).filter(Investigador.area_investigacion == "Inteligencia Artificial").all()
```

### Publicaciones tipo "Artículo" en 2023
```python
session.query(Publicacion).filter(
    and_(
        Publicacion.tipo_publicacion == "Artículo",
        Publicacion.fecha_publicacion >= date(2023, 1, 1),
        Publicacion.fecha_publicacion <= date(2023, 12, 31)
    )
).all()
```

### Investigadores ordenados por apellido
```python
session.query(Investigador).order_by(Investigador.apellido).all()
```

## 🛠️ Tecnologías Utilizadas
- **Python 3.13**
- **SQLAlchemy** - ORM
- **SQLite** - Base de datos

## ✅ Requisitos Cumplidos
- ✅ Configuración de base de datos
- ✅ Definición de entidades con ORM
- ✅ Relaciones entre entidades (claves foráneas)
- ✅ Poblado de base de datos
- ✅ Consultas: all, filter, and, or, order_by