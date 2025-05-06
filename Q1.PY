class Funcionario:
    def __init__(self, nomeFuncionario, cpfFuncionario, valorPorHoraFuncionario):
        self.nome = nomeFuncionario
        self.cpf = cpfFuncionario
        self.horasTrabalhadas = 0
        self.valorPorHora = valorPorHoraFuncionario

    def calcularSalario(self):
        return self.horasTrabalhadas * self.valorPorHora

    def incrementarHoras(self, horas):
        self.horasTrabalhadas += horas