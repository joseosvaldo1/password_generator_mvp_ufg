# Password Generator MVP

Projeto de Produto Mínimo Viável para um gerador de senhas seguras com interface web, desenvolvido em Python usando Streamlit.

## Objetivo

Criar uma aplicação simples e funcional que gere senhas aleatórias e seguras com base em critérios definidos pelo usuário, como:

- tamanho da senha
- inclusão de letras maiúsculas
- inclusão de letras minúsculas
- inclusão de números
- inclusão de caracteres especiais

A proposta também contempla uma experiência assistida por IA, com reforço de segurança e usabilidade na geração das senhas.

## Stack

- Python
- Streamlit
- Git
- VS Code

## Requisitos

- Python 3.10 ou superior
- pip
- ambiente virtual (venv)

## Como rodar localmente

1. Abra o terminal na raiz do projeto.
2. Ative o ambiente virtual:

```bash
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie a aplicação:

```bash
streamlit run app.py
```

5. Acesse no navegador a URL exibida no terminal, normalmente:

```text
http://localhost:8501
```

## Estrutura inicial do projeto

```text
password_project_ufg/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── tests/
│   └── test_password_generator.py
├── .venv/
└── .git/
```

## Funcionalidades previstas

- geração de senha com tamanho configurável
- escolha de tipos de caracteres
- cópia fácil da senha gerada
- interface web intuitiva
- indicadores de segurança
- testes automatizados para validar a geração das senhas
- futura integração com IA para auxiliar na criação de senhas

## Roadmap de releases

### Release 1.0 - MVP
- geração básica de senhas
- parâmetros personalizáveis
- interface simples com Streamlit
- cópia da senha para área de transferência

### Release 1.1 - Melhorias de UX
- validação visual de força da senha
- mensagens de recomendação de segurança
- suporte a geração em lote

### Release 2.0 - Assistência com IA
- sugestões inteligentes de senhas
- explicação de critérios de segurança
- recomendações personalizadas

### Release 3.0 - Produto mais completo
- histórico de senhas geradas
- exportação de senhas
- autenticação e armazenamento seguro (quando aplicável)
- integração com serviços externos

## Testes

Os testes do projeto devem ficar na pasta `tests/` e validar:

- tamanho mínimo e máximo da senha
- presença de letras maiúsculas, minúsculas, números e caracteres especiais
- geração aleatória com critérios configurados
- rejeição de entradas inválidas

Para executar os testes:

```bash
pytest
```

## Observações

Este projeto foi iniciado como um MVP para validar a ideia de um gerador de senhas seguras com interface amigável e potencial para evolução com inteligência artificial.

## Licença

Este projeto é de uso educacional e pode ser adaptado conforme a necessidade do desenvolvimento.
