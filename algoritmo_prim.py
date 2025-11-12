"""
Este arquivo implementa o Algoritmo de Prim para encontrar a
Árvore Geradora Mínima (AGM) de um grafo.
"""

import math
# Importa o grafo e a lista de nós do outro arquivo
from grafos import grafo_direcionado, TODOS_NOS

def _adicionar_aresta_nao_direcionada(grafo_nd, u, v, peso):
    """
    Função auxiliar para adicionar uma aresta a um grafo não direcionado.
    
    Ela verifica se uma aresta entre 'u' e 'v' já existe e, em caso afirmativo,
    mantém apenas a aresta de menor peso.

    Entrada:
    - grafo_nd (dict): O grafo não direcionado sendo construído.
    - u (int): Nó de origem.
    - v (int): Nó de destino.
    - peso (int/float): O peso da aresta (u, v).
    """
    # Adiciona a aresta (u, v)
    if v not in grafo_nd[u] or peso < grafo_nd[u][v]:
        grafo_nd[u][v] = peso
        
    # Adiciona a aresta (v, u)
    if u not in grafo_nd[v] or peso < grafo_nd[v][u]:
        grafo_nd[v][u] = peso

def criar_grafo_nao_direcionado(grafo_dir, nos):
    """
    Converte o grafo direcionado importado em um grafo não direcionado.

    Entrada:
    - grafo_dir (dict): O grafo direcionado original.
    - nos (set): Um conjunto com todos os números de nós (ex: 1 a 19).

    Saída:
    - (dict): Uma representação de lista de adjacência de um grafo
              não direcionado, pronto para o Algoritmo de Prim.
    """
    # Inicializa o grafo não direcionado com todos os nós
    grafo_nd = {no: {} for no in nos}
    
    # Itera sobre todas as arestas do grafo direcionado
    for u, vizinhos in grafo_dir.items():
        for v, peso in vizinhos.items():
            # Adiciona a aresta nos dois sentidos (u,v) e (v,u)
            _adicionar_aresta_nao_direcionada(grafo_nd, u, v, peso)
            
    return grafo_nd

def algoritmo_prim(grafo_nd, no_inicial):
    """
    Executa o Algoritmo de Prim (implementação clássica, O(N^2)).

    Segue o pseudocódigo:
    Z = nós na árvore
    N = nós fora da árvore
    A cada passo, encontra a aresta (j, k) de peso mínimo
    tal que j está em Z e k está em N.

    Entrada:
    - grafo_nd (dict): O grafo NÃO DIRECIONADO.
    - no_inicial (int): O nó onde o algoritmo deve começar (raiz da árvore).

    Saída:
    - (list): Uma lista de tuplas, onde cada tupla representa uma aresta
              na AGM no formato (peso, nó_origem, nó_destino).
    - (float/int): O custo total da AGM.
    """
    
    # T ← ∅ (Arestas da árvore final)
    agm_arestas = []
    custo_total = 0
    
    # Z ← {i} (Z = nós_visitados)
    nos_visitados = {no_inicial}
    
    # N ← V \ {i} (N = nos_nao_visitados)
    nos_nao_visitados = set(grafo_nd.keys()) - nos_visitados

    # Enquanto N.tamanho > 0 faça
    while nos_nao_visitados:
        
        # ---
        # Início: "Encontrar a aresta (j,k)∈V tal que j∈Z, k∈N e d_jk é mínimo"
        # ---
        peso_minimo = math.inf
        melhor_aresta = None  # Vai guardar (peso, j, k)

        # Para cada nó 'j' que está em Z (nos_visitados)
        for j in nos_visitados:
            # Para cada vizinho 'k' do nó 'j'
            for k, peso in grafo_nd[j].items():
                
                # Verifica se 'k' está em N (nos_nao_visitados)
                if k in nos_nao_visitados:
                    
                    # Se a aresta (j, k) é a mais barata encontrada ATÉ AGORA
                    if peso < peso_minimo:
                        peso_minimo = peso
                        melhor_aresta = (peso, j, k)
        # ---
        # Fim: "Encontrar a aresta..."
        # ---
        
        # Se não encontramos nenhuma aresta, o grafo é desconexo.
        if melhor_aresta is None:
            break  # Sai do loop 'while'

        # Encontramos a aresta mínima!
        (peso, j, k) = melhor_aresta
        
        # Z ← Z ∪ {k}
        nos_visitados.add(k)
        
        # N ← N \ {k}
        nos_nao_visitados.remove(k)
        
        # T ← T ∪ (j,k)
        agm_arestas.append((peso, j, k))
        custo_total += peso

    # 9. Verifica se o grafo era conexo
    if nos_nao_visitados: # Se sobraram nós em N
        print(f"\nAviso: O grafo pode não ser conexo.")
        print(f"A AGM foi gerada para {len(nos_visitados)} nós alcançáveis.")
        
    return agm_arestas, custo_total

