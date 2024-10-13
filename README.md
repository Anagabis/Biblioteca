  <h1>Projeto Biblioteca 📚</h1>
    <p>Este projeto é uma aplicação de gerenciamento de biblioteca, onde é possível gerenciar livros e usuários de forma eficiente.</p>

  <h2>Estrutura do Projeto</h2>
    <pre>
biblioteca/
│
├── main.py                  # 🎯 Ponto de entrada do aplicativo
│
├── presentation/            # 🖥️ Camada de Apresentação
│   ├── cli.py               # 💻 Interface de linha de comando
│   └── gui.py               # 🖼️ Interface gráfica (opcional)
│
├── business/                # ⚙️ Camada de Negócio
│   ├── library_manager.py    # 📖 Lógica de negócios para gerenciamento de livros
│   └── user_manager.py       # 👤 Lógica de negócios para gerenciamento de usuários
│
└── persistence/             # 💾 Camada de Persistência
    ├── book_repository.py    # 📚 Persistência de livros
    └── user_repository.py     # 🧑‍🤝‍🧑 Persistência de usuários
    </pre>

  <h2>Como Usar</h2>
    <ol>
        <li><strong>Clone o repositório</strong>:
            <pre>
git clone https://github.com/Anagabis/biblioteca.git
cd biblioteca       </pre>
        </li>
        <li><strong>Execute na IDE OU VScode</strong>:
            <pre>
python main.py </pre>
        </li>
        <li><strong>Escolha a interface</strong>: Você pode optar pela interface de linha de comando ou pela interface gráfica (se implementada).</li>
    </ol>

   <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias.</p>

  <h2>Licença</h2>
    <p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>

</body>
</html>
