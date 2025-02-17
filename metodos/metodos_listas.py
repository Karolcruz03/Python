# LIST - crea una lista
lista = list(["hola", "Karol", 100])
lista2 = list([334,35,23,True, 65,2030])

# LEN - cuenta la cantidad de elementos de una lista
resultado = len(lista)
print(resultado)


# APPEND - agrega un elemento a la lista
agregar_append = lista.append("JAJAJAJA")
print(lista)

# INSERT - agrega un elemento a la lista en el índice especificado
lista.insert(2, "TOMAAA")
print(lista)

# EXTEND - agrega varios elementos a la lista
lista.extend([False,2030])
print(lista)

# POP - elimina un elemento de una lista, pide índice y devuelve valor
lista.pop(0)
lista.pop(-1) #Eliminar el ultimo, -2 para eliminar el penultimo, etc
print(lista)

# REMOVE - remueve un elemento de una lista, pide valor
lista.remove("TOMAAA")
print(lista)

# CLEAR - elimina todos los elementos de una lista
#lista.clear()
print(lista)


# SORT - ordena una lista de forma ascendente a descendente
lista2.sort() #Ascendente
print(lista2)
lista2.sort(reverse=True) #En reversa
print(lista2)

# REVERSE - invierte los elementos de una lista
lista2.reverse()
print(lista2)