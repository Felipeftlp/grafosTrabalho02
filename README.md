# 📊 Implementação de Algoritmos Clássicos em Grafos

Este repositório contém a implementação de nove algoritmos fundamentais da Teoria dos Grafos, abrangendo problemas de Árvores Geradoras Mínimas (MST), Caminhos Mais Curtos e Grafos Eulerianos. O projeto serve como um estudo prático e material de referência para essas estruturas.

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 🗂️ Algoritmos Implementados

O escopo do projeto inclui os seguintes algoritmos, divididos por categoria:

| Categoria | Algoritmo | Status | Responsável |
| :--- | :--- | :--- | :--- |
| **A. Árvores Geradoras Mínimas** | | | |
| (1) | Algoritmo de Kruskal | ⏳ Pendente | [Pessoa 3](#seuNome3) |
| (2) | Algoritmo de Prim | ⏳ Pendente | [Pessoa 5](#seuNome5) |
| (3) | Algoritmo de Boruvka (OPC) | ⏳ Pendente | [Pessoa 2] |
| (4) | Algoritmo de Chu-Liu/Edmonds (OPC) | ⏳ Pendente | [Pessoa 1](#felipe) |
| **B. Caminho Mais Curto** | | | |
| (5) | Algoritmo de Dijkstra | ⏳ Pendente | [Pessoa 5](#seuNome5) |
| (6) | Algoritmo de Bellman-Ford | ⏳ Pendente | [Pessoa 3](#seuNome3) |
| (7) | Algoritmo de Floyd-Warshall | ⏳ Pendente | [Pessoa 2](#seuNome2) |
| **C. Grafos Eulerianos** | | | |
| (8) | Algoritmo de Hierholzer (CICLOS) | ⏳ Pendente | [Pessoa 4](#seuNome4) |
| (9) | Algoritmo de Hierholzer (CAMINHOS) (OPC) | ⏳ Pendente | [Pessoa 4](#seuNome4) |

## 💻 Tecnologias (Stack)

Este projeto é desenvolvido puramente em **Python 3.x**.

Recomenda-se o uso das seguintes bibliotecas para auxiliar na criação das estruturas de grafos, testes e visualização:

* **`networkx`**: Para criar, manipular e estudar as estruturas de grafos (embora os algoritmos em si devam ser implementados "do zero").
* **`matplotlib`**: Usado pelo `networkx` para desenhar e visualizar os grafos.
* **`pytest`**: Para a criação de testes unitários robustos para cada algoritmo.

## 🚀 Como Executar

Siga as instruções abaixo para executar o projeto em sua máquina local.

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    cd nome-da-pasta-do-projeto
    ```

2.  **Instale as dependências:**

    ```bash
    # Exemplo para Python com pip
    pip install -r requirements.txt
    ```

3.  **Execute o programa (ou testes):**

    ```bash
    # Exemplo para Python
    python main.py
    ```

## 👥 Equipe e Divisão de Tarefas

O projeto está sendo desenvolvido pela seguinte equipe, com base em uma divisão de carga de trabalho:

*  <a name="felipe"></a>**Felipe** `Algoritmo de Chu-Liu/Edmonds (4)`
*  <a name="seuNome1"></a>**Seu nome:** `Algoritmo de Boruvka (3)` e `Algoritmo de Floyd-Warshall (7)`
*  <a name="seuNome2"></a>**Seu nome:** `Algoritmo de Kruskal (1)` e `Algoritmo de Bellman-Ford (6)`
*  <a name="seuNome3"></a>**Seu nome:** `Algoritmo de Hierholzer (CICLOS) (8)` e `Algoritmo de Hierholzer (CAMINHOS) (9)`
*  <a name="seuNome4"></a>**Seu nome:** `Algoritmo de Prim (2)` e `Algoritmo de Dijkstra (5)`
