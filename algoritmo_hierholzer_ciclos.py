"""
Implementação do Algoritmo de Hierholzer para encontrar CICLOS eulerianos.
Entrada: grafo representado como dicionário {vertice: [lista_de_vizinhos]}
Saída: lista com o ciclo euleriano.
"""

from collections import defaultdict


def verifica_ciclo_euleriano(grafo):
    """
    Verifica se o grafo direcionado possui um CICLO euleriano.
    Condições:
    - Todo vértice deve ter grau-in == grau-out
    - Todos vértices com arestas devem estar no mesmo componente conectado (ignorado aqui
      pois o trabalho usa grafos pequenos e totalmente conectados)
    """
    grau_in = defaultdict(int)
    grau_out = defaultdict(int)

    for u in grafo:
        for v in grafo[u]:
            grau_out[u] += 1
            grau_in[v] += 1

    vertices = set(list(grau_in.keys()) + list(grau_out.keys()))

    for v in vertices:
        if grau_in[v] != grau_out[v]:
            return False

    return True


def hierholzer_ciclo(grafo):
    """
    Encontra um ciclo euleriano completo caso exista.
    """
    g = {u: vizinhos[:] for u, vizinhos in grafo.items()}

    inicio = next((v for v in g if len(g[v]) > 0), None)
    if inicio is None:
        return []

    caminho = []
    pilha = [inicio]

    while pilha:
        v = pilha[-1]

        if g[v]:
            u = g[v].pop()
            pilha.append(u)
        else:
            caminho.append(pilha.pop())

    return caminho[::-1]


if __name__ == "__main__":
    # Grafo exemplo
    grafo_exemplo = {
        'A': ['B', 'F'],
        'B': ['A', 'D'],
        'C': ['B'],
        'D': ['B', 'C'],
        'E': ['A', 'D'],
        'F': ['E']
    }

    print("=== Hierholzer (CICLOS) ===")
    print("Grafo:", grafo_exemplo)

    # === Verificação antes de rodar ===
    if not verifica_ciclo_euleriano(grafo_exemplo):
        print("ERRO: O grafo NÃO possui ciclo euleriano.")
    else:
        ciclo = hierholzer_ciclo(grafo_exemplo)
        print("Ciclo Euleriano Encontrado:", ciclo)
