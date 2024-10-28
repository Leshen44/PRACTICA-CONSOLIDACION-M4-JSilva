from bicicleta import Bicicleta


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
