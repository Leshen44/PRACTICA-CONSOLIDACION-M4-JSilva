from automovil import Automovil


class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numeros_puesto):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numeros_puesto = numeros_puesto
