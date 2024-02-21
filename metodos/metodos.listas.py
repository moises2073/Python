# Creando una lista con list
lista = list(["Hola", "David", "23"])


# Devuelve la cantidad de elementos de una lista
cantidad_Elementos = len(lista)

# Agregando un elemento a las lista
lista.append("jajajaja")

# agregando un elemento a la lista en un indice especifico 

lista.insert(2, "Moises")


# Agregando varios elementos a la lista

lista.extend([False,2030])

# Elimando elementos de la lista por un indice

lista.pop(0) #elimino el indice 0 que es "Hola"

# si queremos eliminar el ultimo elemento de la lista hacemos el siguiente ejemplo

lista.pop(-1) # Elimina el indice -1 que es "2030" siendo el ultimo (Nota: si quieres eliminar de atras hacia adelante, tienes que contar desde -1 que seria el untimo indice de la lista y si continuas seria -2,-3,-4...)


# Remover un un elemento de la lista por su valor

lista.remove("Moises")# ejemplo, en .insert agregue a la lista "Moises" y con remove lo elimine con el valor que seria "Moises"

# "lista.sort" Ordenando la lista de forma ascendente, Ejemplo ( si tenemos una lista de [30,20,50] con el metodo .srot nos acomoda la lista asi [20,30,50]) no funciona con cadena de texto, ejmplo "Moises, DAvid"  | Si usamos el parametro reverse=true lo oderna de forma reversa , es decir .sort(reverse=true) lo haria así [50,30,20]

# Invirtiendo los elementos de una lista

lista.reverse()

#Verificando si un elemento se ecuentra en la lista 

Elemento_encontrado = lista.index("23")


lista.clear() # eliminar todo los elementos de la lista


print(lista)

