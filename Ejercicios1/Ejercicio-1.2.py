
frase = input ("dime una frase y te calculo cuanto atrdes en decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo  ')
print(f'Dalto lo diria en {cantidad_de_palabras  * 10 //2 /1.3 // 10 } segundos ')