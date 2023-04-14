
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 =  [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 =  [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

lis_nombres = nombres.replace("\n","").replace("\'","").replace(" ","").split(',')

#Genero un diccionario donde las contraseñas son los nombres de los alumnos que contienen sus notas dos en una tupla.
def generarEstructura ():
    notas = zip(notas_1,notas_2) 
    return dict(zip(lis_nombres,notas))

#Calculo el promedio para cada estudiante y lo guardo en un diccionario nuevo donde nuevamente las contradeñas son los nombres y el valor es el promedio de sus dos notas.
def promedioPorEstudiante(Notas):
    resultado = map(lambda key: (Notas[key][0]+ Notas[key][1])/len(Notas[key]),Notas)
    return dict(zip(lis_nombres,resultado))

#Usando el diccionario creado en promedioPorEstudiante sumo todos los valor y luego saco su promedio.
def promedioGeneral(Promedios):
    suma = sum(Promedios.values())
    return suma / len(Promedios)

#Usando nuevamente el diccionario creado en promedioPorEstudiante busco el nombre de la persona que tiene un mayor promeio.
def mayorPromedio(Promedios):
    nombreMax = max(Promedios, key=Promedios.get)
    return (nombreMax, Promedios[nombreMax]) #Devuelvo una tupla que contiene el nombre y la nota promedio mas alta del estudiante.

#Con la estructura generada en generarEstructura busco el nombre del estudiante que obtuvo menor nota.
def notaMinima(Notas):
    nombreMin = min(Notas, key = lambda x: min(Notas[x]))
    return (nombreMin,min(Notas[nombreMin]))#Vuelvo hacer un minimo pero de nombremin asi retorna el nombre que obtuvo menor nota con su nota correspondiente, porque cada estudiante contenia una tupla de sus dos notas.

#Guardo funciones en una variable porque algunas las utilizo mas de una vez y para no llamarlas cada vez que las necesite las pongo en una variable.
combinado = generarEstructura() 
promPorEstu = promedioPorEstudiante(combinado)
promedioGene = promedioGeneral(promPorEstu)
mayorProm = mayorPromedio(promPorEstu)
notaMin = notaMinima(combinado)

#Imprimo todo lo retornado;
print("-"*60)
print("CADA NOMBRE ASOCIADO A SUS DOS NOTAS")
print (combinado)
print("-"*60)
print("PROMEDIO ENTRE SUS NOTAS POR CADA ESTUDIANTE");
print(promPorEstu)
print("-"*60)
print(f"El promedio de las notas de todo el curso es [{promedioGene}]")
print("-"*60)
print(f"La nota y el alumno/a que obtuvo mayor promedio entre sus notas es: {mayorProm[0]} con el promedio {mayorProm[1]}.")
print("-"*60)
print(f"El alumno/a {notaMin[0]} obtuvo la nota minima que fue {notaMin[1]}.")