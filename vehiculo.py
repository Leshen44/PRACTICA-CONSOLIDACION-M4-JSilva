from dataclasses import dataclass


@dataclass
class Vehiculo:
    marca: str
    modelo: str
    numero_ruedas: int

    @property
    def marca(self):
        return self.marca

    @marca.setter
    def marca(self, marca):
        self.marca = marca

    @property
    def modelo(self):
        return self.modelo

    @modelo.setter
    def modelo(self, modelo):
        self.modelo = modelo

    @property
    def numero_ruedas(self):
        return self.numero_ruedas

    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas):
        self.numero_ruedas = numero_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    @property
    def velocidad(self):
        return self.velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.velocidad = velocidad

    @property
    def cilindrada(self):
        return self.cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.cilindrada = cilindrada


class Particular(Automovil):
    def __init__(
        self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos
    ):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos

    @property
    def numero_puestos(self):
        return self.numero_puestos

    @numero_puestos.setter
    def numero_puestos(self, numero_puestos):
        self.numero_puestos = numero_puestos


class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    @property
    def peso_carga(self):
        return self.peso_carga

    @peso_carga.setter
    def peso_carga(self, peso_carga):
        self.peso_carga = peso_carga


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    @property
    def nro_radios(self):
        return self.nro_radios

    @nro_radios.setter
    def nro_radios(self, nro_radios):
        self.nro_radios = nro_radios

    @property
    def cuadro(self):
        return self.cuadro

    @cuadro.setter
    def cuadro(self, cuadro):
        self.cuadro = cuadro

    @property
    def motor(self):
        return self.motor

    @motor.setter
    def motor(self, motor):
        self.motor = motor
