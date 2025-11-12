"""
Implementa o Algoritmo de Dijkstra para encontrar o caminho mais curto
a partir de um nó de origem (s).

A saída está configurada para focar no caminho de (s=1) para (fim=15).
"""

import math
# Importa o grafo e a lista de nós
from grafos import grafo_direcionado, TODOS_NOS

def _encontrar_proximo_no_classico(distancias, visitados):
    """
    Função auxiliar que implementa o Passo 5:
    "Seja x um vértice não visitado com menor x.distância"

    Entrada:
    - distancias (dict): Dicionário de distâncias atuais.
    - visitados (dict): Dicionário de status de visita (True/False).

    Saída:
    - (int/None): O nó não visitado com a menor distância, ou None
                  se todos os nós restantes forem inalcançáveis.
    """
    dist_minima = math.inf
    proximo_no = None
    
    # Itera sobre TODOS os nós
    for no, foi_visitado in visitados.items():
        # "um vértice u com u.visitado==0"
        if not foi_visitado:
            # "com menor x.distância"
            if distancias[no] < dist_minima:
                dist_minima = distancias[no]
                proximo_no = no
                
    return proximo_no

def algoritmo_dijkstra(grafo, todos_nos, no_inicial):
    """
    Executa o Algoritmo de Dijkstra seguindo o pseudocódigo fornecido.

    Entrada:
    - grafo (dict): O grafo direcionado (lista de adjacência).
    - todos_nos (set): Um conjunto com todos os nós (ex: 1 a 19).
    - no_inicial (int): O nó de origem (s).

    Saída:
    - (dict): Dicionário de distâncias mínimas {no: distancia}.
    - (dict): Dicionário de predecessores {no: predecessor}.
    """
    
    # --- Início da Inicialização (Passos 1-4) ---
    
    # "Para todo vértice v ∈ V faça v.visitado = 0;"
    visitados = {no: False for no in todos_nos}
    
    # "Se v ∈ N+(s) ... Senão ... v.distância = INF;"
    distancias = {}
    predecessores = {}
    
    for v in todos_nos:
        # "Se v ∈ N+(s) faça" (Verifica se 'v' é vizinho de 's')
        if v in grafo.get(no_inicial, {}):
            # "v.predecessor = s;"
            predecessores[v] = no_inicial
            # "v.distância = w(sv);"
            distancias[v] = grafo[no_inicial][v]
        else:
            # "Senão v.predecessor = NULL; v.distância = INF;"
            predecessores[v] = None
            distancias[v] = math.inf

    # "s.distância= 0;"
    distancias[no_inicial] = 0
    
    # --- Fim da Inicialização ---

    # --- Início do Loop Principal (Passos 5-7) ---
    
    # "Enquanto houver vértice u com u.visitado==0 faça"
    while True:
        
        # "Seja x um vértice não visitado com menor x.distância"
        x = _encontrar_proximo_no_classico(distancias, visitados)
        
        if x is None or distancias[x] == math.inf:
            break
            
        # "x.visitado = 1;"
        visitados[x] = True
        
        # "Para todo vértice y∈N+(x) faça"
        if x in grafo:
            for y, peso_xy in grafo[x].items():
                
                # "Se y.visitado==0 então"
                if not visitados[y]:
                    
                    # "Se y.distância > x.distância + w(xy) então"
                    nova_distancia = distancias[x] + peso_xy
                    if distancias[y] > nova_distancia:
                        
                        # "y.distância = x.distância + w(xy)"
                        distancias[y] = nova_distancia
                        # "y.predecessor = x;"
                        predecessores[y] = x
                        
    return distancias, predecessores

def reconstruir_caminho(predecessores, no_inicial, no_final):
    """
    Função auxiliar para montar o caminho a partir do dicionário
    de predecessores.
    
    Saída:
    - (list): Lista de nós do 'no_inicial' ao 'no_final'.
    - (None): Se o caminho não for encontrado.
    """
    caminho = []
    atual = no_final
    
    if predecessores.get(atual) is None and atual != no_inicial:
        return None
        
    while atual is not None:
        caminho.append(atual)
        atual = predecessores.get(atual)

    if caminho[-1] != no_inicial:
        return None
        
    return caminho[::-1]


# --- Bloco de Execução Principal  ---
if __name__ == "__main__":
    
    no_de_inicio = 1
    no_de_fim = 15
    
    print(f"Executando Dijkstra (Versão Clássica)...")
    print(f"Buscando o caminho mais curto de (s={no_de_inicio}) para (fim={no_de_fim})...")
    
    # 1. Executa o algoritmo
    # O algoritmo sempre calcula de 's' para TODOS os nós
    dist, pred = algoritmo_dijkstra(grafo_direcionado, TODOS_NOS, no_de_inicio)
    
    print("\n--- 🏁 Resultado do Caminho Mais Curto ---")
    
    # 2. Pega os resultados específicos para o 'no_de_fim'
    distancia_final = dist[no_de_fim]
    caminho_final = reconstruir_caminho(pred, no_de_inicio, no_de_fim)
    
    # 3. Exibe o resultado específico
    if distancia_final == math.inf or caminho_final is None:
        print(f"  Origem:  {no_de_inicio}")
        print(f"  Destino: {no_de_fim}")
        print(f"  Custo:   ∞ (Inalcançável)")
        print(f"  Caminho: Nenhum caminho encontrado.")
    else:
        # Formata o caminho como "1 -> 11 -> ..."
        
        caminho_str = " -> ".join(map(str, caminho_final))
        print(f"  Origem:  {no_de_inicio}")
        print(f"  Destino: {no_de_fim}")
        print(f"  Custo:   {distancia_final}")
        print(f"  Caminho: {caminho_str}")