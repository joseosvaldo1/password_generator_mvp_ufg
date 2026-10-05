# Password Generator MVP

Aplicação web para geração de senhas seguras, com interface em Streamlit, validação de regras de negócio e avaliação de força baseada em entropia e variedade de caracteres.

## Deploy online

A aplicação está disponível em:

- https://passwordgeneratorufg.streamlit.app/

## Visão geral

O projeto tem como objetivo oferecer uma ferramenta simples e funcional para gerar senhas fortes, configuráveis e fáceis de usar. A aplicação permite:

- definir o tamanho da senha
- ativar ou desativar letras maiúsculas, minúsculas, números e símbolos
- validar regras da política de senha
- avaliar a força da senha em tempo real
- gerar uma senha segura em poucos segundos

A solução foi estruturada em camadas para manter organização e facilitar testes automatizados.

## Stack tecnológica

- Python 3.10+
- Streamlit
- Pytest
- Git
- VS Code

## Requisitos

- Python 3.10 ou superior
- pip
- ambiente virtual (`venv`)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/joseosvaldo1/password_generator_mvp_ufg.git
cd password_project_ufg
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução da aplicação

Na raiz do projeto, execute:

```bash
streamlit run main/app.py
```

Ou, se estiver usando o ambiente já configurado:

```bash
python -m streamlit run main/app.py
```

A aplicação abrirá no navegador em um endereço semelhante a:

```text
http://localhost:8501
```

## Estrutura do projeto

```text
password_project_ufg/
├── app/
│   └── models/
│       ├── __init__.py
│       ├── domain.py
│       ├── interface.py
│       ├── services.py
│       └── tests.py
├── docs/
│   ├── arquitetura-componentes.md
│   ├── backlog.md
│   └── escopo-mvp.md
├── main/
│   └── app.py
├── tests/
│   ├── test_password_domain.py
│   ├── test_password_service.py
│   └── test_password_interface.py
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/
```

## Arquitetura

O projeto foi organizado em camadas para manter a separação de responsabilidades:

### 1. Camada de domínio
Arquivo principal: `app/models/domain.py`

Responsável por:
- definição de políticas de senha
- regras de validação
- geração aleatória
- classificação de força da senha
- avaliação de entropia e variedade de caracteres

### 2. Camada de serviço
Arquivo principal: `app/models/services.py`

Responsável por:
- encapsular regras de negócio
- orquestrar geração e validação
- expor operações reutilizáveis para a interface

### 3. Camada de interface
Arquivo principal: `app/models/interface.py`

Responsável por:
- renderizar controles do Streamlit
- coletar configurações do usuário
- mostrar feedback visual da força da senha
- apresentar a senha gerada em formato legível para cópia

### 4. Camada de entrada da aplicação
Arquivo principal: `main/app.py`

Responsável por:
- inicializar a aplicação
- configurar o caminho do projeto
- chamar a interface principal

## Uso da IA

A aplicação foi desenvolvida com apoio do GitHub Copilot como assistente de código, utilizado para:

- acelerar a escrita e revisão do código Python
- sugerir melhorias de estrutura, clareza e organização do projeto
- auxiliar na criação e refinamento de testes automatizados
- apoiar a análise de regras de negócio e da lógica de força da senha
- propor melhorias na interface e no fluxo de validação do usuário

A IA também é parte da visão de evolução do produto para cenários futuros, como:

- recomendar combinações seguras de caracteres
- explicar por que uma senha está fraca, média ou forte
- sugerir melhorias em tempo real com base na política configurada
- orientar o usuário em relação ao tamanho ideal e à combinação de grupos de caracteres

Nesse MVP, a IA foi usada sobretudo como assistente de desenvolvimento, enquanto o núcleo funcional da geração e validação continua sendo executado localmente sem depender de serviços externos.

## Testes

A suíte de testes está localizada em `tests/` e cobre:

- validação de tamanho mínimo e máximo
- rejeição de opções inválidas
- presença de letras maiúsculas, minúsculas, números e símbolos
- geração conforme a política selecionada
- força da senha baseada em entropia e variedade
- comportamento da interface e mensagens de erro

Para executar os testes:

```bash
pytest
```

Ou, se quiser usar o ambiente virtual:

```bash
.\.venv\Scripts\python -m pytest -q
```

## Limitações

A solução atual ainda possui algumas limitações importantes:

- a geração é aleatória e segura dentro do escopo do projeto, mas não possui histórico persistente de senhas geradas
- não há armazenamento seguro de senhas ou credenciais
- não há autenticação ou gerenciamento de usuários
- a avaliação de força é heurística e orientada à experiência do usuário, não a uma análise criptográfica profunda
- a interface é funcional e clara, mas ainda é um MVP voltado para demonstração e validação de conceito

## Próximos passos

Algumas melhorias planejadas para evolução do projeto:

- histórico de senhas geradas com opção de visualizar e copiar
- exportação em formatos úteis
- mecanismo de sugestão inteligente com IA
- ranking de segurança mais detalhado
- suporte a geração em lote
- melhorias de UX e acessibilidade
- integração com autenticação segura em cenários reais

## Contribuição

Contribuições são bem-vindas. Para sugerir melhorias ou corrigir bugs:

1. faça um fork do projeto
2. crie uma branch para a funcionalidade
3. implemente a mudança
4. rode os testes
5. envie um pull request

## Licença

Este projeto é destinado a fins educacionais e de demonstração. Pode ser adaptado e expandido conforme a necessidade do desenvolvimento.
