class library_manager:
    def __init__(self, library_manager):
        self.library_manager = library_manager

    def display_menu(self):
        print("\nGerenciador de Biblioteca")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Excluir livro")
        print("4. Sair")

    def add_book(self):
        title = input("Título do livro: ")
        author = input("Autor do livro: ")
        self.library_manager.add_book(title, author)
        print("Livro adicionado!")

    def list_books(self):
        books = self.library_manager.list_books()
        if not books:
            print("Nenhum livro encontrado.")
        for book in books:
            print(f"{book['title']} por {book['author']}")

    def delete_book(self):
        title = input("Título do livro a excluir: ")
        self.library_manager.delete_book(title)
        print("Livro excluído!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.delete_book()
            elif choice == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
