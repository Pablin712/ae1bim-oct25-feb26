"""
Consultas usando el operador AND para combinar varias condiciones simultáneamente
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from sqlalchemy import and_
from datetime import date


def consultar_and():
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 15 + "CONSULTAS CON OPERADOR AND (Condiciones Múltiples)" + " " * 13 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Consulta 1: Instituciones en Ecuador Y en Cuenca
    print("\n▸ Condición AND #1: País Ecuador AND Ciudad Cuenca")
    print("─" * 80)
    instituciones = session.query(Institucion).filter(
        and_(Institucion.pais == "Ecuador", Institucion.ciudad == "Cuenca")
    ).all()
    for inst in instituciones:
        print(f"   ◉ {inst.nombre} | Ubicación: {inst.ciudad}, {inst.pais}")
    
    # Consulta 2: Investigadores con apellido "Mendoza" Y área "Desarrollo de Software"
    print("\n▸ Condición AND #2: Apellido Mendoza AND Área Desarrollo de Software")
    print("─" * 80)
    investigadores = session.query(Investigador).filter(
        and_(Investigador.apellido == "Mendoza", Investigador.area_investigacion == "Desarrollo de Software")
    ).all()
    for inv in investigadores:
        print(f"   ◉ {inv.apellido}, {inv.nombre} | Especialización: {inv.area_investigacion}")
    
    # Consulta 3: Publicaciones tipo "Conferencia" Y publicadas en 2024
    print("\n▸ Condición AND #3: Tipo Conferencia AND Año 2024")
    print("─" * 80)
    publicaciones = session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Conferencia",
            Publicacion.fecha_publicacion >= date(2024, 1, 1),
            Publicacion.fecha_publicacion <= date(2024, 12, 31)
        )
    ).all()
    for pub in publicaciones:
        print(f"   ◉ {pub.titulo} | Fecha: {pub.fecha_publicacion}")
    
    # Consulta 4: Investigadores del área "Matemática Aplicada" Y con email de cnm.edu.ec
    print("\n▸ Condición AND #4: Área Matemática Aplicada AND Dominio @cnm.edu.ec")
    print("─" * 80)
    investigadores_mat = session.query(Investigador).filter(
        and_(
            Investigador.area_investigacion == "Matemática Aplicada",
            Investigador.email.like("%@cnm.edu.ec")
        )
    ).all()
    for inv in investigadores_mat:
        print(f"   ◉ {inv.apellido}, {inv.nombre} | Email: {inv.email}")
    
    # Consulta 5: Publicaciones tipo "Artículo" Y de 2024
    print("\n▸ Condición AND #5: Tipo Artículo AND Año 2024")
    print("─" * 80)
    articulos_2024 = session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.fecha_publicacion >= date(2024, 1, 1),
            Publicacion.fecha_publicacion <= date(2024, 12, 31)
        )
    ).all()
    for pub in articulos_2024:
        print(f"   ◉ {pub.titulo} | Publicado: {pub.fecha_publicacion}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_and()
