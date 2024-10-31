from dataclasses import dataclass
import csv
from typing import List


@dataclass
class Vehiculo:
    _marca: str
    _modelo: str
    _numero_ruedas: int

    def __init__(self, marca, modelo, numero_ruedas):
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def numero_ruedas(self):
        return self._numero_ruedas

    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas):
        self._numero_ruedas = numero_ruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a", newline='') as file:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(file)
                archivo_csv.writerows(datos)
                print("Datos guardados en archivo csv")
        except Exception as e:
            print("Error al guardar datos en archivo csv", e)

    def leer_datos_csv(self):
        # datos = []
        particulares=[]
        cargas=[]
        bicicletas=[]
        motocicletas=[]
        try:
            with open("vehiculos.csv", "r") as file:
                archivo_csv = csv.reader(file)
                for row in archivo_csv:
                    # if row[0] == str(self.__class__):
                    #     datos.append(row[1])
                    #     print("Datos leidos del archivo csv")
                    # else:
                    #     print("No hay datos")
                    if row[0]=="<class 'vehiculo.Particular'>":
                        particulares.append(row[1])
                    elif row[0]=="<class 'vehiculo.Carga'>":
                        cargas.append(row[1])
                    elif row[0]=="<class 'vehiculo.Bicicleta'>":
                        bicicletas.append(row[1])
                    elif row[0]=="<class 'vehiculo.Motocicleta'>":
                        motocicletas.append(row[1])
                    else:
                        print("No hay datos")
                print("\nLista de Vehiculos Particular")
                for i in particulares:
                    print(i)
                print("\nLista de Vehiculos de Carga")
                for i in cargas:
                    print(i)
                print("\nLista de Vehiculos Bicicleta")
                for i in bicicletas:
                    print(i)
                print("\nLista de Vehiculos Motocicleta")
                for i in motocicletas:
                    print(i)

        except Exception as e:
            print("Error al leer datos del archivo csv", e)
        # return datos


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc"

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def cilindrada(self):
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada


class Particular(Automovil):
    def __init__(
        self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos
    ):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._numero_puestos = numero_puestos

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.numero_puestos}"

    @property
    def numero_puestos(self):
        return self._numero_puestos

    @numero_puestos.setter
    def numero_puestos(self, numero_puestos):
        self._numero_puestos = numero_puestos


class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._peso_carga = peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc,  Carga:{self.peso_carga} kg"

    @property
    def peso_carga(self):
        return self._peso_carga

    @peso_carga.setter
    def peso_carga(self, peso_carga):
        self._peso_carga = peso_carga


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self._tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}"

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self._motor = motor
        self._cuadro = cuadro
        self._nro_radios = nro_radios

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro radios: {self.nro_radios}"

    @property
    def nro_radios(self):
        return self._nro_radios

    @nro_radios.setter
    def nro_radios(self, nro_radios):
        self._nro_radios = nro_radios

    @property
    def cuadro(self):
        return self._cuadro

    @cuadro.setter
    def cuadro(self, cuadro):
        self._cuadro = cuadro

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor
