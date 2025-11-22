"""
Consultas usando .filter() para filtrar registros por condiciones específicas
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def consultar_filter():
    """
    Ejemplos de consultas usando .filter() para filtrar datos
    """
    print("=" * 80)
    print("CONSULTAS USANDO .filter()")
    print("=" * 80)
    
    # Consulta 1: Instituciones de Ecuador
    print("\n1. Instituciones ubicadas en Ecuador:")
    print("-" * 80)
    instituciones_ecuador = session.query(Institucion).filter(Institucion.pais == "Ecuador").all()
    for inst in instituciones_ecuador:
        print(f"   {inst.nombre} - {inst.ciudad}")
    
    # Consulta 2: Investigadores del área de Inteligencia Artificial
    print("\n2. Investigadores del área de Inteligencia Artificial:")
    print("-" * 80)
    investigadores_ia = session.query(Investigador).filter(
        Investigador.area_investigacion == "Inteligencia Artificial"
    ).all()
    for inv in investigadores_ia:
        print(f"   {inv.nombre} {inv.apellido} - {inv.email}")
    
    # Consulta 3: Publicaciones de tipo "Artículo"
    print("\n3. Publicaciones de tipo 'Artículo':")
    print("-" * 80)
    articulos = session.query(Publicacion).filter(Publicacion.tipo_publicacion == "Artículo").all()
    for pub in articulos:
        print(f"   {pub.titulo} - {pub.fecha_publicacion}")
    
    # Consulta 4: Instituciones de la ciudad de Quito
    print("\n4. Instituciones ubicadas en Quito:")
    print("-" * 80)
    instituciones_quito = session.query(Institucion).filter(Institucion.ciudad == "Quito").all()
    for inst in instituciones_quito:
        print(f"   {inst.nombre}")
    
    # Consulta 5: Departamentos con código específico
    print("\n5. Departamento con código 'DCC-001':")
    print("-" * 80)
    dept = session.query(Departamento).filter(Departamento.codigo == "DCC-001").first()
    if dept:
        print(f"   {dept.nombre} - Código: {dept.codigo}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_filter()
