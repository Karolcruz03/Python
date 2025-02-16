ingreso_mensual: 81000
gasto_mensual = 80000

#if anidado y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Tus gastos estan bien")
    else:
        print("Estas gastando más de lo que te ingresa económicamente")

elif ingreso_mensual > 1000: #else if pero en python se escribe elif
    print("Estas bien económicamente en Latinoamerica")

elif ingreso_mensual > 500: 
    print("Estas bien económicamente en Argentina")

elif ingreso_mensual > 200:
    print("Estas bien económicamente en Venezuela")

else:
    print("Eres pobre :c ")