# Estudos Python - Alura

Repositório de aprendizado Python com foco em progressão do básico ao orientado a objetos. O projeto principal é o **Sabor Express**, um sistema de gerenciamento de restaurantes.

---

## Estrutura do Repositório

```
Alura/python/
├── if_else/                    # Condicionais básicas
├── estrutura_repeticao/        # Laços de repetição
├── sabor-express/              # Versão procedural do projeto
├── oo-sabor-express/           # Versão OO do projeto (PRINCIPAL)
└── desenvolvimento/
    ├── base/                   # Fundamentos
    ├── estrutura_controle/     # Controle de fluxo
    ├── estrutura_repeticao/    # Iteração
    ├── funcoes/                # Funções e lambdas
    ├── lista_e_dicionario/     # Listas e dicionários
    ├── listas_e_tuplas/        # Listas e tuplas
    ├── oo/                     # POO básica
    └── praticando/             # Desafios práticos
```

---

## Projeto Principal: Sabor Express (OO)

Sistema de gerenciamento de restaurantes construído com Programação Orientada a Objetos.

### Como executar

```bash
cd oo-sabor-express
python app.py
```

### Estrutura do projeto

```
oo-sabor-express/
├── app.py                  # Ponto de entrada
└── modelos/
    ├── avaliacao.py        # Classe Avaliacao
    └── restaurante.py      # Classe Restaurante
```

### Conceitos aplicados

- **Classes e instâncias** — `Restaurante` e `Avaliacao`
- **Variáveis de classe** — lista compartilhada de restaurantes
- **Propriedades (`@property`)** — `ativo` com emoji, `media_avaliacoes`
- **Métodos de classe (`@classmethod`)** — `listar_restaurantes()`
- **Encapsulamento** — atributos privados com `_`
- **`__str__`** — representação legível do objeto
- **Agregação** — `Restaurante` contém lista de `Avaliacao`

### Exemplo de uso (app.py)

```python
restaurante_praca = Restaurante('Praça', 'Japonesa')
restaurante_praca.receber_avaliacao('Gui', 8)
restaurante_praca.receber_avaliacao('Ana', 10)
restaurante_praca.alternar_estado()

Restaurante.listar_restaurantes()
```

---

## Versão Procedural: Sabor Express

`sabor-express/app.py` — mesma aplicação usando funções e dicionários (sem classes).

- Interface de menu via CLI
- Funções para cadastrar, listar e alternar status de restaurantes
- Uso de `os.system('clear')` e tratamento de exceções

---

## Trilha de Aprendizado

### 1. Fundamentos (`desenvolvimento/base/`)

| Arquivo | Conceito |
|---|---|
| `apresentar.py` | input/output básico |
| `string.py` | métodos de string (upper, lower, capitalize) |
| `num_int.py` | operações aritméticas |
| `circulo.py` | `math.pi`, cálculo de área |
| `tempo.py` | conversão de segundos em horas:min:seg |
| `moeda.py` | conversor de moedas (Real → Dólar/Euro) |
| `conversor.py` | `match` statement (Python 3.10+) |
| `cpf.py` | validação e formatação de CPF |
| `loja.py` | desconto automático com condicional |
| `aluno.py` | média ponderada de notas |
| `salario_func.py` | cálculo de salário com reajuste |
| `analisa_nome.py` | análise e extração de partes do nome |
| `validacao.py` | validação de múltiplos campos |
| `swap.py` | troca de variáveis |
| `numeros.py` | calculadora com `match` |

### 2. Controle de Fluxo (`if_else/` e `desenvolvimento/estrutura_controle/`)

| Arquivo | Conceito |
|---|---|
| `par_impar.py` | operador módulo `%` |
| `media.py` | aprovação/recuperação/reprovação |
| `calculando_imc.py` | IMC com classificação |
| `ano_bissexto.py` | lógica de ano bissexto |
| `imposto_de_renda.py` | faixas de imposto aninhadas |
| `classificao_idade.py` | classificação por faixa etária |
| `classificacao_filme.py` | rating de filmes |
| `pedra_papel_tesoura.py` | jogo completo com placar e múltiplas rodadas |
| `validador_senha.py` | validação de força de senha |
| `validacao_login.py` | validação de usuário e senha com regras |

### 3. Repetição (`estrutura_repeticao/` e `desenvolvimento/estrutura_repeticao/`)

| Arquivo | Conceito |
|---|---|
| `tabuada.py` | `for` com range |
| `fatorial.py` | acumulador com loop |
| `numeros_pares.py` | filtro com `if` dentro de `for` |
| `numeros_impares.py` | mesma lógica para ímpares |
| `soma.py` | soma de lista com `for` |
| `contagem_regressiva.py` | `while` com decremento |
| `controle_estoque.py` | `while` com menu |
| `livro.py` / `livro_2.py` | rastreador de leitura |

