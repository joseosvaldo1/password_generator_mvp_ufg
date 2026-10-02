# Escopo do MVP

## 1. Objetivo
Desenvolver uma aplicação web simples, utilizando Streamlit, para gerar senhas aleatórias e seguras com base em critérios definidos pelo usuário. A solução deve permitir que o usuário configure o tamanho da senha e escolha se deseja incluir letras maiúsculas, letras minúsculas, números e caracteres especiais, com foco em simplicidade, rapidez e segurança.

## 2. Contexto do Projeto
O projeto visa atender a uma necessidade comum: criar senhas fortes e personalizadas sem exigir conhecimentos avançados em segurança da informação. A aplicação deve ser intuitiva, acessível e funcional, com foco em um MVP (Produto Mínimo Viável), ou seja, uma versão inicial com recursos essenciais para uso prático.

## 3. Escopo do MVP
O MVP incluirá as funcionalidades mínimas necessárias para que o usuário:
- configure critérios de geração;
- gere uma senha aleatória e segura;
- visualize o resultado;
- copie a senha gerada para uso externo.

## 4. Requisitos Funcionais

### RF01 — Configuração do tamanho da senha
O sistema deve permitir que o usuário informe o número de caracteres da senha a ser gerada.

Critérios:
- valor mínimo definido pelo sistema, como 8 caracteres;
- valor máximo definido pelo sistema, como 64 caracteres;
- validação para impedir valores inválidos.

### RF02 — Inclusão de letras minúsculas
O sistema deve permitir que o usuário escolha incluir letras minúsculas na senha.

### RF03 — Inclusão de letras maiúsculas
O sistema deve permitir que o usuário escolha incluir letras maiúsculas na senha.

### RF04 — Inclusão de números
O sistema deve permitir que o usuário escolha incluir números na senha.

### RF05 — Inclusão de caracteres especiais
O sistema deve permitir que o usuário escolha incluir caracteres especiais, como: !, @, #, $, %, &, *, ?, _, -.

### RF06 — Geração de senha aleatória
O sistema deve gerar uma senha aleatória com base nas opções selecionadas pelo usuário.

Critérios:
- a senha deve respeitar os critérios escolhidos;
- deve conter pelo menos um tipo de caractere selecionado, quando aplicável;
- deve evitar geração inválida ou inconsistente.

### RF07 — Visualização do resultado
A senha gerada deve ser exibida na interface em um local claro e legível.

### RF08 — Copiar senha
O sistema deve oferecer uma ação para copiar a senha gerada para a área de transferência do usuário.

### RF09 — Validação de critérios
O sistema deve impedir que o usuário monte uma configuração que gere uma senha inválida ou impossível, como:
- tamanho zero ou inferior ao mínimo;
- ausência total de tipos de caracteres selecionados;
- entradas fora do intervalo permitido.

### RF10 — Feedback ao usuário
A interface deve informar ao usuário quando a geração for concluída com sucesso e quando houver erro na configuração.

## 5. Requisitos Não Funcionais

### RNF01 — Interface simples e intuitiva
A aplicação deve ter uma interface clara, amigável e de fácil uso, mesmo para usuários iniciantes.

### RNF02 — Performance
A geração da senha deve ocorrer em tempo imediato, sem lentidão perceptível para o usuário.

### RNF03 — Segurança
A geração deve ser baseada em mecanismos seguros de aleatoriedade, evitando padrões previsíveis ou geração fraca.

### RNF04 — Portabilidade
A aplicação deve funcionar em ambientes comuns de uso, como Windows, Linux e macOS, desde que o Python e o Streamlit estejam instalados.

### RNF05 — Manutenibilidade
O código deve estar organizado, com estrutura simples e fácil de entender para futuras melhorias.

### RNF06 — Responsividade
A interface deve ser funcional em telas de desktop e em resoluções médias, sem quebrar o layout principal.

## 6. Requisitos de Usabilidade
- O usuário deve conseguir gerar uma senha em poucos segundos.
- Os campos e opções devem ser fáceis de identificar.
- O fluxo principal deve ser simples: selecionar critérios → gerar senha → copiar resultado.

## 7. Fora de Escopo
Os itens abaixo não fazem parte do MVP e podem ser implementados em versões futuras:

- armazenamento de senhas em banco de dados;
- autenticação de usuários;
- login e cadastro;
- gerenciamento de contas e credenciais;
- criptografia de senhas salvas localmente;
- histórico persistente de senhas geradas;
- exportação em arquivos (CSV, TXT, JSON, etc.);
- integração com navegadores ou extensões;
- verificação de força da senha com regras complexas de segurança;
- geração de senhas baseadas em frases ou palavras;
- suporte a múltiplos idiomas;
- geração de relatórios ou dashboards;
- compartilhamento de senhas entre usuários;
- API REST ou backend separado.

## 8. Critérios de Aceitação do MVP
O MVP será considerado concluído quando:
1. o usuário puder definir tamanho da senha;
2. o usuário puder escolher incluir letras maiúsculas, minúsculas, números e caracteres especiais;
3. a aplicação gerar uma senha aleatória conforme as opções escolhidas;
4. a senha seja exibida corretamente na interface;
5. o usuário consiga copiar a senha para a área de transferência;
6. a aplicação valide entradas inválidas e informe o erro de forma clara.

## 9. Resumo do Escopo
O MVP do projeto consiste em uma aplicação web simples para geração de senhas aleatórias e seguras, com personalização de critérios pelo usuário. O foco está na funcionalidade principal: permitir que o usuário crie senhas fortes de forma rápida e intuitiva, sem incluir recursos avançados de armazenamento, autenticação ou gerenciamento de credenciais.

## 10. Conclusão
Este MVP tem como objetivo entregar uma solução funcional, acessível e prática para geração de senhas seguras. A proposta é manter a aplicação simples, focada no uso direto e na experiência do usuário, deixando recursos mais complexos para evoluções futuras.
