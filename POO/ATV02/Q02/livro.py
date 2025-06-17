class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def informacoes(self):
        return f"O livro {self.titulo} do autor {self.autor} possui {self.paginas} páginas"

