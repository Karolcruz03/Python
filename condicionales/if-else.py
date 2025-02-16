edad = 17

if edad >= 18:
    print("Puedes pasar")

else:
    print("No puedes pasar")
    
print("no forma parte de ninguna condicion")

contraseña_almacenada = "KarolDev"
contraseña_escrita = '''KarolDev''' #True
contraseña_incorrecta = '''Karoldev''' #False


if contraseña_almacenada == contraseña_escrita:
    print("Iniciando sesion...")

else:
    print("Contraseña incorrecta, intente nuevamente")