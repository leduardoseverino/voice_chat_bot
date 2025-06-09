# Visão Geral do Projeto

## 📋 Descrição do Projeto

O projeto **Calculator_App** é uma aplicação de calculadora desenvolvida com o objetivo de fornecer uma ferramenta simples e eficiente para realizar cálculos matemáticos básicos. Este projeto utiliza tecnologias modernas e segue boas práticas de desenvolvimento de software para garantir robustez, escalabilidade e manutenibilidade.

### Propósito

A principal finalidade do **Calculator_App** é oferecer uma calculadora funcional que pode ser utilizada tanto em dispositivos móveis quanto em desktops. A aplicação visa simplificar a realização de operações matemáticas cotidianas, como adição, subtração, multiplicação e divisão, além de suportar funções mais avançadas conforme necessário.

### Tecnologias Utilizadas

- **Linguagem de Programação:** JavaScript
- **Framework:** React.js
- **Estilização:** CSS (com suporte para SASS)
- **Gerenciamento de Estado:** Redux
- **Build Tool:** Webpack
- **Testes:** Jest e React Testing Library

### Arquitetura do Projeto

O projeto segue uma arquitetura modular, onde cada componente da aplicação é responsável por uma parte específica da funcionalidade. A estrutura do projeto é organizada da seguinte forma:

```
src/
├── components/
│   ├── Button.js
│   ├── Display.js
│   └── Calculator.js
├── redux/
│   ├── actions/
│   ├── reducers/
│   └── store.js
├── styles/
│   ├── main.css
│   └── variables.scss
└── App.js
```

## 🚀 Instruções de Uso

### Pré-requisitos

Antes de começar, certifique-se de ter instalado as seguintes ferramentas:

- Node.js (versão 12 ou superior)
- npm (gerenciador de pacotes do Node.js)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/giangciti/Calculator_App.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Calculator_App
   ```

3. Instale as dependências:
   ```bash
   npm install
   ```

### Execução

Para iniciar a aplicação em modo de desenvolvimento, execute o seguinte comando:

```bash
npm start
```

A aplicação estará disponível no endereço `http://localhost:3000`.

### Testes

Para executar os testes unitários, utilize o seguinte comando:

```bash
npm test
```

## 📝 Observações

- **Contribuições:** Contribuições são bem-vindas! Para contribuir, por favor, siga as diretrizes de contribuição no arquivo `CONTRIBUTING.md`.
- **Licença:** Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
- **Suporte:** Para suporte ou dúvidas, abra uma issue no repositório do GitHub.

---

**Nota:** Esta documentação é um guia inicial e pode ser expandida conforme necessário.

# Guia de Documentação

## 📚 Documentação Detalhada

### Estrutura do Projeto

#### `src/components/`

- **Button.js**: Componente responsável por renderizar os botões da calculadora.
  ```javascript
  import React from 'react';

  const Button = ({ label, onClick }) => (
    <button onClick={onClick}>
      {label}
    </button>
  );

  export default Button;
  ```

- **Display.js**: Componente responsável por exibir o resultado da calculadora.
  ```javascript
  import React from 'react';

  const Display = ({ value }) => (
    <div className="display">
      {value}
    </div>
  );

  export default Display;
  ```

- **Calculator.js**: Componente principal que integra os botões e o display da calculadora.
  ```javascript
  import React, { useState } from 'react';
  import Button from './Button';
  import Display from './Display';

  const Calculator = () => {
    const [input, setInput] = useState('');

    const handleClick = (value) => {
      setInput(input + value);
    };

    return (
      <div className="calculator">
        <Display value={input} />
        <Button label="1" onClick={() => handleClick('1')} />
        {/* Adicione mais botões aqui */}
      </div>
    );
  };

  export default Calculator;
  ```

#### `src/redux/`

- **actions/**: Diretório contendo as ações Redux.
  ```javascript
  // actions.js
  export const SET_INPUT = 'SET_INPUT';

  export const setInput = (input) => ({
    type: SET_INPUT,
    payload: input,
  });
  ```

- **reducers/**: Diretório contendo os reducers Redux.
  ```javascript
  // reducer.js
  import { SET_INPUT } from '../actions';

  const initialState = {
    input: '',
  };

  const calculatorReducer = (state = initialState, action) => {
    switch (action.type) {
      case SET_INPUT:
        return {
          ...state,
          input: action.payload,
        };
      default:
        return state;
    }
  };

  export default calculatorReducer;
  ```

- **store.js**: Configuração da store Redux.
  ```javascript
  import { createStore } from 'redux';
  import calculatorReducer from './reducers';

  const store = createStore(calculatorReducer);

  export default store;
  ```

#### `src/styles/`

- **main.css**: Estilos principais da aplicação.
  ```css
  .display {
    font-size: 2em;
    text-align: right;
    padding: 10px;
    border: 1px solid #ccc;
  }

  button {
    font-size: 1.5em;
    padding: 10px;
    margin: 5px;
  }
  ```

- **variables.scss**: Variáveis SCSS para estilos.
  ```scss
  $primary-color: #3498db;

  .calculator {
    background-color: $primary-color;
  }
  ```

#### `App.js`

- **App.js**: Componente principal da aplicação.
  ```javascript
  import React from 'react';
  import Calculator from './components/Calculator';

  const App = () => (
    <div className="app">
      <Calculator />
    </div>
  );

  export default App;
  ```

## 📝 Observações Finais

- **Contribuições:** Contribuições são bem-vindas! Para contribuir, por favor, siga as diretrizes de contribuição no arquivo `CONTRIBUTING.md`.
- **Licença:** Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
- **Suporte:** Para suporte ou dúvidas, abra uma issue no repositório do GitHub.

---

**Nota:** Esta documentação é um guia inicial e pode ser expandida conforme necessário.