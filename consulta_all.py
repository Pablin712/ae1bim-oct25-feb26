"""
Consultas usando el método .all() para recuperar todos los registros de las tablas
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def consultar_all():
    """
    Ejemplos de consultas usando .all() para obtener todos los registros
    """
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "CONSULTAS CON MÉTODO .all()" + " " * 31 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Consulta 1: Obtener todas las instituciones
    print("\n>>> Listado completo de Instituciones registradas:")
    print("─" * 80)
    instituciones = session.query(Institucion).all()
    for inst in instituciones:
        print(f"   [{inst.id}] {inst.nombre} ({inst.ciudad}, {inst.pais})")
    
    # Consulta 2: Obtener todos los departamentos
    print("\n>>> Listado completo de Departamentos activos:")
    print("─" * 80)
    departamentos = session.query(Departamento).all()
    for dept in departamentos:
        print(f"   [{dept.codigo}] {dept.nombre}")
    
    # Consulta 3: Obtener todos los investigadores
    print("\n>>> Registro total de Investigadores:")
    print("─" * 80)
    investigadores = session.query(Investigador).all()
    for inv in investigadores:
        print(f"   • {inv.apellido}, {inv.nombre} - Especialidad: {inv.area_investigacion}")
    
    # Consulta 4: Obtener todas las publicaciones
    print("\n>>> Catálogo completo de Publicaciones:")
    print("─" * 80)
    publicaciones = session.query(Publicacion).all()
    for pub in publicaciones:
        print(f"   ◆ '{pub.titulo}' [{pub.tipo_publicacion}] - {pub.fecha_publicacion}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_all()
