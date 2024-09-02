# Calculadora-GUI-OO

---

Calculadora gráfica (GUI) simples produzido em Python usando a biblioteca `tkinter`. A calculadora possui operações matemáticas básicas, como adição, subtração, multiplicação e divisão.

## Instalação
- E recomendado que use uma plataforma de edição de código `Visual Studio Code`, e também certifique que tenha baixado todas as extensões do `python`.
  
1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências necessárias:**

   Não há dependências adicionais para este projeto, pois ele utiliza apenas a biblioteca padrão `tkinter`, que já vem instalada com o Python.

## Execução

Para executar a calculadora, execute o seguinte comando no diretório do projeto:

```bash
python NomeDoArquivo.py
```

## Funcionalidades

- Suporte para operações básicas: soma (+), subtração (-), multiplicação (*) e divisão (/).
- Botão "C" para limpar a tela.
- Exibição dos resultados na mesma interface da calculadora.

## Decisões de Design

### 1. Interface de Usuário com `tkinter`

`tkinter` é uma biblioteca padrão do Python para a criação de interfaces gráficas. Foi escolhida por sua simplicidade e facilidade de uso, além de ser adequada para projetos pequenos e médios.

### 2. Organização do Código

A classe `Calculadora` encapsula toda a lógica da interface gráfica e da manipulação de eventos. O uso de classes permite uma maior modularidade e facilita a manutenção e expansão futura do código.

### 3. Uso de `eval` para Cálculo de Expressões

O método `calculate_expression` utiliza a função `eval` para avaliar a expressão aritmética inserida pelo usuário. **Nota:** O uso de `eval` pode ser perigoso se a entrada do usuário não for controlada. Em um ambiente de produção ou com entradas de usuários não confiáveis, é recomendável substituir `eval` por uma função de parser matemático mais segura.

### 4. Tratamento de Erros

A função `calculate_expression` inclui um bloco `try-except` para capturar exceções e exibir "Erro" na tela se uma expressão inválida for inserida. Esse tratamento básico de erros melhora a usabilidade, evitando que o programa feche inesperadamente.
