usuario = input('Ingrese una palabra') # este comentario me sirve para tomar el input del usuario y así empezar a analizarlo usando la función
# print(usuario[::-1]) prueba para probar output del usuario si sale al revés
def detector(x):
    x = usuario
    if usuario == usuario[::-1]:
        return True
    else:
        return False
print(detector(usuario))
