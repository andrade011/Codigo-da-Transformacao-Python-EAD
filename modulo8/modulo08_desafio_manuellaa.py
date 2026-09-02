# ==============================================================================
#  Desafio Extra: Sistema de Biblioteca
# ==============================================================================

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"📖 Livro '{livro.titulo}' adicionado com sucesso.")

    def listar_livros(self):
        print(f"\n--- Acervo da {self.nome} ---")
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"✅ Empréstimo do livro '{livro.titulo}' realizado!")
                    return
                else:
                    print(f"⚠️ O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"❌ Livro '{titulo}' não foi encontrado.")


# Teste do Desafio Extra
if __name__ == "__main__":
    minha_biblioteca = Biblioteca("Biblioteca Comunitária")
    
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")

    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)

    minha_biblioteca.listar_livros()
    
    print("\n--- Testando Empréstimo ---")
    minha_biblioteca.emprestar_livro("1984")
    minha_biblioteca.listar_livros()