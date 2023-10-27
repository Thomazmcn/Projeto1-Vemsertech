# Projeto Sistema de Gestão de Restaurantes - Vemsertech ADA TECH

Grupo E: </br>
@Micheleregina2022 </br>
@ThiagoRochedo </br>
@Thomazmcn </br>
@AbelNandza 


### Síntese da Proposta do Projeto

**Nome do Projeto:** Sistema de Gestão de Restaurantes

O projeto "Sistema de Gestão de Restaurantes" é uma aplicação em Python desenvolvida para oferecer uma solução completa para gerenciar restaurantes em uma plataforma digital. A proposta visa proporcionar aos alunos uma experiência prática na aplicação de conceitos fundamentais de programação em Python, como variáveis, estruturas condicionais, estruturas de repetição, listas e funções, em um cenário real e útil.

#### Funcionalidades Principais:

1. **Gestão de Restaurantes:**
   - Adição, edição e remoção de restaurantes, com detalhes como nome, endereço, telefone e tempo de entrega.
   
2. **Gestão de Cardápio:**
   - Adição, edição e remoção de itens do cardápio para cada restaurante, com informações sobre nome e preço.
   
3. **Apresentação de Informações:**
   - Visualização detalhada de todos os restaurantes registrados na plataforma, incluindo seus dados.
   - Possibilidade de visualizar o cardápio completo de cada restaurante, listando os alimentos disponíveis e seus preços.

#### Conceitos de Programação Aplicados:

- **Variáveis:** Utilização de variáveis para armazenar informações sobre restaurantes, cardápios e outros dados relevantes.

- **Estruturas Condicionais:** Implementação de estruturas condicionais para tomada de decisões, como verificar a existência de restaurantes ou itens do cardápio.

- **Estruturas de Repetição:** Utilização de estruturas de repetição para gerenciar múltiplos restaurantes e itens de cardápio, percorrendo listas e realizando ações em lote.

- **Listas:** Armazenamento de informações em listas para facilitar a manipulação e organização dos dados relacionados a restaurantes e seus cardápios.

- **Funções:** Criação de funções para organizar o código de forma modular e reutilizável, como funções para adicionar restaurantes, editar cardápios, entre outras.


# Documentação do Código

## Função `Main(acesso="primeiro")`
Esta é a função principal que inicia o fluxo do sistema de Gestão de Restaurantes. Aceita um argumento opcional `acesso` que controla o estado do sistema.

### Comportamento
- Exibe um menu com três opções: Gestão de restaurantes, Gestão de cardápio e Apresentação de informações.
- Redireciona para as funções correspondentes com base na escolha do usuário.
- Em caso de escolha inválida, retorna ao início do fluxo.

## Função `menu_gestao_rest()`
Exibe um menu para a gestão de restaurantes com opções para cadastrar, editar, remover restaurantes ou voltar ao menu principal.

### Comportamento
- Redireciona para as funções correspondentes com base na escolha do usuário.
- Em caso de escolha inválida, retorna ao menu de gestão de restaurantes.

## Função `menu_gestao_cardapio()`
Exibe um menu para a gestão de cardápio com opções para editar cardápios, aplicar desconto ou voltar ao menu principal.

### Comportamento
- Redireciona para as funções correspondentes com base na escolha do usuário.
- Em caso de escolha inválida, retorna ao menu de gestão de cardápio.

## Função `menu_informacoes()`
Exibe um menu para apresentação de informações com opções para listar restaurantes, detalhar restaurantes, visualizar cardápio ou voltar ao menu principal.

### Comportamento
- Redireciona para as funções correspondentes com base na escolha do usuário.
- Em caso de escolha inválida, retorna ao menu de informações.

## Função `cadastro()`
Permite o cadastro de um novo restaurante e seu cardápio.

### Comportamento
- Solicita informações sobre o restaurante (nome, endereço, telefone, tempo de entrega).
- Cadastra o restaurante e redireciona para a criação do cardápio.

## Função `editar_restaurante()`
Permite a edição das informações de um restaurante existente.


## Função `criar_cardapio(nome_restaurante)`
Permite a criação de um cardápio para um restaurante específico.

### Parâmetros
- `nome_restaurante`: Nome do restaurante para o qual o cardápio será criado.

### Comportamento
- Solicita os nomes e preços dos pratos e os adiciona ao cardápio do restaurante.

## Função `editar_cardapio()`
Permite editar o cardápio de um restaurante existente (editar, deletar ou adicionar pratos).

### Comportamento
- Permite editar, deletar ou adicionar pratos ao cardápio do restaurante selecionado.

## Função `tratar_prato(id_restaurante)`
Auxilia na seleção de um prato do cardápio durante a edição.

### Parâmetros
- `id_restaurante`: Índice do restaurante no qual o prato existe.

### Comportamento
- Solicita o número do prato e valida se é um valor válido para o restaurante selecionado.

## Função `visualizar_cardapio(origem)`
Permite visualizar o cardápio de um restaurante.

### Parâmetros
- `origem`: Indica a origem da chamada da função (redirecionamento).

### Comportamento
- Lista os pratos e preços do cardápio do restaurante.

## Função `listar_restaurantes(origem)`
Lista os nomes de todos os restaurantes cadastrados.

### Parâmetros
- `origem`: Indica a origem da chamada da função (redirecionamento).

### Comportamento
- Lista os nomes de todos os restaurantes cadastrados.

## Função `detalhar_restaurantes()`
Apresenta informações detalhadas de um restaurante específico.

### Comportamento
- Lista informações detalhadas (nome, endereço, telefone, tempo de entrega) do restaurante selecionado.

## Função `desconto()`
Aplica um desconto a todos os pratos do cardápio de um restaurante.

### Comportamento
- Permite selecionar um restaurante e define o percentual de desconto a ser aplicado a todos os pratos.

## Função `remover_restaurante()`
Remove um restaurante do sistema.

### Comportamento
- Lista os restaurantes cadastrados e permite selecionar um para remoção.
- Remove o restaurante selecionado, incluindo seu cardápio e preços associados.

Este documento fornece uma visão geral do código e de suas funcionalidades principais.
