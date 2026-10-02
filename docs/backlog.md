# Backlog Mínimo do Projeto

## Release 1 - Core

### [ ] RF-01 — Definir tamanho da senha
**Descrição:** O usuário deve poder informar o número de caracteres da senha.

**Critério de aceite:**
[ ] O sistema exibe um campo para inserir o tamanho da senha.
[ ] O valor aceito deve estar dentro do intervalo mínimo e máximo definido.
[ ] Se o valor for inválido, o sistema informa o erro e não gera a senha.

### [ ] RF-02 — Selecionar letras minúsculas
**Descrição:** O usuário deve poder incluir letras minúsculas na geração da senha.

**Critério de aceite:**
[ ] Existe uma opção para ativar ou desativar letras minúsculas.
[ ] Quando ativa, a senha pode conter letras minúsculas.
[ ] Quando desativada, a senha não inclui esse tipo de caractere.

### [ ] RF-03 — Selecionar letras maiúsculas
**Descrição:** O usuário deve poder incluir letras maiúsculas na geração da senha.

**Critério de aceite:**
[ ] Existe uma opção para ativar ou desativar letras maiúsculas.
[ ] Quando ativa, a senha pode conter letras maiúsculas.
[ ] Quando desativada, a senha não inclui esse tipo de caractere.

### [ ] RF-04 — Selecionar números
**Descrição:** O usuário deve poder incluir números na geração da senha.

**Critério de aceite:**
[ ] Existe uma opção para ativar ou desativar números.
[ ] Quando ativa, a senha pode conter números.
[ ] Quando desativada, a senha não inclui esse tipo de caractere.

### [ ] RF-05 — Selecionar caracteres especiais
**Descrição:** O usuário deve poder incluir caracteres especiais na geração da senha.

**Critério de aceite:**
[ ] Existe uma opção para ativar ou desativar caracteres especiais.
[ ] Quando ativa, a senha pode conter caracteres especiais.
[ ] Quando desativada, a senha não inclui esse tipo de caractere.

### [ ] RF-06 — Gerar senha aleatória
**Descrição:** O sistema deve gerar uma senha aleatória conforme as opções selecionadas.

**Critério de aceite:**
[ ] A senha é gerada após a interação do usuário.
[ ] A senha respeita os critérios configurados.
[ ] O resultado não contém tipos de caracteres não selecionados.

### [ ] FT-01 — Interface básica de geração
**Descrição:** A interface deve permitir que o usuário configure os critérios e veja o resultado.

**Critério de aceite:**
[ ] O usuário consegue visualizar todos os controles de configuração.
[ ] A senha gerada aparece na tela de forma legível.
[ ] A interface funciona sem erros visuais básicos.

---

## Release 2 - Qualidade

### [ ] RF-07 — Validar regras da senha
**Descrição:** O sistema deve impedir configurações inválidas ou inconsistentes.

**Critério de aceite:**
[ ] Se nenhuma categoria for selecionada, o sistema exibe uma mensagem de erro.
[ ] Se o tamanho for inválido, o sistema bloqueia a geração.
[ ] Mensagens de validação são claras e compreensíveis.

### [ ] RF-08 — Feedback visual de sucesso/erro
**Descrição:** O sistema deve informar ao usuário sobre o resultado da operação.

**Critério de aceite:**
[ ] Em caso de sucesso, a aplicação confirma a geração da senha.
[ ] Em caso de erro, mostra uma mensagem explicando o problema.
[ ] O feedback é visível na interface sem quebrar o layout.

### [ ] FT-02 — Experiência de uso refinada
**Descrição:** Melhorar a usabilidade da aplicação para uma experiência mais clara e amigável.

**Critério de aceite:**
[ ] Os campos e botões estão organizados visualmente.
[ ] O fluxo principal é simples e direto.
[ ] A aplicação se mantém estável em uso comum.

---

## Release 3 - Entrega Final

### [ ] RF-09 — Copiar senha para a área de transferência
**Descrição:** O usuário deve poder copiar a senha gerada com um único clique.

**Critério de aceite:**
[ ] Existe um botão ou ação para copiar a senha.
[ ] A senha é copiada com sucesso para a área de transferência.
[ ] O usuário recebe confirmação visual de que a cópia ocorreu.

### [ ] RF-10 — Exibir senha de forma segura e legível
**Descrição:** A senha deve ser apresentada de forma clara para o usuário, sem comprometer a usabilidade.

**Critério de aceite:**
[ ] A senha aparece em um campo ou área visível.
[ ] O texto é legível e está bem formatado.
[ ] O layout permanece funcional em telas comuns.

### [ ] FT-03 — Finalização da entrega
**Descrição:** A aplicação deve estar pronta para uso em ambiente de demonstração ou entrega final.

**Critério de aceite:**
[ ] A aplicação executa sem erros básicos.
[ ] Todas as funcionalidades do MVP estão disponíveis.
[ ] A interface final está consistente e pronta para uso.

---

## Resumo do Backlog

- Release 1: foco em geração básica e interface principal.
- Release 2: foco em validação, qualidade e usabilidade.
- Release 3: foco em polimento final, cópia e entrega estável.
