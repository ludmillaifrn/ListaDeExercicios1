class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, codigo, cargo):
        super().__init__(nome, cpf)
        self.codigo = codigo
        self.cargo = cargo

    def __str__(self):
        return f"Funcionário(Nome: {self.nome}, CPF: {self.cpf}, Código: {self.codigo}, Cargo: {self.cargo})"

class Autor(Pessoa):
    def __init__(self, nome, cpf, codigo):
        super().__init__(nome, cpf)
        self.codigo = codigo
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        livro.adicionarAutor(self)

    def __str__(self):
        return f"Autor(Nome: {self.nome}, CPF: {self.cpf}, Código: {self.codigo})"

class Livro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.autores = []

    def adicionarAutor(self, autor):
        self.autores.append(autor)

    def __str__(self):
        return f"Livro(Título: {self.titulo}, ISBN: {self.isbn})"

class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.funcionarios = []
        self.livros = []

    def adicionarFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return f"Biblioteca(Nome: {self.nome}, Endereço: {self.endereco}, Número de Funcionários: {len(self.funcionarios)}, Número de Livros: {len(self.livros)})"


biblioteca1 = Biblioteca("Biblioteca Central", "Rua Principal, 123")

funcionario1 = Funcionario("Carlos Silva", "123.456.789-00", 101, "Bibliotecário")
biblioteca1.adicionarFuncionario(funcionario1)

autor1 = Autor("Machado de Assis", "987.654.321-00", 201)
livro1 = Livro("Dom Casmurro", "978-85-03-01058-2")
autor1.adicionarLivro(livro1)
biblioteca1.adicionarLivro(livro1)

autor2 = Autor("Clarice Lispector", "111.222.333-44", 202)
livro2 = Livro("A Hora da Estrela", "978-85-346-0443-0")
autor2.adicionarLivro(livro2)
biblioteca1.adicionarLivro(livro2)

print(biblioteca1)
print(funcionario1)
print(autor1)
print(livro1)
print(autor2)
print(livro2)

print(f"\nLivros de {autor1.nome}: {[livro.titulo for livro in autor1.livros]}")
print(f"Autores de {livro1.titulo}: {[autor.nome for autor in livro1.autores]}")