def anagrama_orden(primera, segunda):
    return sorted(primera) == sorted(segunda)

print(anagrama_orden('roma','amor'))

# CONDICIÓN EVALUA A FALSE ENTONCES ASSERT ARROJA UN ASSERTION ERROR
assert True == anagrama_orden('road','camino'), 'Este es un anagrama'
# OUPUT En esta se aplican la función sobre los elementos con resultado False
# True == False >> False entonces assert despliega un error..

assert False == anagrama_orden('roma','amor'), 'Este es un anagrama'
# OUPUT En esta se aplican la función sobre los elementos con resultado True
# False == True >> False entonces assert despliega un error.


# CONDICIÓN EVALUA A TRUE ENTONCES ASSERT NO HACE NADA
assert True == anagrama_orden('roma','amor')
# OUPUT En esta se aplican la función sobre los elementos con resultado True
# True == True >> True entonces assert no hace nada.

assert False == anagrama_orden('road','camino')
# OUPUT En esta se aplican la función sobre los elementos con resultado False
# False == False >> True entonces assert no hace nada.