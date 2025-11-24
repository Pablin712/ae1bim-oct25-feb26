"""
Consultas usando el método .filter() para aplicar condiciones de filtrado específicas
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def consultar_filter():
    """
    Ejemplos de consultas usando .filter() para filtrar datos
    """
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 19 + "CONSULTAS CON FILTROS (.filter())" + " " * 26 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Consulta 1: Instituciones de la ciudad de Cuenca
    print("\n➤ Filtro 1: Instituciones en la ciudad de Cuenca")
    print("─" * 80)
    instituciones_cuenca = session.query(Institucion).filter(Institucion.ciudad == "Cuenca").all()
    for inst in instituciones_cuenca:
        print(f"   ✓ {inst.nombre} [{inst.ciudad}]")
    
    # Consulta 2: Investigadores del área de Desarrollo de Software
    print("\n➤ Filtro 2: Investigadores especializados en Desarrollo de Software")
    print("─" * 80)
    investigadores_dev = session.query(Investigador).filter(
        Investigador.area_investigacion == "Desarrollo de Software"
    ).all()
    for inv in investigadores_dev:
        print(f"   ✓ {inv.apellido}, {inv.nombre} | Contacto: {inv.email}")
    
    # Consulta 3: Publicaciones de tipo "Conferencia"
    print("\n➤ Filtro 3: Publicaciones categorizadas como 'Conferencia'")
    print("─" * 80)
    conferencias = session.query(Publicacion).filter(Publicacion.tipo_publicacion == "Conferencia").all()
    for pub in conferencias:
        print(f"   ✓ {pub.titulo} (Publicado: {pub.fecha_publicacion})")
    
    # Consulta 4: Instituciones de la ciudad de Ambato
    print("\n➤ Filtro 4: Instituciones establecidas en Ambato")
    print("─" * 80)
    instituciones_ambato = session.query(Institucion).filter(Institucion.ciudad == "Ambato").all()
    for inst in instituciones_ambato:
        print(f"   ✓ {inst.nombre}")
    
    # Consulta 5: Departamentos con código específico
    print("\n➤ Filtro 5: Departamento con identificador 'TEC-101'")
    print("─" * 80)
    dept = session.query(Departamento).filter(Departamento.codigo == "TEC-101").first()
    if dept:
        print(f"   ✓ {dept.nombre} [Código: {dept.codigo}]")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_filter()
