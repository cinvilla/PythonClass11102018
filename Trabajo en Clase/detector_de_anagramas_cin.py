def anag_dect(pal1,pal2):
    if len(pal1) == len(pal2):
        return True
    else:
        return False

a = 'car'
b = 'arc'
print(anag_dect(a,b))

a = 'ana'
b = 'een'
print()
print(anag_dect(a,b))
