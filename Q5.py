class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = [] 

    def adicionar_turma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
            turma.adicionar_aluno(self) 
    def remover_turma(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)
            turma.remover_aluno(self) 
    def listar_turmas(self):
        print(f"O aluno {self.nome} pertence às seguintes turmas:")
        for turma in self.turmas:
            print(f"- {turma.nome}")

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = [] 

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.adicionar_turma(self) 
    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.remover_turma(self) 

    def listar_alunos(self):
        print(f"A turma {self.nome} possui os seguintes alunos:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")

aluno1 = Aluno("Carlos")
aluno2 = Aluno("Mariana")
aluno3 = Aluno("Pedro")

turmaA = Turma("Matemática")
turmaB = Turma("Português")

turmaA.adicionar_aluno(aluno1)
turmaA.adicionar_aluno(aluno2)
turmaB.adicionar_aluno(aluno2)
turmaB.adicionar_aluno(aluno3)

turmaA.listar_alunos()
print("-" * 20)
turmaB.listar_alunos()
print("-" * 20)

aluno1.listar_turmas()
print("-" * 20)
aluno2.listar_turmas()
print("-" * 20)
aluno3.listar_turmas()