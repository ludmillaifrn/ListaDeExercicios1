from Q1 import Funcionario

novoFuncionario = Funcionario("Luis", "12345678910", 25.50)
print(f"Nome: {novoFuncionario.nome}")
print(f"CPF: {novoFuncionario.cpf}")
print(f"Valor por hora: R$ {novoFuncionario.valorPorHora:.2f}")

novoFuncionario.incrementarHoras(8)
print(f"Horas trabalhadas: {novoFuncionario.horasTrabalhadas}")

novoFuncionario.incrementarHoras(4)
print(f"\nNome: {novoFuncionario.nome}")
print(f"Horas trabalhadas: {novoFuncionario.horasTrabalhadas}")

salario = novoFuncionario.calcularSalario()
print(f"\nSalário de {novoFuncionario.nome}: R$ {salario:.2f}")