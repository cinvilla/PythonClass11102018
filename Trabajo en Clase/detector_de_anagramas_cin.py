# CÓDIGO ERRÓNEO DEBIDO A QUE SI SE EVALUABA EL # DE
# CARACTERES SE CAÍA EN EL RIESGO DE QUE PALABRAS CON
# DIFERENTES LETRAS DIERAN TRUE SOLO POR EL # DE LETRAS....
# def anag_dect(pal1,pal2):
#     if len(pal1) == len(pal2):
#         return True
#     else:
#         return False
#
# a = 'car'
# b = 'arc'
# print(anag_dect(a,b))
#
# a = 'ana'
# b = 'een'
# print()
# print(anag_dect(a,b))

# EVALUACIÓN HECHA POR LE PROFESOR utilizando sorted para ordenar las palabras y
# presentarlas en igualdad
def anagrama_orden(primera, segunda):
    return sorted(primera) == sorted(segunda)

print(anagrama_orden('roma','amor'))
assert False == anagrama_orden('roma','amor'), 'Este es un anagrama'









