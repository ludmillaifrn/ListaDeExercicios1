from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcularSalario(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal

    def __str__(self):
        return f"Funcionário CLT(Nome: {self.nome}, Salário Mensal: {self.salario_mensal})"

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcularSalario(self):
        return self.valor_hora * self.horas_trabalhadas

    def __str__(self):
        return f"Funcionário Horista(Nome: {self.nome}, Valor por Hora: {self.valor_hora}, Horas Trabalhadas: {self.horas_trabalhadas})"

funcionario_clt = FuncionarioCLT("Ana Silva", 3000.00)
funcionario_horista = FuncionarioHorista("Pedro Oliveira", 25.00, 160)

print(funcionario_clt)
print(f"Salário de {funcionario_clt.nome}: R$ {funcionario_clt.calcularSalario():.2f}")
print(funcionario_horista)
print(f"Salário de {funcionario_horista.nome}: R$ {funcionario_horista.calcularSalario():.2f}")