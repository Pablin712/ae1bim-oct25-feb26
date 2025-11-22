"""
Poblar la base de datos con información de prueba
"""
from datetime import date
from configuracion import session
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion


def poblar_base_datos():
    """
    Función para ingresar datos a las entidades de la base de datos
    """
    print("Iniciando el poblado de la base de datos...")
    
    # ========== CREAR INSTITUCIONES ==========
    print("\n1. Creando Instituciones...")
    inst1 = Institucion(nombre="Universidad Central del Ecuador", ciudad="Quito", pais="Ecuador")
    inst2 = Institucion(nombre="Escuela Politécnica Nacional", ciudad="Quito", pais="Ecuador")
    inst3 = Institucion(nombre="Universidad de Guayaquil", ciudad="Guayaquil", pais="Ecuador")
    
    session.add_all([inst1, inst2, inst3])
    session.commit()
    print(f"   - {inst1}")
    print(f"   - {inst2}")
    print(f"   - {inst3}")
    
    # ========== CREAR DEPARTAMENTOS ==========
    print("\n2. Creando Departamentos...")
    dept1 = Departamento(nombre="Departamento de Ciencias de la Computación", codigo="DCC-001", institucion_id=inst1.id)
    dept2 = Departamento(nombre="Departamento de Matemáticas", codigo="MAT-002", institucion_id=inst1.id)
    dept3 = Departamento(nombre="Departamento de Ingeniería de Sistemas", codigo="SIS-003", institucion_id=inst2.id)
    dept4 = Departamento(nombre="Departamento de Física", codigo="FIS-004", institucion_id=inst2.id)
    dept5 = Departamento(nombre="Departamento de Biología", codigo="BIO-005", institucion_id=inst3.id)
    
    session.add_all([dept1, dept2, dept3, dept4, dept5])
    session.commit()
    print(f"   - {dept1}")
    print(f"   - {dept2}")
    print(f"   - {dept3}")
    print(f"   - {dept4}")
    print(f"   - {dept5}")
    
    # ========== CREAR INVESTIGADORES ==========
    print("\n3. Creando Investigadores...")
    inv1 = Investigador(nombre="Juan", apellido="Pérez", email="juan.perez@uce.edu.ec", 
                        area_investigacion="Inteligencia Artificial", departamento_id=dept1.id)
    inv2 = Investigador(nombre="María", apellido="González", email="maria.gonzalez@uce.edu.ec", 
                        area_investigacion="Machine Learning", departamento_id=dept1.id)
    inv3 = Investigador(nombre="Carlos", apellido="Ramírez", email="carlos.ramirez@uce.edu.ec", 
                        area_investigacion="Álgebra Lineal", departamento_id=dept2.id)
    inv4 = Investigador(nombre="Ana", apellido="Torres", email="ana.torres@epn.edu.ec", 
                        area_investigacion="Redes de Computadoras", departamento_id=dept3.id)
    inv5 = Investigador(nombre="Luis", apellido="Morales", email="luis.morales@epn.edu.ec", 
                        area_investigacion="Ciberseguridad", departamento_id=dept3.id)
    inv6 = Investigador(nombre="Sofia", apellido="Jiménez", email="sofia.jimenez@epn.edu.ec", 
                        area_investigacion="Física Cuántica", departamento_id=dept4.id)
    inv7 = Investigador(nombre="Pedro", apellido="Vargas", email="pedro.vargas@ug.edu.ec", 
                        area_investigacion="Biotecnología", departamento_id=dept5.id)
    
    session.add_all([inv1, inv2, inv3, inv4, inv5, inv6, inv7])
    session.commit()
    print(f"   - {inv1}")
    print(f"   - {inv2}")
    print(f"   - {inv3}")
    print(f"   - {inv4}")
    print(f"   - {inv5}")
    print(f"   - {inv6}")
    print(f"   - {inv7}")
    
    # ========== CREAR PUBLICACIONES ==========
    print("\n4. Creando Publicaciones...")
    pub1 = Publicacion(titulo="Aplicaciones de Deep Learning en Visión por Computadora", 
                       fecha_publicacion=date(2023, 5, 15), doi="10.1234/ai.2023.001", 
                       tipo_publicacion="Artículo", investigador_id=inv1.id)
    pub2 = Publicacion(titulo="Algoritmos de Clasificación Supervisada", 
                       fecha_publicacion=date(2023, 8, 20), doi="10.1234/ml.2023.002", 
                       tipo_publicacion="Artículo", investigador_id=inv2.id)
    pub3 = Publicacion(titulo="Tesis Doctoral: Redes Neuronales Convolucionales", 
                       fecha_publicacion=date(2024, 1, 10), doi="10.1234/thesis.2024.001", 
                       tipo_publicacion="Tesis", investigador_id=inv2.id)
    pub4 = Publicacion(titulo="Espacios Vectoriales y Transformaciones Lineales", 
                       fecha_publicacion=date(2023, 11, 5), doi="10.1234/math.2023.003", 
                       tipo_publicacion="Artículo", investigador_id=inv3.id)
    pub5 = Publicacion(titulo="Seguridad en Protocolos de Red", 
                       fecha_publicacion=date(2024, 2, 28), doi="10.1234/net.2024.004", 
                       tipo_publicacion="Conferencia", investigador_id=inv4.id)
    pub6 = Publicacion(titulo="Criptografía Post-Cuántica", 
                       fecha_publicacion=date(2024, 3, 15), doi="10.1234/sec.2024.005", 
                       tipo_publicacion="Artículo", investigador_id=inv5.id)
    pub7 = Publicacion(titulo="Entrelazamiento Cuántico en Sistemas Abiertos", 
                       fecha_publicacion=date(2023, 9, 12), doi="10.1234/physics.2023.006", 
                       tipo_publicacion="Artículo", investigador_id=inv6.id)
    pub8 = Publicacion(titulo="Ingeniería Genética en Plantas", 
                       fecha_publicacion=date(2024, 4, 7), doi="10.1234/bio.2024.007", 
                       tipo_publicacion="Conferencia", investigador_id=inv7.id)
    pub9 = Publicacion(titulo="Nuevas Técnicas en Machine Learning", 
                       fecha_publicacion=date(2024, 5, 1), doi="10.1234/ml.2024.008", 
                       tipo_publicacion="Artículo", investigador_id=inv1.id)
    pub10 = Publicacion(titulo="Avances en Ciberseguridad Industrial", 
                        fecha_publicacion=date(2024, 6, 10), doi="10.1234/sec.2024.009", 
                        tipo_publicacion="Tesis", investigador_id=inv5.id)
    
    session.add_all([pub1, pub2, pub3, pub4, pub5, pub6, pub7, pub8, pub9, pub10])
    session.commit()
    print(f"   - {pub1}")
    print(f"   - {pub2}")
    print(f"   - {pub3}")
    print(f"   - {pub4}")
    print(f"   - {pub5}")
    print(f"   - {pub6}")
    print(f"   - {pub7}")
    print(f"   - {pub8}")
    print(f"   - {pub9}")
    print(f"   - {pub10}")
    
    print("\n✅ Base de datos poblada exitosamente!")
    print(f"\nResumen:")
    print(f"  - {session.query(Institucion).count()} Instituciones")
    print(f"  - {session.query(Departamento).count()} Departamentos")
    print(f"  - {session.query(Investigador).count()} Investigadores")
    print(f"  - {session.query(Publicacion).count()} Publicaciones")


if __name__ == "__main__":
    poblar_base_datos()
