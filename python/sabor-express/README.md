# Sabor Express

Sistema de gerenciamento de restaurantes via linha de comando, desenvolvido em Python.

## Descrição

O Sabor Express permite cadastrar, listar e gerenciar o estado (ativo/desativado) de restaurantes. O sistema é executado diretamente no terminal com um menu interativo.

## Funcionalidades

- **Cadastrar restaurante** — adiciona um novo restaurante informando nome e categoria
- **Listar restaurantes** — exibe todos os restaurantes cadastrados com nome, categoria e estado atual
- **Alternar estado do restaurante** — ativa ou desativa um restaurante pelo nome
- **Sair** — encerra a aplicação

## Requisitos

- Python 3.12 ou superior

## Como executar

```bash
python app.py
```

## Estrutura do projeto

```
sabor-express/
└── app.py       # Arquivo principal da aplicação
```

## Estrutura de dados

Cada restaurante é armazenado como um dicionário com os seguintes campos:

| Campo      | Tipo    | Descrição                          |
|------------|---------|------------------------------------|
| `nome`     | string  | Nome do restaurante                |
| `categoria`| string  | Categoria culinária                |
| `ativo`    | boolean | Estado do restaurante (ativo/inativo) |

## Restaurantes pré-cadastrados

| Nome           | Categoria | Estado      |
|----------------|-----------|-------------|
| Praça          | Japonesa  | Desativado  |
| Jacquin        | Italiana  | Ativado     |
| Bacio di Latte | Francês   | Ativado     |
