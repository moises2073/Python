# Creando una lista que se puede modificar
Lista = ["Moises David","Velasquez",True,1.75]
print(Lista[0]) # el "0" Es el numero  para indicar que quiero que me muestre de la lista

#Crando una lista que no se puede modificar con tupla
tupla =("Moises David","Velasquez",True,1.75)
print(tupla)

#Esto es valido y modificable
#Lista[3] = "moto"

#esto no es valido y no se modifica
#tupla[3] = "moto"

# (Se coloca el numeral al codigo para no ser ejecutado)

#print(Lista[3])
 
#creando un conjunto (set)

conjunto  = {"Moises David","Velasquez",True,1.75,"Moises David"} #El conjunto no te deja repetir elementos, ejemplo con "Moises david" cuando lo vas a imprimir solo te muestra 1 y almacena los datos desordenados
print(conjunto)

#Creando un diccionario (dict)
diccionario = {
    'Nombre' : "Moises David",
    'Apellido': "Velasquez",
    'Esta_feliz' : True,
    'Altura' : 1.70,
}

print(diccionario["Altura"] + 2) #Aca podemos llmar algun elemento de la lista por la deficion que se le ha colocado, ejemplo "Altura". El numero "2" es solo para sumarle agun digito si lo desea

