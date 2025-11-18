import math

def gerar_matriz_pesos(grafo, vertices):
    N = len(vertices)

    matriz_pesos = [[math.inf for _ in range(N)] for _ in range(N)]

    for u in vertices:
        if u in grafo:
            for v, w in grafo[u].items():
                matriz_pesos[u - 1][v - 1] = w
                matriz_pesos[v - 1][u - 1] = w
    
    return matriz_pesos


class Boruvka:

    def __init__(self, vertices, matriz_pesos):
        self.vertices = vertices
        self.matriz = matriz_pesos

        self.pai = {v: v for v in vertices}

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, a, b):
        raiz_a = self.encontrar(a)
        raiz_b = self.encontrar(b)
        if raiz_a != raiz_b:
            self.pai[raiz_b] = raiz_a

    def executar(self):
        florestas = len(self.vertices)
        agm = []

        while florestas > 1:
            menor_aresta = {}

            for u in self.vertices:
                u_idx = u - 1
                for v in self.vertices:
                    if u == v:
                        continue

                    v_idx = v - 1
                    peso = self.matriz[u_idx][v_idx]

                    if peso == math.inf:
                        continue

                    raiz_u = self.encontrar(u)
                    raiz_v = self.encontrar(v)

                    if raiz_u != raiz_v:
                        if raiz_u not in menor_aresta or menor_aresta[raiz_u][2] > peso:
                            menor_aresta[raiz_u] = (u, v, peso)

            for raiz, (u, v, peso) in menor_aresta.items():
                if self.encontrar(u) != self.encontrar(v):
                    agm.append((u, v, peso))
                    self.unir(u, v)
                    florestas -= 1

        return agm
    

def exibir_agm_desenhada_boruvka(agm_arestas, nos_totais, no_raiz, peso_total):
    """
    Desenha a Árvore Geradora Mínima (AGM) no terminal de forma hierárquica.
    Adaptado para Borůvka, onde as arestas vêm no formato (u, v, peso).

    Parâmetros:
    - agm_arestas: lista de arestas no formato (u, v, peso)
    - nos_totais: conjunto com todos os nós do grafo
    - no_raiz: nó inicial para desenhar a árvore
    - peso_total: peso total da AGM
    """

    print(f"\n🌳 Árvore Geradora Mínima (Borůvka) — raiz={no_raiz} 🌳")
    print(f"📌 Peso total da AGM = {peso_total}\n")

    # Construir adjacência da MST
    mst_adj = {no: [] for no in nos_totais}
    for u, v, peso in agm_arestas:
        mst_adj[u].append((v, peso))
        mst_adj[v].append((u, peso))

    visitados = set()

    def _dfs_desenho(no_atual, prefixo):
        visitados.add(no_atual)

        filhos = [(viz, peso) for viz, peso in mst_adj[no_atual] if viz not in visitados]
        filhos.sort(key=lambda x: x[0])

        total = len(filhos)
        for i, (filho, peso) in enumerate(filhos):
            ultimo = (i == total - 1)
            conector = "└── " if ultimo else "├── "
            print(f"{prefixo}{conector}{filho} (peso: {peso})")

            novo_prefixo = prefixo + ("    " if ultimo else "│   ")
            _dfs_desenho(filho, novo_prefixo)

    # Começa o desenho
    print(f"{no_raiz} (Raiz)")
    _dfs_desenho(no_raiz, "")
    print("-------------------------------------------------\n")


if __name__ == "__main__":
    from grafos import grafo_direcionado, TODOS_NOS
    
    print("Grafo do Trabalho: Direcionado e Ponderado (19 vértices)")
    print("Requisito: s=1 (vértice inicial)")
    print()
    
    matriz_pesos = gerar_matriz_pesos(grafo_direcionado, TODOS_NOS)
    
    alg = Boruvka(TODOS_NOS, matriz_pesos)
    agm_final = alg.executar()
    
    no_raiz = 1
    
    peso_total = sum(p for _, _, p in agm_final)

    exibir_agm_desenhada_boruvka(agm_final, TODOS_NOS, no_raiz, peso_total)
    
    