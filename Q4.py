class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Empresa:
    def __init__(self, nome, funcionario):
        self.nome = nome
        self.funcionario = funcionario

p1 = Pessoa("Ana")
e1 = Empresa("TechCorp", p1) 
# Correção: Passando o objeto Pessoa 'p1' como funcionário