# Documentação Técnica dos Arquivos

## 📁 Estrutura Geral
A estrutura de diretórios do projeto HeidiSQL é organizada da seguinte maneira:

```
HeidiSQL/
├── src/
│   ├── core/
│   │   ├── database.cpp
│   │   └── database.h
│   ├── gui/
│   │   ├── mainwindow.cpp
│   │   └── mainwindow.h
│   ├── utils/
│   │   ├── logger.cpp
│   │   └── logger.h
├── include/
│   ├── core/
│   │   ├── database.h
│   ├── gui/
│   │   ├── mainwindow.h
│   ├── utils/
│   │   ├── logger.h
├── tests/
│   ├── test_database.cpp
│   ├── test_mainwindow.cpp
│   └── test_logger.cpp
├── CMakeLists.txt
└── README.md
```

## 📁 Descrição dos Arquivos

### `database.cpp` e `database.h`
**Propósito:** Implementação da lógica de negócios e operações de banco de dados.

**Localização:**
- `src/core/database.cpp`
- `include/core/database.h`

**Tecnologias:** C++, Qt Framework

#### 📋 Funcionalidades:
- Conexão com o banco de dados
- Execução de consultas SQL
- Gerenciamento de transações

#### 🛠️ Funções/Métodos Principais:
- `connectToDatabase(QString connectionString)`: Estabelece uma conexão com o banco de dados.
  - **Parâmetros:** `QString connectionString` (string de conexão)
  - **Retorno:** `bool` (true se a conexão for bem-sucedida, false caso contrário)

- `executeQuery(QString query)`: Executa uma consulta SQL.
  - **Parâmetros:** `QString query` (consulta SQL)
  - **Retorno:** `QSqlQuery` (objeto de consulta)

- `beginTransaction()`: Inicia uma transação.
  - **Retorno:** `bool` (true se a transação for iniciada com sucesso, false caso contrário)

- `commitTransaction()`: Confirma a transação atual.
  - **Retorno:** `bool` (true se a transação for confirmada com sucesso, false caso contrário)

- `rollbackTransaction()`: Reverte a transação atual.
  - **Retorno:** `bool` (true se a transação for revertida com sucesso, false caso contrário)

#### 📦 Classes/Estruturas:
- `Database`: Classe principal para gerenciamento de operações de banco de dados.

#### 🔗 APIs/Endpoints:
- Consome a API do Qt Framework para conexões de banco de dados e execução de consultas SQL.

#### 📝 Observações:
Este arquivo é responsável pela lógica de negócios e operações de banco de dados, permitindo que o sistema interaja com o banco de dados de forma eficiente.

### `mainwindow.cpp` e `mainwindow.h`
**Propósito:** Implementação da interface gráfica do usuário.

**Localização:**
- `src/gui/mainwindow.cpp`
- `include/gui/mainwindow.h`

**Tecnologias:** C++, Qt Framework

#### 📋 Funcionalidades:
- Gerenciamento de widgets e eventos
- Interação com o usuário através da interface gráfica

#### 🛠️ Funções/Métodos Principais:
- `MainWindow()`: Construtor da classe MainWindow.
  - **Parâmetros:** Nenhum
  - **Retorno:** Nenhum

- `setupUi()`: Configura a interface gráfica do usuário.
  - **Parâmetros:** Nenhum
  - **Retorno:** Nenhum

- `connectDatabase()`: Conecta ao banco de dados através da interface gráfica.
  - **Parâmetros:** Nenhum
  - **Retorno:** Nenhum

#### 📦 Classes/Estruturas:
- `MainWindow`: Classe principal para gerenciamento da interface gráfica do usuário.

#### 🔗 APIs/Endpoints:
- Consome a API do Qt Framework para criação e gerenciamento de widgets e eventos.

#### 📝 Observações:
Este arquivo é responsável pela interface gráfica do usuário, permitindo que o usuário interaja com o sistema através de uma interface visual intuitiva.

### `logger.cpp` e `logger.h`
**Propósito:** Implementação do sistema de logs.

**Localização:**
- `src/utils/logger.cpp`
- `include/utils/logger.h`

**Tecnologias:** C++, Qt Framework

#### 📋 Funcionalidades:
- Registro de mensagens de log
- Gerenciamento de níveis de log (info, warning, error)

#### 🛠️ Funções/Métodos Principais:
- `logMessage(QString message, LogLevel level)`: Registra uma mensagem de log.
  - **Parâmetros:** `QString message` (mensagem de log), `LogLevel level` (nível de log)
  - **Retorno:** Nenhum

- `setLogLevel(LogLevel level)`: Define o nível de log atual.
  - **Parâmetros:** `LogLevel level` (nível de log)
  - **Retorno:** Nenhum

#### 📦 Classes/Estruturas:
- `Logger`: Classe principal para gerenciamento de logs.

#### 🔗 APIs/Endpoints:
- Consome a API do Qt Framework para criação e gerenciamento de widgets e eventos.

#### 📝 Observações:
Este arquivo é utilizado para registrar mensagens de log em diferentes níveis (info, warning, error), facilitando o diagnóstico e a depuração do sistema.

## 🏗️ Arquitetura e Fluxo
A arquitetura do HeidiSQL segue um padrão MVC (Model-View-Controller), onde:

- **Model:** Representado principalmente pelo `database.cpp`, que lida com a lógica de negócios e operações de banco de dados.
- **View:** Implementada em `mainwindow.cpp`, que gerencia a interface gráfica do usuário.
- **Controller:** A interação entre o modelo e a view é gerenciada através de sinais e slots do Qt Framework.

O fluxo de execução geralmente começa na janela principal (`MainWindow`), onde o usuário pode iniciar uma conexão com o banco de dados. As operações de banco de dados são realizadas pelo `Database`, e os resultados são exibidos na interface gráfica. O sistema de logs (`Logger`) é utilizado para registrar eventos importantes durante a execução do programa.

## 📦 Dependências
- Qt Framework (versão 5.x ou superior)

## 🛠️ Compilação e Execução
Para compilar e executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o Qt Framework instalado em seu sistema.
2. Abra o arquivo `.pro` do projeto no Qt Creator.
3. Configure o kit de compilação adequado para sua plataforma.
4. Clique no botão "Build" para compilar o projeto.
5. Execute o programa através do Qt Creator ou pelo terminal.

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

---

Este README fornece uma visão geral do projeto HeidiSQL, incluindo suas funcionalidades principais, arquitetura, dependências e instruções de compilação e execução.