### 4. Funções (`desenvolvimento/funcoes/`)

| Arquivo | Conceito |
|---|---|
| `saudacao.py` | parâmetros e retorno |
| `calcular_idade.py` | função simples com lógica |
| `somando_numeros_recursivamente.py` | **recursão** |
| `calculadora_lambda.py` | **lambda** + dicionário de funções |
| `filtrando_pares.py` | **filter()** com lambda |
| `calculadora_vendas.py` | **map()** e soma |
| `contador_caracter.py` | `len()` |
| `conversor_tipos.py` | conversão int/float/str |
| `juntando_lista.py` | concatenação de listas |
| `numeros_pares.py` | list comprehension |
| `funcoes_personalizadas.py` | funções com `*args`/`**kwargs` |

### 5. Estruturas de Dados (`desenvolvimento/lista_e_dicionario/` e `listas_e_tuplas/`)

**Listas:**
- `lista1.py` a `lista7.py` — criação, iteração, métodos (`append`, `remove`, `sort`), slicing, listas aninhadas, list comprehension

**Dicionários:**
- `dicionario1.py` — CRUD completo com menu interativo
- `dicionario2.py` a `dicionario4.py` — métodos, comprehension, dicionários aninhados

**Tuplas:**
- `relatorio_estoque.py` — concatenação de tupla + lista
- `itens_despensa.py` — verificação de itens
- `lista_convidados.py` — inserção em posição específica
- `voluntario_ong.py` — gerenciamento com tuplas

### 6. POO Básica (`desenvolvimento/oo/`)

| Arquivo | Conceito |
|---|---|
| `carro.py` | classe com atributos, método estático `listar_carros()` |
| `restaurante.py` | protótipo da classe principal do projeto |

### 7. Desafios Práticos (`desenvolvimento/praticando/`)

| Arquivo | Descrição |
|---|---|
| `adivinhar_numero.py` | Jogo de adivinhação 1-100 com dicas |
| `gerador_senha.py` | Senha aleatória de 20 chars com `secrets` |
| `validando_cpf.py` | Validação e formatação de CPF |
| `contador_vogais.py` | Contar vogais em texto |
| `palavra_longa.py` | Encontrar palavra mais longa |
| `gorjeta.py` | Calcular gorjeta |
| `gerenciador_de_tarefas.py` | Sistema de to-do list |
| `contador_bancario.py` | Conta bancária com transações |
| `pedra_papel_tesoura.py` | Jogo vs computador |
| `calculadora_erro.py` | Calculadora com tratamento de exceções |

---

## Conceitos-Chave por Tópico

### Strings
```python
nome.upper()        # MAIÚSCULO
nome.lower()        # minúsculo
nome.capitalize()   # Primeira maiúscula
nome.title()        # Cada Palavra Maiúscula
nome.strip()        # Remove espaços
f"Olá, {nome}!"    # f-string
```

### Listas
```python
lista.append(item)          # adiciona no fim
lista.insert(0, item)       # insere na posição
lista.remove(item)          # remove por valor
lista.pop()                 # remove último
lista.sort()                # ordena in-place
sorted(lista)               # retorna nova lista ordenada
[x for x in lista if x > 0] # list comprehension
```

### Dicionários
```python
d = {'chave': 'valor'}
d['nova'] = 'valor'         # adiciona/atualiza
d.get('chave', 'padrão')    # acessa com fallback
del d['chave']              # remove
d.items()                   # pares chave-valor
d.keys()                    # só chaves
d.values()                  # só valores
```

### Funções
```python
def soma(a, b=0):           # parâmetro com default
    return a + b

dobro = lambda x: x * 2    # lambda

list(filter(lambda x: x % 2 == 0, nums))  # filter
list(map(lambda x: x * 2, nums))          # map

def fatorial(n):            # recursão
    return 1 if n <= 1 else n * fatorial(n - 1)
```

### Classes (POO)
```python
class Restaurante:
    _restaurantes = []                      # variável de classe

    def __init__(self, nome, categoria):
        self._nome = nome.title()           # encapsulamento
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante._restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):                        # getter
        return '🟢' if self._ativo else '🔴'

    @classmethod
    def listar_restaurantes(cls):           # método de classe
        for r in cls._restaurantes:
            print(r)

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 10:
            self._avaliacoes.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        return round(sum(a.nota for a in self._avaliacoes) / len(self._avaliacoes), 1)
```

---

## Tecnologias

- **Python 3.10+** (uso de `match` statement)
- **Módulos padrão:** `os`, `math`, `random`, `secrets`

---

## Referências

- [Alura](https://www.alura.com.br/) — Plataforma de cursos
- [Documentação Python](https://docs.python.org/pt-br/3/)
