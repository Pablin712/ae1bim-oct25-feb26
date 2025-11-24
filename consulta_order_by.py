"""
Consultas usando el método .order_by() para ordenar los resultados según criterios específicos
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def consultar_order_by():
    """
    Ejemplos de consultas usando .order_by() para ordenar datos
    """
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 18 + "CONSULTAS CON ORDENAMIENTO (.order_by())" + " " * 20 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Consulta 1: Instituciones ordenadas por nombre (ascendente)
    print("\n⇅ Ordenamiento #1: Instituciones alfabéticamente (A→Z)")
    print("─" * 80)
    instituciones = session.query(Institucion).order_by(Institucion.nombre).all()
    for inst in instituciones:
        print(f"   ⋙ {inst.nombre} | {inst.ciudad}")
    
    # Consulta 2: Investigadores ordenados por apellido (ascendente)
    print("\n⇅ Ordenamiento #2: Investigadores por apellido (A→Z)")
    print("─" * 80)
    investigadores = session.query(Investigador).order_by(Investigador.apellido).all()
    for inv in investigadores:
        print(f"   ⋙ {inv.apellido}, {inv.nombre} ({inv.area_investigacion})")
    
    # Consulta 3: Publicaciones ordenadas por fecha (más recientes primero)
    print("\n⇅ Ordenamiento #3: Publicaciones cronológicamente (Reciente→Antigua)")
    print("─" * 80)
    publicaciones = session.query(Publicacion).order_by(Publicacion.fecha_publicacion.desc()).all()
    for pub in publicaciones:
        print(f"   ⋙ [{pub.fecha_publicacion}] {pub.titulo}")
    
    # Consulta 4: Departamentos ordenados por código
    print("\n⇅ Ordenamiento #4: Departamentos por código identificador")
    print("─" * 80)
    departamentos = session.query(Departamento).order_by(Departamento.codigo).all()
    for dept in departamentos:
        print(f"   ⋙ [{dept.codigo}] {dept.nombre}")
    
    # Consulta 5: Investigadores ordenados por área de investigación y luego por nombre
    print("\n⇅ Ordenamiento #5: Investigadores por área, después por nombre")
    print("─" * 80)
    investigadores_area = session.query(Investigador).order_by(
        Investigador.area_investigacion, Investigador.nombre
    ).all()
    for inv in investigadores_area:
        print(f"   ⋙ [{inv.area_investigacion}] {inv.nombre} {inv.apellido}")
    
    # Consulta 6: Publicaciones ordenadas por tipo y luego por fecha (descendente)
    print("\n⇅ Ordenamiento #6: Publicaciones por categoría, luego fecha descendente")
    print("─" * 80)
    pub_ordenadas = session.query(Publicacion).order_by(
        Publicacion.tipo_publicacion, Publicacion.fecha_publicacion.desc()
    ).all()
    for pub in pub_ordenadas:
        print(f"   ⋙ [{pub.tipo_publicacion}] {pub.titulo} - {pub.fecha_publicacion}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_order_by()
