#las listas se pueden modificar
lista = ["Karol Cruz", "Junior dev", True, 1.75, "Junior dev"]
print(lista)
print(lista[0])

#No se puede modificar los elementos
tupla = ("Karol Cruz", "Junior dev", True, 1.75, "Junior dev") 
#tupla[3] = "Karolyne" #No es valido
print(tupla)
print(tupla[0])

#Para ser conjuntos (set)
#Tampoco se pueden modificar los elementos, y no se muestran datos repetidos, ni se puede acceder por indice conjunto[0]
conjunto = {"Karol Cruz", "Junior dev", True, 1.75, "Junior dev"} 
#Se puede redefinir la variable
conjunto = {"Hola mundo", "Hola mundo"}
tupla = ("Holii")
print(conjunto)
#print(conjunto[3]) -> no se puede acceder

#Diccionario (dict) /json en js a ={key: value, key:value}
diccionario = {
    'nombre' : "Karol Cruz",
    'profesion' : "Junior dev",
    'feliz?' : True,
    'altura' : 1.75,
    'dato_duplicado': "Junior dev"
}
print(diccionario['nombre'])
