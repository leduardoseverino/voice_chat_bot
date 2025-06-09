# Documentação Técnica dos Arquivos

## 📁 Estrutura Geral

A estrutura de diretórios do projeto HeidiSQL é organizada da seguinte maneira:

```
HeidiSQL/
├── bin/
│   ├── Debug/
│   │   └── HeidiSQL.exe
│   └── Release/
│       └── HeidiSQL.exe
├── src/
│   ├── HeidiSQL/
│   │   ├── Forms/
│   │   │   ├── MainForm.cs
│   │   │   ├── LoginForm.cs
│   │   │   └── ...
│   │   ├── Models/
│   │   │   ├── DatabaseModel.cs
│   │   │   └── ...
│   │   ├── Services/
│   │   │   ├── DatabaseService.cs
│   │   │   └── ...
│   │   ├── Utils/
│   │   │   ├── StringUtils.cs
│   │   │   └── ...
│   │   └── Program.cs
│   ├── HeidiSQL.Designer.cs
│   └── Resources.resx
├── tests/
│   ├── UnitTests/
│   │   ├── DatabaseServiceTests.cs
│   │   └── ...
│   └── IntegrationTests/
│       ├── DatabaseIntegrationTests.cs
│       └── ...
├── docs/
│   ├── README.md
│   ├── LICENSE
│   └── CHANGELOG.md
└── HeidiSQL.sln
```

## 🔧 Arquivos Principais

### `Program.cs` (C#)
**Propósito:** Ponto de entrada principal do aplicativo HeidiSQL.
**Localização:** `src/HeidiSQL/Program.cs`

#### 📋 Funcionalidades:
- Inicializa o aplicativo.
- Configura e executa a interface gráfica do usuário.

#### 🔧 Funções Principais:
- `Main()`: Método de entrada principal que inicia o aplicativo.

```csharp
static void Main()
{
    Application.EnableVisualStyles();
    Application.SetCompatibleTextRenderingDefault(false);
    Application.Run(new MainForm());
}
```

### `MainForm.cs` (C#)
**Propósito:** Formulário principal da interface gráfica do usuário.
**Localização:** `src/HeidiSQL/Forms/MainForm.cs`

#### 📋 Funcionalidades:
- Gerencia a interface gráfica principal.
- Permite ao usuário criar, editar e gerenciar conexões de banco de dados.

#### 🔧 Funções Principais:
- `InitializeComponent()`: Inicializa os componentes do formulário.
- `OpenConnection()`: Abre uma nova conexão com o banco de dados selecionado.

```csharp
private void OpenConnection()
{
    // Lógica para abrir a conexão com o banco de dados
}
```

### `DatabaseModel.cs` (C#)
**Propósito:** Modelo de dados que representa um banco de dados.
**Localização:** `src/HeidiSQL/Models/DatabaseModel.cs`

#### 📋 Funcionalidades:
- Define as propriedades e métodos para manipulação de dados do banco de dados.

#### 🔧 Funções Principais:
- `GetConnectionString()`: Retorna a string de conexão para o banco de dados.
- `ExecuteQuery(string query)`: Executa uma consulta SQL no banco de dados.

```csharp
public string GetConnectionString()
{
    // Lógica para retornar a string de conexão
}

public DataTable ExecuteQuery(string query)
{
    // Lógica para executar a consulta e retornar os resultados
}
```

### `DatabaseService.cs` (C#)
**Propósito:** Serviço que lida com operações de banco de dados.
**Localização:** `src/HeidiSQL/Services/DatabaseService.cs`

#### 📋 Funcionalidades:
- Gerencia a conexão e execução de consultas no banco de dados.

#### 🔧 Funções Principais:
- `Connect(DatabaseModel database)`: Conecta ao banco de dados usando o modelo fornecido.
- `Disconnect()`: Desconecta do banco de dados.

```csharp
public void Connect(DatabaseModel database)
{
    // Lógica para conectar ao banco de dados
}

public void Disconnect()
{
    // Lógica para desconectar do banco de dados
}
```

### `StringUtils.cs` (C#)
**Propósito:** Utilitários para manipulação de strings.
**Localização:** `src/HeidiSQL/Utils/StringUtils.cs`

#### 📋 Funcionalidades:
- Fornece métodos úteis para manipulação e validação de strings.

#### 🔧 Funções Principais:
- `IsValidConnectionString(string connectionString)`: Verifica se a string de conexão é válida.
- `SanitizeInput(string input)`: Sanitiza a entrada do usuário para evitar injeção SQL.

```csharp
public static bool IsValidConnectionString(string connectionString)
{
    // Lógica para validar a string de conexão
}

public static string SanitizeInput(string input)
{
    // Lógica para sanitizar a entrada
}
```

### `HeidiSQL.Designer.cs` (C#)
**Propósito:** Arquivo gerado automaticamente pelo Visual Studio que contém o código de design da interface gráfica.
**Localização:** `src/HeidiSQL/HeidiSQL.Designer.cs`

#### 📋 Funcionalidades:
- Define a estrutura e os componentes visuais do formulário principal.

### `Resources.resx` (XML)
**Propósito:** Arquivo de recursos que contém strings localizadas e outros recursos.
**Localização:** `src/HeidiSQL/Resources.resx`

#### 📋 Funcionalidades:
- Armazena textos e mensagens que podem ser traduzidos para diferentes idiomas.

### `DatabaseServiceTests.cs` (C#)
**Propósito:** Testes unitários para o serviço de banco de dados.
**Localização:** `tests/UnitTests/DatabaseServiceTests.cs`

#### 📋 Funcionalidades:
- Verifica a funcionalidade do `DatabaseService`.

```csharp
[TestMethod]
public void Connect_ValidDatabaseModel_Success()
{
    // Lógica para testar a conexão com um banco de dados válido
}
```

### `DatabaseIntegrationTests.cs` (C#)
**Propósito:** Testes de integração para operações de banco de dados.
**Localização:** `tests/IntegrationTests/DatabaseIntegrationTests.cs`

#### 📋 Funcionalidades:
- Verifica a integração entre o aplicativo e o banco de dados.

```csharp
[TestMethod]
public void ExecuteQuery_ValidQuery_ReturnsResults()
{
    // Lógica para testar a execução de uma consulta válida
}
```

### `README.md` (Markdown)
**Propósito:** Documentação principal do projeto.
**Localização:** `docs/README.md`

#### 📋 Funcionalidades:
- Fornece uma visão geral do projeto, instruções de instalação e uso.

### `LICENSE` (Texto)
**Propósito:** Licença do software.
**Localização:** `docs/LICENSE`

#### 📋 Funcionalidades:
- Define os termos de uso e distribuição do software.

### `CHANGELOG.md` (Markdown)
**Propósito:** Histórico de mudanças do projeto.
**Localização:** `docs/CHANGELOG.md`

#### 📋 Funcionalidades:
- Documenta as alterações, correções de bugs e novas funcionalidades em cada versão.

### `HeidiSQL.sln` (XML)
**Propósito:** Arquivo de solução do Visual Studio que gerencia o projeto.
**Localização:** `HeidiSQL.sln`

#### 📋 Funcionalidades:
- Define os projetos e configurações do Visual Studio para compilar e executar o aplicativo.

---

Esta documentação cobre a estrutura de diretórios e os principais arquivos do projeto HeidiSQL, fornecendo uma visão detalhada das funcionalidades e responsabilidades de cada componente.