from vehiculo import Vehiculo
from vehiculo import Automovil
from vehiculo import Carga
from vehiculo import Particular
from vehiculo import Bicicleta
from vehiculo import Motocicleta

# PARTE 1
print("---INICIO PARTE 1---")
# cantidad_ing = int(input("Cuantos Vehiculos desea insertar: "))
# vehiculos = []
# for i in range(cantidad_ing):
#     print(f"Datos del automóvil {i+1}")
#     marca = input("Inserte la marca del automóvil: ")
#     modelo = input("Inserte el modelo del automóvil: ")
#     numero_ruedas = int(input("Inserte el número de ruedas: "))
#     velocidad = float(input("Inserte la velocidad en km/h:"))
#     cilindrada = int(input("Inserte el cilindraje en cc: "))
#     auto = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
#     vehiculos.append(auto)
# print("Imprimiendo por pantalla los Vehiculos")
# for i in vehiculos:
#     print(i)

print("---INICIO PARTE 2---")
# PARTE 2
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print(
    "Motocicleta es instacion con relación a Vehiculo: ",
    isinstance(motocicleta, Vehiculo),
)
print(
    "Motocicleta es instacion con relación a Automovil: ",
    isinstance(motocicleta, Automovil),
)
print(
    "Motocicleta es instacion con relación a Vehiculo particular: ",
    isinstance(motocicleta, Particular),
)
print(
    "Motocicleta es instacion con relación a Vehiculo de carga: ",
    isinstance(motocicleta, Carga),
)
print(
    "Motocicleta es instacion con relación a Bicicleta: ",
    isinstance(motocicleta, Bicicleta),
)
print(
    "Motocicleta es instacion con relación a Motocicleta: ",
    isinstance(motocicleta, Motocicleta),
)

particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

particular.leer_datos_csv()