cadena1 = "Hola soy Karol"
cadena2 = "Bienvenido"
cadena3 = "Hola,soy,Karol"

#DIR- devuelve la lista de atributos validos del objeto pasado
resultado = dir(cadena1) #funcion
#####################################


#UPPER - convierte a mayúscula
resultado2 = cadena1.upper #metodo

#LOWER - convierte a minúscula
resultado3 = cadena1.lower()

#CAPITALIZE - primera en mayúscula
capital = cadena1.capitalize()
#####################################


#FIND - método encuentra la primera aparición del valor especificado, sino devuelve -1
busqueda = cadena1.find("Hola")

#INDEX - método encuentra la primera aparición del valor especificado, sino devuelve una excepción
busqueda2 = cadena1.index("H")
#####################################


#ISNUMERIC - si es numérico devuelve true
busqueda3 = cadena1.isnumeric()

#ISALPHA - si es alfanumérico devuelve true
busq4 = cadena1.isalpha()
#####################################


#COUNT - devuelve el número de ocurrencias de una subcadena en la cadena dada.
contar = cadena1.count("a")
 
#LEN - cuenta los caracteres de una cadena
cuenta = len(cadena2)
#####################################


#STARTSWITH - verifica si una cadena comienza con
empieza = cadena1.startswith("H")

#ENDSWITH - verifica si una cadena termina con
termina = cadena2.endswith("S")
#####################################


# REPLACE - remplaza un valor por otro
reemplaza = cadena1.replace("la","li")

# SPLIT - separa por el parámetro dado
separar = cadena3.split(",")
print(separar[0])

print(resultado)