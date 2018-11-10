# motor
class motor:
    def __init__(self,potencia,cilindro_motor):
        self.potencia = potencia
        self.cilindro_motor = cilindro_motor

class llanta:
    def __init__(self,tamnno,color_llanta):
        self.tamanno = tamnno
        self.color_llanta = color_llanta

class asientos:
    def __init__(self,material_asiento,color_asiento):
        self.material_assiento = material_asiento
        self.color_asiento = color_asiento

class carros(motor,asientos,llanta):
    def __init__(self,potencia,cilindro_motor,tamnno,color_llanta,material_asiento,color_asiento):
        self.el_motor =  motor (potencia,cilindro_motor)
        self.la_llanta = llanta(tamnno, color_llanta)
        self.el_asiento = asientos(material_asiento, color_asiento)

mi_carro = carro(potencia = 100, cilindro_motor = 4,
                 tamanno = 17, color_llanta = 'negro',
                 material_asiento = 'cuero',
                 color_asiento = 'negro')

pass

