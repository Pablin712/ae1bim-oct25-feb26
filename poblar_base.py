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
    inst1 = Institucion(nombre="Instituto Tecnológico Superior", ciudad="Cuenca", pais="Ecuador")
    inst2 = Institucion(nombre="Colegio Nacional Mejía", ciudad="Quito", pais="Ecuador")
    inst3 = Institucion(nombre="Ministerio de Educación", ciudad="Quito", pais="Ecuador")
    inst4 = Institucion(nombre="Unidad Educativa Particular San Francisco", ciudad="Guayaquil", pais="Ecuador")
    inst5 = Institucion(nombre="Centro de Investigación Científica CIEC", ciudad="Ambato", pais="Ecuador")
    
    session.add_all([inst1, inst2, inst3, inst4, inst5])
    session.commit()
    print(f"   - {inst1}")
    print(f"   - {inst2}")
    print(f"   - {inst3}")
    print(f"   - {inst4}")
    print(f"   - {inst5}")
    
    # ========== CREAR DEPARTAMENTOS ==========
    print("\n2. Creando Departamentos...")
    dept1 = Departamento(nombre="Departamento de Tecnología e Innovación", codigo="TEC-101", institucion_id=inst1.id)
    dept2 = Departamento(nombre="Departamento de Ciencias Exactas", codigo="CEX-202", institucion_id=inst2.id)
    dept3 = Departamento(nombre="Departamento de Planificación Educativa", codigo="PLE-303", institucion_id=inst3.id)
    dept4 = Departamento(nombre="Departamento de Investigación Aplicada", codigo="INA-404", institucion_id=inst4.id)
    dept5 = Departamento(nombre="Departamento de Desarrollo Científico", codigo="DCI-505", institucion_id=inst5.id)
    dept6 = Departamento(nombre="Departamento de Robótica", codigo="ROB-106", institucion_id=inst1.id)
    
    session.add_all([dept1, dept2, dept3, dept4, dept5, dept6])
    session.commit()
    print(f"   - {dept1}")
    print(f"   - {dept2}")
    print(f"   - {dept3}")
    print(f"   - {dept4}")
    print(f"   - {dept5}")
    print(f"   - {dept6}")
    
    # ========== CREAR INVESTIGADORES ==========
    print("\n3. Creando Investigadores...")
    inv1 = Investigador(nombre="Roberto", apellido="Mendoza", email="roberto.mendoza@its.edu.ec", 
                        area_investigacion="Desarrollo de Software", departamento_id=dept1.id)
    inv2 = Investigador(nombre="Patricia", apellido="Salazar", email="patricia.salazar@cnm.edu.ec", 
                        area_investigacion="Matemática Aplicada", departamento_id=dept2.id)
    inv3 = Investigador(nombre="Diego", apellido="Vásquez", email="diego.vasquez@mineduc.gob.ec", 
                        area_investigacion="Políticas Educativas", departamento_id=dept3.id)
    inv4 = Investigador(nombre="Gabriela", apellido="Castro", email="gabriela.castro@sanfrancisco.edu.ec", 
                        area_investigacion="Pedagogía Digital", departamento_id=dept4.id)
    inv5 = Investigador(nombre="Fernando", apellido="Orellana", email="fernando.orellana@ciec.org.ec", 
                        area_investigacion="Biotecnología Educativa", departamento_id=dept5.id)
    inv6 = Investigador(nombre="Valeria", apellido="Chimbo", email="valeria.chimbo@its.edu.ec", 
                        area_investigacion="Inteligencia Artificial", departamento_id=dept1.id)
    inv7 = Investigador(nombre="Andrés", apellido="Palacios", email="andres.palacios@its.edu.ec", 
                        area_investigacion="Automatización Industrial", departamento_id=dept6.id)
    inv8 = Investigador(nombre="Mónica", apellido="Herrera", email="monica.herrera@ciec.org.ec", 
                        area_investigacion="Neurociencias", departamento_id=dept5.id)
    
    session.add_all([inv1, inv2, inv3, inv4, inv5, inv6, inv7, inv8])
    session.commit()
    print(f"   - {inv1}")
    print(f"   - {inv2}")
    print(f"   - {inv3}")
    print(f"   - {inv4}")
    print(f"   - {inv5}")
    print(f"   - {inv6}")
    print(f"   - {inv7}")
    print(f"   - {inv8}")
    
    # ========== CREAR PUBLICACIONES ==========
    print("\n4. Creando Publicaciones...")
    pub1 = Publicacion(titulo="Metodologías Ágiles en el Desarrollo Educativo", 
                       fecha_publicacion=date(2023, 3, 12), doi="10.5678/dev.2023.001", 
                       tipo_publicacion="Artículo", investigador_id=inv1.id)
    pub2 = Publicacion(titulo="Aplicaciones del Cálculo Diferencial en Física", 
                       fecha_publicacion=date(2023, 7, 8), doi="10.5678/mat.2023.002", 
                       tipo_publicacion="Artículo", investigador_id=inv2.id)
    pub3 = Publicacion(titulo="Reforma Curricular Nacional: Análisis y Perspectivas", 
                       fecha_publicacion=date(2024, 2, 20), doi="10.5678/pol.2024.003", 
                       tipo_publicacion="Conferencia", investigador_id=inv3.id)
    pub4 = Publicacion(titulo="Tesis Doctoral: Gamificación en el Aprendizaje", 
                       fecha_publicacion=date(2024, 1, 15), doi="10.5678/ped.2024.004", 
                       tipo_publicacion="Tesis", investigador_id=inv4.id)
    pub5 = Publicacion(titulo="Innovación en Cultivos mediante Biotecnología", 
                       fecha_publicacion=date(2023, 10, 30), doi="10.5678/bio.2023.005", 
                       tipo_publicacion="Artículo", investigador_id=inv5.id)
    pub6 = Publicacion(titulo="Redes Neuronales Profundas para Clasificación de Imágenes", 
                       fecha_publicacion=date(2024, 4, 18), doi="10.5678/ia.2024.006", 
                       tipo_publicacion="Artículo", investigador_id=inv6.id)
    pub7 = Publicacion(titulo="Sistemas de Control Automatizado en la Industria 4.0", 
                       fecha_publicacion=date(2024, 3, 25), doi="10.5678/aut.2024.007", 
                       tipo_publicacion="Conferencia", investigador_id=inv7.id)
    pub8 = Publicacion(titulo="Plasticidad Cerebral y Aprendizaje", 
                       fecha_publicacion=date(2023, 9, 14), doi="10.5678/neu.2023.008", 
                       tipo_publicacion="Artículo", investigador_id=inv8.id)
    pub9 = Publicacion(titulo="Arquitecturas de Microservicios en Aplicaciones Web", 
                       fecha_publicacion=date(2024, 5, 22), doi="10.5678/dev.2024.009", 
                       tipo_publicacion="Artículo", investigador_id=inv1.id)
    pub10 = Publicacion(titulo="Tesis: Optimización de Algoritmos Genéticos", 
                        fecha_publicacion=date(2024, 6, 5), doi="10.5678/ia.2024.010", 
                        tipo_publicacion="Tesis", investigador_id=inv6.id)
    pub11 = Publicacion(titulo="Evaluación de Competencias en Educación Virtual", 
                        fecha_publicacion=date(2023, 11, 17), doi="10.5678/ped.2023.011", 
                        tipo_publicacion="Conferencia", investigador_id=inv4.id)
    pub12 = Publicacion(titulo="Modelos Matemáticos para Predicción Climatológica", 
                        fecha_publicacion=date(2024, 4, 9), doi="10.5678/mat.2024.012", 
                        tipo_publicacion="Artículo", investigador_id=inv2.id)
    
    session.add_all([pub1, pub2, pub3, pub4, pub5, pub6, pub7, pub8, pub9, pub10, pub11, pub12])
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
    print(f"   - {pub11}")
    print(f"   - {pub12}")
    
    print("\n✅ Base de datos poblada exitosamente!")
    print(f"\nResumen:")
    print(f"  - {session.query(Institucion).count()} Instituciones")
    print(f"  - {session.query(Departamento).count()} Departamentos")
    print(f"  - {session.query(Investigador).count()} Investigadores")
    print(f"  - {session.query(Publicacion).count()} Publicaciones")


if __name__ == "__main__":
    poblar_base_datos()
