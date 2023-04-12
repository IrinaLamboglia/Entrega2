
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

def opcionA ():
    lis_nombres = nombres.replace("\n"," ").split(',')
    return list(zip(lis_nombres,notas_1,notas_2))

def opcionB(lista):
    resultado = map(lambda x: (x[1] + x[2])/2,lista)
    return list(resultado)

def opcionC(lista):
    suma = list(map(lambda x: x[1] + x[2],lista))
    #suma =  sum([sum(nota[1:]) for nota in lista]) / (len(lista)*2)
    return (sum(suma) / (len(lista)*2))

def opcionD(lista):
    notaMax = max(lista , key = lambda x: (x[1] + x[2] / 2))
    return notaMax[0]

def opcionE(lista):
    notaMin = min(lista, key = lambda x: (x[1] + x[2])/2)
    return  notaMin[0]


combinado = opcionA()
print (combinado)
print(opcionB(combinado))
print(opcionC(combinado))
print(opcionD(combinado))
print(opcionE(combinado))
