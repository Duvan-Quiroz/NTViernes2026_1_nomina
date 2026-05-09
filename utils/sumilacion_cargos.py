import random

def generar_cargos(numeroCargos):

    listaNombres = [
        "Instructor",
        "Coordinador Académico",
        "Auxiliar Administrativo",
        "Analista de Sistemas",
        "Asesor Comercial",
        "Director de Programa",
        "Soporte Técnico"
    ]

    listaDescripciones = [
        "Encargado de dictar clases y formar estudiantes",
        "Coordina programas académicos y docentes",
        "Apoya procesos administrativos y atención",
        "Gestiona sistemas de información de la empresa",
        "Asesora a estudiantes sobre programas educativos",
        "Dirige y supervisa programas académicos",
        "Brinda soporte técnico a equipos y usuarios"
    ]

    cargos = []

    for i in range(numeroCargos):

        cargo = {
            "id": random.randint(0, 5000),
            "nombre": random.choice(listaNombres),
            "descripcion": random.choice(listaDescripciones)
        }
        
        probabilidad_error = random.random()

        if probabilidad_error < 0.1:
            cargo["id"] = ["id"] = random.choice([-1, -24, 0])
        elif probabilidad_error < 0.2:
            cargo["nombre"] = " " + cargo["nombre"].lower()
        elif probabilidad_error < 0.3:
            cargo["descripcion"] = " " + cargo["descripcion"] + " "
        

        cargos.append(cargo)

    return cargos