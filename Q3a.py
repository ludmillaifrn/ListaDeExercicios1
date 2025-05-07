class Motor:
    def __init__(self, numero_serie, cavalos, torque):
        self.numero_serie = numero_serie
        self.cavalos = cavalos
        self.torque = torque

    def __str__(self):
        return f"Motor(Número de Série: {self.numero_serie}, Cavalos: {self.cavalos}, Torque: {self.torque})"

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  

    def __str__(self):
        return f"Carro(Marca: {self.marca}, Modelo: {self.modelo}, Motor: {self.motor})"

motor1 = Motor("ABC12345", 150, 20.5)
carro1 = Carro("Volkswagen", "Gol", motor1)

print(carro1)