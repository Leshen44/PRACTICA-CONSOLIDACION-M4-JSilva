from vehiculo import Vehiculo
from automovil import Automovil
from carga import Carga
from particular import Particular
from bicicleta import Bicicleta
from motocicleta import Motocicleta


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

print(particular)

print(isinstance(motocicleta,Vehiculo))