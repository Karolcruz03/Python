a = 1
b = 2
c= a+b
print(c)

nombre= "Karol" #1
nombre = "Andrea" #2
print(nombre)

numero = 10
numero += 10
numero -= 5
print(numero)

nombre = "Pepito"
bienvenida = "Hola " + nombre+ " ¿Como estas?"
print(bienvenida)

nombre = 5 #"Pepito"
bienvenida = f"Hola  {nombre} ¿Como estas?" #fStrings
#del nombrar ###para borrar datos en memoria
print(bienvenida)

#Logicos
nombre = "Pedro" #True #5 #"Pepito"
bienvenida = f"Hola  {nombre} ¿Como estas?"
print("Pedro" not in bienvenida)#False
print("Pedro" in bienvenida) #True

#Definiendo variables con camelCase (comun en js)
nombreCompletoDelUsuario = "Pedro Perez"

#Definiendo variables con snake_case (recomendado por python)
nombre_completo_del_usuario = "Pedro Perez"

#concantenar con +
bienvenida = "Hola"  + "¿Como estas?"

#concantenar con  f-strings
bienvenida = f"Hola  {nombre_completo_del_usuario} ¿Como estas?"

#operadores de pertenencia
print("Pedro" not in bienvenida)#False
print("Pedro" in bienvenida) #True