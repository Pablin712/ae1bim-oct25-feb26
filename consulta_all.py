"""
Consultas usando .all() para obtener todos los registros
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def consultar_all():
    """
    Ejemplos de consultas usando .all() para obtener todos los registros
    """
    print("=" * 80)
    print("CONSULTAS USANDO .all()")
    print("=" * 80)
    
    # Consulta 1: Obtener todas las instituciones
    print("\n1. Todas las Instituciones:")
    print("-" * 80)
    instituciones = session.query(Institucion).all()
    for inst in instituciones:
        print(f"   ID: {inst.id} | {inst.nombre} | {inst.ciudad}, {inst.pais} | Núm Departamentos: {len(inst.departamentos)}")
    
    # Consulta 2: Obtener todos los departamentos
    print("\n2. Todos los Departamentos:")
    print("-" * 80)
    departamentos = session.query(Departamento).all()
    for dept in departamentos:
        print(f"   ID: {dept.id} | Código: {dept.codigo} | {dept.nombre} | Institución: {dept.institucion.nombre}")
    
    # Consulta 3: Obtener todos los investigadores
    print("\n3. Todos los Investigadores:")
    print("-" * 80)
    investigadores = session.query(Investigador).all()
    for inv in investigadores:
        print(f"   ID: {inv.id} | {inv.nombre} {inv.apellido} | Área: {inv.area_investigacion} | {inv.departamento.nombre}")
    
    # Consulta 4: Obtener todas las publicaciones
    print("\n4. Todas las Publicaciones:")
    print("-" * 80)
    publicaciones = session.query(Publicacion).all()
    for pub in publicaciones:
        print(f"   ID: {pub.id} | {pub.titulo} | Tipo: {pub.tipo_publicacion} | Fecha: {pub.fecha_publicacion} | Investigador: {pub.investigador.nombre} {pub.investigador.apellido}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_all()
