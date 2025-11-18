"""
Implementação do Algoritmo de Hierholzer para encontrar CAMINHOS eulerianos.
Entrada: grafo não direcionado representado como dicionário {vertice: [lista_de_vizinhos]}
Saída: caminho euleriano caso exista.
"""

from collections import defaultdict


def verifica_caminho_euleriano(grafo):
    """
    Verifica se um grafo NÃO DIRECIONADO possui caminho euleriano.

    Condições para caminho euleriano (não direcionado):
    - 0 vértices de grau ímpar → ciclo euleriano (também vale como caminho)
    - 2 vértices de grau ímpar → caminho euleriano
    - qualquer outro valor → não possui
    """
    graus = defaultdict(int)

    for u in grafo:
        graus[u] += len(grafo[u])

    impares = [v for v in graus if graus[v] % 2 == 1]

    return len(impares) in (0, 2)


def hierholzer_caminho(grafo):
    """
    Encontra um caminho euleriano caso exista (grafo NÃO direcionado).
    """
    # Copia profunda para não alterar o grafo original
    g = {u: vizinhos[:] for u, vizinhos in grafo.items()}

    # Conta graus para escolher o vértice inicial
    graus = defaultdict(int)
    for u in g:
        graus[u] += len(g[u])

    impares = [v for v in graus if graus[v] % 2 == 1]

    # Regra do grafo não direcionado
    if len(impares) == 2:
        inicio = impares[0]
    else:  # 0 ímpares → pode começar de qualquer vértice com arestas
        inicio = next((v for v in g if len(g[v]) > 0), None)

    if inicio is None:
        return []

    pilha = [inicio]
    caminho = []

    while pilha:
        v = pilha[-1]

        if g[v]:
            u = g[v].pop()
            g[u].remove(v)   # remove a aresta inversa
            pilha.append(u)
        else:
            caminho.append(pilha.pop())

    return caminho[::-1]


if __name__ == "__main__":
    # Grafo exemplo NÃO direcionado com caminho euleriano
    grafo_exemplo = {
        '1': ['2', '3'],
        '2': ['1', '3', '4', '5'],
        '3': ['1', '2', '4', '6'],
        '4': ['2', '3', '5', '6'],
        '5': ['2', '4', '6', '7'],
        '6': ['3', '4', '5', '7'],
        '7': ['5', '6']
    }

    print("=== Hierholzer (CAMINHOS — NÃO DIRECIONADO) ===")
    print("Grafo:", grafo_exemplo)

    # ===== Verificação antes de executar =====
    if not verifica_caminho_euleriano(grafo_exemplo):
        print("ERRO: O grafo NÃO possui caminho euleriano.")
    else:
        caminho = hierholzer_caminho(grafo_exemplo)
        print("Caminho Euleriano Encontrado:", caminho)