# --- 
# --- FUNÇÃO DE DESENHO ---
# --- 
def exibir_agm_desenhada(agm_arestas, nos_totais, no_raiz):
    """
    Desenha a Árvore Geradora Mínima (AGM) no terminal de forma hierárquica.

    Entrada:
    - agm_arestas (list): A lista de arestas ((peso, u, v)) retornada por Prim.
    - nos_totais (set): O conjunto de todos os nós no grafo.
    - no_raiz (int): O nó que foi usado como início (s=1).
    """
    
    print(f"\n🌳 Desenho da Árvore Geradora Mínima (raiz={no_raiz}) 🌳")
    
    # 1. Constrói uma lista de adjacência (mapa) APENAS da AGM
    mst_adj = {no: [] for no in nos_totais}
    for peso, u, v in agm_arestas:
        mst_adj[u].append((v, peso))
        mst_adj[v].append((u, peso))

    # 2. Define um conjunto de 'visitados' para a DFS
    visitados = set()

    def _dfs_desenho(no_atual, prefixo):
        """
        Função auxiliar recursiva (DFS) para desenhar a árvore.
        """
        visitados.add(no_atual)
        
        # 3. Encontra os "filhos" do nó atual
        filhos = []
        for vizinho, peso in mst_adj[no_atual]:
            if vizinho not in visitados:
                filhos.append((vizinho, peso))
        filhos.sort()
        
        # 4. Itera sobre os filhos para desenhar
        total_filhos = len(filhos)
        for i, (filho, peso) in enumerate(filhos):
            eh_ultimo = (i == total_filhos - 1)
            conector = "└── " if eh_ultimo else "├── "
            print(f"{prefixo}{conector}{filho} (peso: {peso})")
            
            # 5. Prepara o prefixo para a próxima chamada recursiva
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            _dfs_desenho(filho, novo_prefixo)

    # 6. Inicia o desenho
    print(f"{no_raiz} (Raiz)")
    _dfs_desenho(no_raiz, "")
    print("-------------------------------------------------")


# --- Bloco de Execução Principal (Sem alteração) ---
if __name__ == "__main__":
    
    print("Iniciando o processo da Árvore Geradora Mínima (AGM)...")
    
    # 1. Converter o grafo direcionado para não direcionado
    print("Convertendo grafo direcionado para não direcionado...")
    grafo_nd = criar_grafo_nao_direcionado(grafo_direcionado, TODOS_NOS)

    # 2. Definir o nó inicial (s=1)
    no_de_inicio = 1
    print(f"Executando o Algoritmo de Prim (Versão Clássica) começando pelo nó {no_de_inicio}...")

    # 3. Executar o algoritmo
    agm_final, custo_final = algoritmo_prim(grafo_nd, no_de_inicio)
    
    # 4. Exibir os resultados (Lista Simples)
    print("\n--- Árvore Geradora Mínima (AGM) Encontrada ---")
    print("\nArestas (Formato: (Peso, Nó A, Nó B)):")
    for aresta in agm_final:
        # Formata para (peso, u, v)
        print(f"  {aresta}")
        
    print("\n-------------------------------------------------")
    print(f"Custo Total da AGM: {custo_final}")
    print(f"Total de Arestas na AGM: {len(agm_final)}")
    print("-------------------------------------------------")

    # 5. Exibir os resultados (Desenho da Árvore)
    exibir_agm_desenhada(agm_final, TODOS_NOS, no_de_inicio)