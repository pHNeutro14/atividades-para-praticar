class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def informacoes(self):
        return f"O livro {self.titulo} do autor {self.autor} possui {self.paginas} páginas"

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K Rowling", 323)
livro2 = Livro("A Culpa é das Estrelas", "Jonh Green", 313)

print(livro1.informacoes())
print(livro2.informacoes())

livro1.paginas = 223

print(livro1.informacoes())