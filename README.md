# 📊 Implementação de Algoritmos Clássicos em Grafos

Este repositório contém a implementação de nove algoritmos fundamentais da Teoria dos Grafos, abrangendo problemas de Árvores Geradoras Mínimas (MST), Caminhos Mais Curtos e Grafos Eulerianos. O projeto serve como um estudo prático e material de referência para essas estruturas.

![Status](https://img.shields.io/badge/Status-Finalizado-brightgreen)

## 🗂️ Algoritmos Implementados

O escopo do projeto inclui os seguintes algoritmos, divididos por categoria:

| Categoria | Algoritmo | Status | Responsável |
| :--- | :--- | :--- | :--- |
| **A. Árvores Geradoras Mínimas** | | | |
| (1) | Algoritmo de Kruskal | ✅ Concluído | [Ianco](https://github.com/ianco-so) |
| (2) | Algoritmo de Prim | ✅ Concluído | Kaio Eduardo |
| (3) | Algoritmo de Boruvka (OPC) | ✅ Pendente | [Djavan Costa](https://github.com/djavan93) |
| (4) | Algoritmo de Chu-Liu/Edmonds (OPC) | ✅ Concluído | [Pessoa 1](#pessoa1) |
| **B. Caminho Mais Curto** | | | |
| (5) | Algoritmo de Dijkstra | ✅ Concluído | Kaio Eduardo |
| (6) | Algoritmo de Bellman-Ford | ✅ Concluído | [Ianco](https://github.com/ianco-so) |
| (7) | Algoritmo de Floyd-Warshall | ✅ Pendente | [Djavan Costa](https://github.com/djavan93) |
| **C. Grafos Eulerianos** | | | |
| (8) | Algoritmo de Hierholzer (CICLOS) | ✅ Concluído | [Giliardo Júlio](https://github.com/gili-julio) |
| (9) | Algoritmo de Hierholzer (CAMINHOS) (OPC) | ✅ Concluído | [Giliardo Júlio](https://github.com/gili-julio) |

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
    git clone https://github.com/Felipeftlp/grafosTrabalho02.git
    cd grafosTrabalho02
    ```

2.  **Instale as dependências (por enquanto o pytest):**

    ```bash
    pip install pytest
    ```

3.  **Execute o programa principal:**

    ```bash
    python main.py
    ```

    Este comando executará todos os algoritmos implementados no grafo do trabalho.

## 🧪 Como Executar os Testes

O projeto possui testes unitários completos para os algoritmos implementados.

### Opção 1: Script Simplificado (Recomendado)
```bash
python executar_testes.py
```

### Opção 2: Comando Pytest Direto
```bash
python -m pytest test/ -v
```

### Opção 3: Pytest Curto
```bash
pytest test/ -v
```

## 👥 Equipe e Divisão de Tarefas

O projeto está sendo desenvolvido pela seguinte equipe, com base em uma divisão de carga de trabalho:

*  <a name="pessoa1"></a>**Felipe Freitas (Pessoa 1)** `Algoritmo de Chu-Liu/Edmonds (4)`
*  <a name="Djavan Costa" href="https://github.com/djavan93"></a>**Djavan Costa:** `Algoritmo de Boruvka (3)` e `Algoritmo de Floyd-Warshall (7)`
*  <a name="Ianco" href="https://github.com/ianco-so">**Ianco**:</a> `Algoritmo de Kruskal (1)` e `Algoritmo de Bellman-Ford (6)`
*  <a name="pessoa4"></a>**Giliardo Júlio (Pessoa 4):** `Algoritmo de Hierholzer (CICLOS) (8)` e `Algoritmo de Hierholzer (CAMINHOS) (9)`
*  <a name="pessoa5"></a>**Kaio Eduardo (Pessoa 5):** `Algoritmo de Prim (2)` e `Algoritmo de Dijkstra (5)`
