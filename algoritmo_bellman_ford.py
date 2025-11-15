"""
Algoritmo de Bellman-Ford para Caminho Mais Curto

Implementação do algoritmo de Bellman-Ford (1956-58) que encontra o caminho
mais curto de um vértice origem para todos os demais vértices do grafo.

Permite arestas com peso negativo e detecta ciclos de peso negativo.

Complexidade: O(|V| * |E|) onde V é o conjunto de vértices e E é o conjunto de arestas.

Autor: Ianco
"""


def bellman_ford(grafo, origem, vertices=None):
    """
    Implementa o Algoritmo de Bellman-Ford para encontrar caminhos mais curtos.
    
    Algoritmo:
    1. Inicialização: distância[origem] = 0, distância[v] = ∞ para outros vértices
    2. Relaxamento: Para cada vértice (|V|-1 vezes):
       - Para cada aresta (u, v, peso):
         - Se distância[v] > distância[u] + peso:
           - distância[v] = distância[u] + peso
           - predecessor[v] = u
    3. Detecção de ciclo negativo:
       - Para cada aresta (u, v, peso):
         - Se distância[v] > distância[u] + peso: existe ciclo negativo
    
    Args:
        grafo: Dicionário {u: {v: peso}} representando o grafo direcionado
        origem: Vértice de origem para calcular os caminhos
        vertices: Lista opcional de vértices. Se None, extrai do grafo
        
    Returns:
        Tupla (distancias, predecessores, tem_ciclo_negativo) onde:
        - distancias: Dicionário {v: distância} com as menores distâncias
        - predecessores: Dicionário {v: predecessor} para reconstruir caminhos
        - tem_ciclo_negativo: True se existe ciclo de peso negativo acessível da origem
    """
    # Extrai vértices se não fornecidos
    if vertices is None:
        vertices = set(grafo.keys())
        for u in grafo:
            vertices.update(grafo[u].keys())
    
    vertices = list(vertices)
    n = len(vertices)
    
    # Passo 1: Inicialização
    distancias = {v: float('inf') for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[origem] = 0
    
    # Extrai todas as arestas
    arestas = []
    for u in grafo:
        for v, peso in grafo[u].items():
            arestas.append((u, v, peso))
    
    # Passo 2: Relaxamento das arestas (|V| - 1 iterações)
    for i in range(n - 1):
        atualizado = False  # Flag para otimização: parar se não houver mudanças
        
        for u, v, peso in arestas:
            # Relaxamento: verifica se passar por u melhora o caminho para v
            if distancias[u] != float('inf') and distancias[v] > distancias[u] + peso:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u
                atualizado = True
        
        # Otimização: se não houve atualização, já convergiu
        if not atualizado:
            break
    
    # Passo 3: Detecção de ciclo negativo
    tem_ciclo_negativo = False
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[v] > distancias[u] + peso:
            tem_ciclo_negativo = True
            break
    
    return distancias, predecessores, tem_ciclo_negativo


def reconstruir_caminho(predecessores, origem, destino):
    """
    Reconstrói o caminho da origem ao destino usando o vetor de predecessores.
    
    Args:
        predecessores: Dicionário {v: predecessor} retornado pelo Bellman-Ford
        origem: Vértice de origem
        destino: Vértice de destino
        
    Returns:
        Lista de vértices representando o caminho, ou None se não existe caminho
    """
    if predecessores[destino] is None and destino != origem:
        return None  # Não existe caminho
    
    caminho = []
    atual = destino
    
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    
    caminho.reverse()
    
    # Verifica se o caminho começa na origem
    if caminho[0] != origem:
        return None
    
    return caminho


def formatar_resultado(origem, distancias, predecessores, tem_ciclo_negativo, destino=None):
    """
    Formata o resultado do Bellman-Ford para exibição.
    
    Args:
        origem: Vértice de origem
        distancias: Dicionário com as distâncias
        predecessores: Dicionário com os predecessores
        tem_ciclo_negativo: Booleano indicando se há ciclo negativo
        destino: Vértice de destino opcional (para mostrar caminho específico)
        
    Returns:
        String formatada com o resultado
    """
    resultado = ""
    if tem_ciclo_negativo:
        resultado += "AVISO: Ciclo de peso negativo detectado!\n"
        resultado += "As distâncias podem não estar bem definidas.\n\n"
    
    # Se foi especificado um destino, mostra apenas esse caminho
    if destino is not None:
        if distancias[destino] == float('inf'):
            resultado += f"Não existe caminho de {origem} para {destino}\n"
        else:
            caminho = reconstruir_caminho(predecessores, origem, destino)
            resultado += f"  Distância: {distancias[destino]}\n"
            if caminho:
                resultado += f"  Caminho: {' -> '.join(map(str, caminho))}\n"
    else:
        resultado += "\n"
        
        vertices_com_dist_ordenadas = sorted(distancias.keys(), 
                                   key=lambda x: (distancias[x], str(x)))
        
        for v in vertices_com_dist_ordenadas:
            if v == origem:
                resultado += f"{v}: 0 (origem)\n"
            elif distancias[v] == float('inf'):
                resultado += f"Destino: {v}:\t| Distância: inf | Caminho: inacessível\n"
            else:
                caminho = reconstruir_caminho(predecessores, origem, v)
                caminho_str = ' -> '.join(map(str, caminho)) if caminho else "?"
                resultado += f"Destino: {v}:\t| Distância: {distancias[v]}\t| Caminho: {caminho_str}\n"
    
    return resultado


if __name__ == "__main__":
    from grafos import grafo_direcionado, TODOS_NOS
    
    print("BELLMAN-FORD")
    origem = 1
    destino = 15
    print(f"Origem={origem}, Destino={destino}")
    print()
    
    
    # Executa Bellman-Ford
    distancias, predecessores, tem_ciclo_negativo = bellman_ford(
        grafo_direcionado, origem, TODOS_NOS
    )
    
    # Exibe resultado completo (todas as distâncias)
    print("." * 20)
    print(f"TODAS AS DISTÂNCIAS A PARTIR DO VÉRTICE {origem}:")
    print(formatar_resultado(origem, distancias, predecessores, tem_ciclo_negativo))
    print("." * 20)
    
    # Exibe resultado específico para o destino 15
    print("." * 20)
    print(f"CAMINHO ESPECÍFICO DE {origem} PARA O VÉRTICE {destino}:")
    print(formatar_resultado(origem, distancias, predecessores, tem_ciclo_negativo, destino))
    print("." * 20)
