from rich import print
class Vehiculo:
    #Atributo de clase
    #Atributos de instancia
    def __init__(self,marca:str,modelo:int,color:str,ruedas):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas
    def prender(self,encendido:str):
        return f"el {self.marca} esta {encendido}"
    def apagar(self,apagado:str):
        return f"el {self.marca} esta {apagado}"
    def avanzar(self,avanzar:str):
        return f"el {self.marca} puede {avanzar}"
    def retroceder(self,retroceder:str):
        return f"el {self.marca} esta {retroceder}"
class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: int, color: str, ruedas:str,rpm:int):
        super().__init__(marca, modelo, color, ruedas)
        self.rpm=rpm
    def nitro(self):
        return "Corre como un flash"
class Omnibus(Vehiculo):
    def __init__(self, marca: str, modelo: int, color: str, ruedas:str,num_asientos:int):
        super().__init__(marca, modelo, color, ruedas)
        self.num_asientos=num_asientos
    def pasajeros(self):
        return "Lleva muchos pasajeros"
Lambo=Auto("Lamborghini","Huracan","Negro","Perille","8.400")
Palomino=Omnibus("Hyundai","9800","Azul","Lanvigator","40")
