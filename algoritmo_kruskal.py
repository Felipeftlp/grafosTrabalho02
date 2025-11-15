"""
Algoritmo de Kruskal para Árvore Geradora Mínima (AGM)

Complexidade: O(m log m)
"""


class UnionFind:
    """
    Estrutura de dados Union-Find (Disjoint Set) para detectar ciclos.
    
    Utiliza compressão de caminho e união por rank para otimização.
    """
    
    def __init__(self, vertices):
        """
        Inicializa a estrutura Union-Find.
        
        Args:
            vertices: Lista ou conjunto de vértices do grafo
        """
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v):
        """
        Encontra o representante (raiz) do conjunto que contém v.
        Usa compressão de caminho para otimização.
        
        Args:
            v: Vértice a ser buscado
            
        Returns:
            Representante do conjunto que contém v
        """
        if self.pai[v] != v:
            self.pai[v] = self.find(self.pai[v])  # Compressão de caminho
        return self.pai[v]
    
    def union(self, u, v):
        """
        Une os conjuntos que contêm u e v.
        Usa união por rank para manter a árvore balanceada.
        
        Args:
            u: Primeiro vértice
            v: Segundo vértice
            
        Returns:
            True se os conjuntos foram unidos, False se já estavam no mesmo conjunto
        """
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        
        if raiz_u == raiz_v:
            return False  # Já estão no mesmo conjunto (formaria ciclo)
        
        # União por rank
        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.pai[raiz_u] = raiz_v
        elif self.rank[raiz_u] > self.rank[raiz_v]:
            self.pai[raiz_v] = raiz_u
        else:
            self.pai[raiz_v] = raiz_u
            self.rank[raiz_u] += 1
        
        return True


def kruskal(grafo, vertices=None):
    """
    Implementa o Algoritmo de Kruskal para encontrar a AGM.
    
    Algoritmo:
    1. Ordena todas as arestas por peso crescente
    2. Para cada aresta (u, v, peso) na ordem:
       - Se u e v não estão no mesmo conjunto (não forma ciclo):
         - Adiciona a aresta na AGM
         - Une os conjuntos de u e v
    3. Para quando tiver n-1 arestas (árvore completa)
    
    Args:
        grafo: Dicionário {u: {v: peso}} representando o grafo
        vertices: Lista opcional de vértices. Se None, extrai do grafo
        
    Returns:
        Tupla (arestas_agm, custo_total) onde:
        - arestas_agm: Lista de tuplas (u, v, peso) da AGM
        - custo_total: Soma dos pesos das arestas da AGM
    """
    # Extrai vértices se não fornecidos
    if vertices is None:
        vertices = set(grafo.keys())
        for u in grafo:
            vertices.update(grafo[u].keys())
    
    vertices = list(vertices)
    n = len(vertices)
    
    # Caso especial: grafo vazio ou com um vértice
    if n <= 1:
        return [], 0
    
    # Extrai todas as arestas do grafo
    arestas = []
    for u in grafo:
        for v, peso in grafo[u].items():
            # Para grafos não direcionados, evita duplicatas (u,v) e (v,u)
            # Adiciona apenas se u < v ou se o grafo é direcionado
            arestas.append((u, v, peso))
    
    # Remove arestas duplicadas em grafos não direcionados
    # (considera apenas uma direção de cada aresta)
    arestas_unicas = {}
    for u, v, peso in arestas:
        chave = tuple(sorted([u, v]))
        if chave not in arestas_unicas:
            arestas_unicas[chave] = peso
        else:
            # Mantém a aresta com menor peso se houver múltiplas
            arestas_unicas[chave] = min(arestas_unicas[chave], peso)
    
    arestas = [(u, v, peso) for (u, v), peso in arestas_unicas.items()]
    
    # Passo 1: Ordena as arestas por peso (ordem crescente)
    arestas.sort(key=lambda x: x[2])
    
    # Inicializa Union-Find
    uf = UnionFind(vertices)
    
    # Passo 2: Seleciona arestas que não formam ciclo
    agm = []
    custo_total = 0
    
    for u, v, peso in arestas:
        # Se u e v estão em conjuntos diferentes, não forma ciclo
        if uf.union(u, v):
            agm.append((u, v, peso))
            custo_total += peso
            
            # Para quando tiver n-1 arestas (árvore completa)
            if len(agm) == n - 1:
                break
    
    return agm, custo_total


def kruskal_direcionado(grafo, vertices=None):
    """
    Versão do Kruskal que trata o grafo direcionado como não direcionado.
    
    Para AGM, a direção das arestas não importa. Esta função converte
    o grafo direcionado em não direcionado antes de aplicar Kruskal.
    
    Args:
        grafo: Dicionário {u: {v: peso}} representando o grafo direcionado
        vertices: Lista opcional de vértices. Se None, extrai do grafo
        
    Returns:
        Tupla (arestas_agm, custo_total) onde:
        - arestas_agm: Lista de tuplas (u, v, peso) da AGM
        - custo_total: Soma dos pesos das arestas da AGM
    """
    # Converte para grafo não direcionado
    grafo_nd = {}
    
    for u in grafo:
        if u not in grafo_nd:
            grafo_nd[u] = {}
        for v, peso in grafo[u].items():
            # Adiciona aresta em ambas as direções
            if u not in grafo_nd:
                grafo_nd[u] = {}
            if v not in grafo_nd:
                grafo_nd[v] = {}
            
            # Mantém o menor peso se houver múltiplas arestas
            if v not in grafo_nd[u]:
                grafo_nd[u][v] = peso
            else:
                grafo_nd[u][v] = min(grafo_nd[u][v], peso)
            
            if u not in grafo_nd[v]:
                grafo_nd[v][u] = peso
            else:
                grafo_nd[v][u] = min(grafo_nd[v][u], peso)
    
    return kruskal(grafo_nd, vertices)


def formatar_resultado(arestas_agm, custo_total):
    """
    Formata o resultado da AGM para exibição.
    
    Args:
        arestas_agm: Lista de tuplas (u, v, peso)
        custo_total: Custo total da AGM
        
    Returns:
        String formatada com o resultado
    """
    resultado = "Árvore Geradora Mínima (Kruskal)\n"
    # resultado += "-" * 40 + "\n"
    
    if not arestas_agm:
        resultado += "Grafo vazio ou desconexo\n"
    else:
        resultado += f"Arestas na AGM ({len(arestas_agm)}):\n"
        for u, v, peso in sorted(arestas_agm, key=lambda x: x[2]):
            resultado += f"  ({u}, {v}) - Peso: {peso}\n"
        resultado += f"\nCusto Total: {custo_total}\n"
    
    return resultado


if __name__ == "__main__":
    from grafos import grafo_direcionado, TODOS_NOS
    
    print("KRUSKAL")
    print()
    print("Grafo do Trabalho: Direcionado e Ponderado (19 vértices)")
    print("Requisito: s=1 (vértice inicial)")
    print()
    
    # Executa Kruskal no grafo do trabalho
    arestas_agm, custo_total = kruskal_direcionado(grafo_direcionado, TODOS_NOS)
    
    # Exibe resultado
    print(formatar_resultado(arestas_agm, custo_total))
    
    # Informações adicionais
    print("\nInformações Adicionais:")
    print(f"  Número de vértices: {len(TODOS_NOS)}")
    print(f"  Número de arestas na AGM: {len(arestas_agm)}")
    print(f"  Número esperado (n-1): {len(TODOS_NOS) - 1}")
    
    if len(arestas_agm) < len(TODOS_NOS) - 1:
        print("AVISO: O grafo pode estar desconexo!")
