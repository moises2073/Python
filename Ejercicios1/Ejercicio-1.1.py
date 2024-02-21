
#Promedio de duracion

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
Dalto_curso = 1.5

#Duración de crudo
crudo_Promedio = 5
crudo_dalto = 3.5

#Difierencia de duración

diferecia_con_min = 100 - Dalto_curso / otros_cursos_min * 100
diferecia_con_max = 100 - Dalto_curso *1000 // otros_cursos_max / 10
diferecia_con_promedio = 100 - Dalto_curso / otros_cursos_promedio * 100

#Calcular el procentaje de tiempo vacio removido
tiempo_vacio_Promedio =100 - otros_cursos_promedio * 1000 // crudo_Promedio / 10
tiempo_vacio_dalto =100 - Dalto_curso * 1000 // crudo_dalto/ 10


#Encontrando las diferencias de duración (Ejercicio A)
print(f'el curso de dalto dura un {diferecia_con_min}% menos que es más rapido')
print(f'el curso de dalto dura un {diferecia_con_max}% menos que es más lento')
print(f'el curso de dalto dura un {diferecia_con_promedio}% menos que que el promedio')
print("*********************************************************************")

#Mostrar cantidad de espacios vacios que se remueven (Ejercicio B)
print(f' Un curso promedio elimina un {tiempo_vacio_Promedio}% de tiempo vacio')
print(f' Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print("*********************************************************************")

#Mostrando diferencia si los cursos duraran 10 horas

print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // Dalto_curso / 10} horas de otros cursos ')
print(f'Ver 10 horas de este curso equivale a ver { Dalto_curso * 100 // otros_cursos_promedio / 10 } horas de otros cursos ')
