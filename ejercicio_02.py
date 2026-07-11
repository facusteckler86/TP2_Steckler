
#Clase Base Bicicleta

class Bicicleta:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.__precio = precio

    def obtener_precio(self):
        return self.__precio
    
    def describir(self):
        print(f"Modelo: {self.modelo}")


# Clas Hija Bicielectrica
class BicicletaElectrica(Bicicleta):
    def __init__(self, modelo, precio, bateria):
        super().__init__(modelo, precio)
        self.bateria = bateria

mi_bici = BicicletaElectrica("Venzo X250", 750.000, "500Wh")
print(f"Precio: {mi_bici.obtener_precio()}")
mi_bici.describir()



