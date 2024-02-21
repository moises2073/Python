cadena1 = "hola, soy, Moises"
cadena2 = "mañana es otro día"

 #el .upper() convierte todo a mayuscula
 
mayuscula = cadena1.upper() 

# y el .lower() convierte todo a minuscula

minuscula = cadena1.lower()

#Primera letra a Mayuscula

primer_letra_mayuscula = cadena1.capitalize()


#Buscar una cadena en otra cadena, si no hay resultado te devuelve -1
busqueda_find = cadena1.find("M")#colocar lo que quieres que busque en la cadena dentro de los ("")
 
 
 #Buscar una cadena en otra cadena con index
 
busqueda_index = cadena2.index("m")


#si es numerico, devolvemos true, sino devolvemos false

es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true, sino devolvemos false

es_alfanumerico = cadena1.isalpha()



#Buscar una cadena en otra cadena, devuelve la catidad de veces que coincida en la cadena
contar_coincidencias = cadena1.count("a")

 
 
 #contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
 
 
 #verificamos si una cadena empiza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("hola")#validar cadena1 : así empiza cadena 1



#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("Moises") #validar cadena1: termina en cadena 1
 
 
#remplaza un pedazo de la cadena dada por otra cadena
cadena_nueva = cadena1.replace("Moises","David")#Se coloca primero lo que se quiere remplazar y lusgo que le pondras 
 
 
#separar cadenas con cadenas con cadenas que pasemos
cadena_separada = cadena1.split(",")
 
#los [2] es para buscar el valor en la cadena
 
print(cadena_separada[2])