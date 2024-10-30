from dataclasses import dataclass


@dataclass
class Vehiculo:
    marca: str
    modelo: str
    numero_ruedas: int


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Particular(Automovil):
    def __init__(
        self, marca, modelo, numero_ruedas, velocidad, cilindrada, numeros_puesto
    ):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numeros_puesto = numeros_puesto


class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
