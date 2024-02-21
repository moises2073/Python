#and
#or
#not

#ejemplos
#AND (Si Aguno es falso es resultado sera falso, solo devuelve verdadero si 2 mismos resultados pegan)
Resultado = True & True #Devolver true
Resultado2 = False & True #Devolver falso
Resultado3 = True & False #Devuelve Falso
Resultado4 = False & False #Devuelve Falso

#OR(Solo devuelve falso cuanda ambas son falsas) con que alguna de cumple devuelve verdadero, si las 2 no se cumplen devuelve falso
Resultado5 = True | True #Devolver true
Resultado6 = False | True #Devolver true
Resultado7 = True | False #Devuelve true
Resultado8 = False | False #Devuelve Falso

#NOT (Si le pasas treu te devuelve false y lo contrario, es de negación)
Resultado9 = not True #Devolver Falso    
Resultado10 = not False #Devolver true


print(Resultado10)