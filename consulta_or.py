"""
Consultas usando el operador OR para buscar registros que cumplan al menos una de varias condiciones
"""
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from sqlalchemy import or_


def consultar_or():
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 14 + "CONSULTAS CON OPERADOR OR (Condiciones Alternativas)" + " " * 12 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Consulta 1: Instituciones en Cuenca O Ambato
    print("\n◆ Alternativa OR #1: Ciudad Cuenca OR Ciudad Ambato")
    print("─" * 80)
    instituciones = session.query(Institucion).filter(
        or_(Institucion.ciudad == "Cuenca", Institucion.ciudad == "Ambato")
    ).all()
    for inst in instituciones:
        print(f"   ► {inst.nombre} | Ciudad: {inst.ciudad}")
    
    # Consulta 2: Investigadores del área "Inteligencia Artificial" O "Neurociencias"
    print("\n◆ Alternativa OR #2: Área Inteligencia Artificial OR Neurociencias")
    print("─" * 80)
    investigadores_ia_neu = session.query(Investigador).filter(
        or_(
            Investigador.area_investigacion == "Inteligencia Artificial",
            Investigador.area_investigacion == "Neurociencias"
        )
    ).all()
    for inv in investigadores_ia_neu:
        print(f"   ► {inv.apellido}, {inv.nombre} | Campo: {inv.area_investigacion}")
    
    # Consulta 3: Publicaciones tipo "Artículo" O "Tesis"
    print("\n◆ Alternativa OR #3: Tipo Artículo OR Tipo Tesis")
    print("─" * 80)
    publicaciones = session.query(Publicacion).filter(
        or_(Publicacion.tipo_publicacion == "Artículo", Publicacion.tipo_publicacion == "Tesis")
    ).all()
    for pub in publicaciones:
        print(f"   ► {pub.titulo} | Categoría: {pub.tipo_publicacion}")
    
    # Consulta 4: Investigadores con apellido "Salazar" O "Castro"
    print("\n◆ Alternativa OR #4: Apellido Salazar OR Apellido Castro")
    print("─" * 80)
    investigadores_apellido = session.query(Investigador).filter(
        or_(Investigador.apellido == "Salazar", Investigador.apellido == "Castro")
    ).all()
    for inv in investigadores_apellido:
        print(f"   ► {inv.apellido}, {inv.nombre} | Especialidad: {inv.area_investigacion}")
    
    # Consulta 5: Departamentos con código "TEC-101" O "ROB-106"
    print("\n◆ Alternativa OR #5: Código TEC-101 OR Código ROB-106")
    print("─" * 80)
    departamentos = session.query(Departamento).filter(
        or_(Departamento.codigo == "TEC-101", Departamento.codigo == "ROB-106")
    ).all()
    for dept in departamentos:
        print(f"   ► {dept.nombre} | ID: {dept.codigo}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    consultar_or()
