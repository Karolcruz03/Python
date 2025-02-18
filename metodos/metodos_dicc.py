diccionario = {
    "nombre" : "karol",
    "apellido" : "Klein",
    "numero" : 10000,
    "grado" : "Centigrados"
}

#keys() devuelve las claves, tmb sirve para iterar
claves = diccionario.keys()
print(claves)

#get() devuelve el valor de una clave, no lanza excepciones
claves = diccionario.get("apellido")
print(claves)

#clear() elimina todos los elementos
#diccionario.clear()

#pop() elimina un elemento
diccionario.pop("numero", "grado")

#items() para iterar el dict
diccionario_iterar = diccionario.items()
print(diccionario_iterar)