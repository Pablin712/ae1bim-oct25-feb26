"""
Consultas usando OR para buscar registros que cumplan al menos una condición
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from sqlalchemy import or_


def consultar_or():
    print("=" * 80)
    print("CONSULTAS USANDO OR")
    print("=" * 80)
    
    # Consulta 1: Instituciones en Quito O Guayaquil
    print("\n1. Instituciones ubicadas en Quito O Guayaquil:")
    print("-" * 80)
    instituciones = session.query(Institucion).filter(
        or_(Institucion.ciudad == "Quito", Institucion.ciudad == "Guayaquil")
    ).all()
    for inst in instituciones:
        print(f"   {inst.nombre} - {inst.ciudad}")
    
    # Consulta 2: Investigadores del área "Machine Learning" O "Inteligencia Artificial"
    print("\n2. Investigadores de 'Machine Learning' O 'Inteligencia Artificial':")
    print("-" * 80)
    investigadores_ia_ml = session.query(Investigador).filter(
        or_(
            Investigador.area_investigacion == "Machine Learning",
            Investigador.area_investigacion == "Inteligencia Artificial"
        )
    ).all()
    for inv in investigadores_ia_ml:
        print(f"   {inv.nombre} {inv.apellido} - {inv.area_investigacion}")
    
    # Consulta 3: Publicaciones tipo "Tesis" O "Conferencia"
    print("\n3. Publicaciones de tipo 'Tesis' O 'Conferencia':")
    print("-" * 80)
    publicaciones = session.query(Publicacion).filter(
        or_(Publicacion.tipo_publicacion == "Tesis", Publicacion.tipo_publicacion == "Conferencia")
    ).all()
    for pub in publicaciones:
        print(f"   {pub.titulo} - Tipo: {pub.tipo_publicacion}")
    
    # Consulta 4: Investigadores con apellido "González" O "Torres"
    print("\n4. Investigadores con apellido 'González' O 'Torres':")
    print("-" * 80)
    investigadores_apellido = session.query(Investigador).filter(
        or_(Investigador.apellido == "González", Investigador.apellido == "Torres")
    ).all()
    for inv in investigadores_apellido:
        print(f"   {inv.nombre} {inv.apellido} - {inv.area_investigacion}")
    
    # Consulta 5: Departamentos con código "DCC-001" O "SIS-003"
    print("\n5. Departamentos con código 'DCC-001' O 'SIS-003':")
    print("-" * 80)
    departamentos = session.query(Departamento).filter(
        or_(Departamento.codigo == "DCC-001", Departamento.codigo == "SIS-003")
    ).all()
    for dept in departamentos:
        print(f"   {dept.nombre} - Código: {dept.codigo}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_or()
