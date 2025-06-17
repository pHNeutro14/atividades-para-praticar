import livro

livro1 = livro.Livro("Harry Potter e a Pedra Filosofal", "J.K Rowling", 323)
livro2 = livro.Livro("A Culpa é das Estrelas", "Jonh Green", 313)

print(livro1.informacoes())
print(livro2.informacoes())

livro1.paginas = 223

print(livro1.informacoes())