from arquitetura.business import library_manager
import arquitetura

# Exemplo de uso
resultado = arquitetura.funcao_exemplo(arquitetura)
print(resultado)

from presentation.cli import CLI

if __name__ == "__main__":
    cli = library_manager
    cli.run()
