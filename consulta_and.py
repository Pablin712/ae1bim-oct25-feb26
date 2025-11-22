"""
Consultas usando AND para combinar múltiples condiciones
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from sqlalchemy import and_
from datetime import date


def consultar_and():
    print("=" * 80)
    print("CONSULTAS USANDO AND")
    print("=" * 80)
    
    # Consulta 1: Instituciones en Ecuador Y en Quito
    print("\n1. Instituciones en Ecuador Y en Quito:")
    print("-" * 80)
    instituciones = session.query(Institucion).filter(
        and_(Institucion.pais == "Ecuador", Institucion.ciudad == "Quito")
    ).all()
    for inst in instituciones:
        print(f"   {inst.nombre} - {inst.ciudad}, {inst.pais}")
    
    # Consulta 2: Investigadores con apellido "Pérez" Y área "Inteligencia Artificial"
    print("\n2. Investigadores con apellido 'Pérez' Y área 'Inteligencia Artificial':")
    print("-" * 80)
    investigadores = session.query(Investigador).filter(
        and_(Investigador.apellido == "Pérez", Investigador.area_investigacion == "Inteligencia Artificial")
    ).all()
    for inv in investigadores:
        print(f"   {inv.nombre} {inv.apellido} - {inv.area_investigacion}")
    
    # Consulta 3: Publicaciones tipo "Artículo" Y publicadas en 2023
    print("\n3. Publicaciones tipo 'Artículo' Y publicadas en 2023:")
    print("-" * 80)
    publicaciones = session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.fecha_publicacion >= date(2023, 1, 1),
            Publicacion.fecha_publicacion <= date(2023, 12, 31)
        )
    ).all()
    for pub in publicaciones:
        print(f"   {pub.titulo} - {pub.fecha_publicacion}")
    
    # Consulta 4: Investigadores del área "Ciberseguridad" Y con email de epn.edu.ec
    print("\n4. Investigadores de 'Ciberseguridad' Y con email @epn.edu.ec:")
    print("-" * 80)
    investigadores_ciber = session.query(Investigador).filter(
        and_(
            Investigador.area_investigacion == "Ciberseguridad",
            Investigador.email.like("%@epn.edu.ec")
        )
    ).all()
    for inv in investigadores_ciber:
        print(f"   {inv.nombre} {inv.apellido} - {inv.email}")
    
    # Consulta 5: Publicaciones tipo "Tesis" Y de 2024
    print("\n5. Publicaciones tipo 'Tesis' Y publicadas en 2024:")
    print("-" * 80)
    tesis_2024 = session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Tesis",
            Publicacion.fecha_publicacion >= date(2024, 1, 1),
            Publicacion.fecha_publicacion <= date(2024, 12, 31)
        )
    ).all()
    for pub in tesis_2024:
        print(f"   {pub.titulo} - {pub.fecha_publicacion}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_and()
