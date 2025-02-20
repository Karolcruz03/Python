#ejercicio 1
# --Este curso(1.5h)
# ---Min(2.5h)---CRUDO(3.5h)---Promedio(4h)---CRUDO(5h)---Max(7h)

#A) Diferencia en porcentaje entre el curso actual y 
# -El más rapido de otros cursos
# -El mas lento de otros cursos
# -El promedio de los cursos

#B)Porcentaje de material inservible que se reduce en:
# -El promedio de cursos
# -El curso actual(este curso)

# C) Ver 10 horas de este curso ¿a cuantas horas de otros cursos equivale?
# ¿y al reves?


#Promedio duracion
otros_cursos_min = 2.5 #Horas
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#Diferencias A)
#Restando 100: Obtienes cuánto más lento (negativo) o más rápido (positivo)
# es el curso actual en comparación con el curso más rápido.
diferencia_con_min = 100 - dalto_curso/otros_cursos_min * 100
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido')

#diferencia_con_max = 100 - dalto_curso//otros_cursos_max* 100
diferencia_con_max = 100 - dalto_curso *1000 //otros_cursos_max /10
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el más lento')

diferencia_con_prom = 100 - dalto_curso/otros_cursos_prom * 100
print(f'El curso de Dalto dura un {diferencia_con_prom}% menos que el promedio')
print("------------------------------------")

#Duracion de crudos B)
crudo_promedio = 5
crudo_dalto = 3.5

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_prom *1000 //crudo_promedio /10
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')

tiempo_vacio_dalto = 100 - dalto_curso *1000 //crudo_dalto /10
print(f'Este curso elimino un {tiempo_vacio_dalto}% de tiempo vacio')
print("------------------------------------")

#Mostrando diferencias si los cursos duraran 10 horas C)
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom*100 //dalto_curso/10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso*100 //otros_cursos_prom/10} horas de este curso')
 

