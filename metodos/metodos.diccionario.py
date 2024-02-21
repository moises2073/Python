diccionario = {
    "nombre" : 'Lucas',
    "aplellido" : 'dalto',
    "suns"  : 1000000
      
}

#
claves =diccionario.keys() # Resultado es "dict_keys(['nombre', 'aplellido', 'suns'])"

# Busca algo en el diccionario, busca un propiedad particular de algun objeto 

claves =diccionario.get("nombre")

#Eliminando todo del diccionario
#diccionario.clear


#elimina un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict:items iterable 
diccionario_iterable = diccionario.items()


print(diccionario_iterable)