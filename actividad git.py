import numpy as np

num_candidatos = 30
num_votantes = 5000
votos = np.random.randint(1, num_candidatos + 1, num_votantes)
conteo_votos = np.bincount(votos)[1:]  
candidatos = np.arange(1, num_candidatos + 1)
resultado = np.column_stack((candidatos, conteo_votos))
resultado_ordenado = resultado[resultado[:, 1].argsort()[::-1]]
print("Listado de candidatos y sus votos (de mayor a menor):")
for candidato, votos in resultado_ordenado:
    print(f"Candidato {int(candidato)}: {int(votos)} votos")

num_estudiantes = 6500

np.random.seed(0)  
codigos = np.arange(1, num_estudiantes + 1)
nombres = [f"Estudiante {i}" for i in codigos]
promedios = np.random.uniform(2.0, 5.0, num_estudiantes)  
anios_ingreso = np.random.randint(1980, 2023, num_estudiantes)  
codigos_carrera = np.random.randint(1, 5, num_estudiantes)  

dtype = [('codigo', int), ('nombre', 'U20'), ('promedio', float), ('anio_ingreso', int), ('codigo_carrera', int)]
estudiantes = np.zeros(num_estudiantes, dtype=dtype)


estudiantes['codigo'] = codigos
estudiantes['nombre'] = nombres
estudiantes['promedio'] = promedios
estudiantes['anio_ingreso'] = anios_ingreso
estudiantes['codigo_carrera'] = codigos_carrera


codigo_carrera_x = int(input("Ingrese el código de la carrera a listar: "))
estudiantes_carrera_x = estudiantes[(estudiantes['codigo_carrera'] == codigo_carrera_x) & (estudiantes['promedio'] >= 4)]

print(f"\nEstudiantes de la carrera {codigo_carrera_x} con promedio >= 4:")
for estudiante in estudiantes_carrera_x:
    print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")
print(f"Total de estudiantes: {len(estudiantes_carrera_x)}")


estudiantes_condicionales = estudiantes[(estudiantes['anio_ingreso'] < 1990) & (estudiantes['promedio'] < 3.0)]

print("\nEstudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in estudiantes_condicionales:
    print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")