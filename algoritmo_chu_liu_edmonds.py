from grafos import grafo_direcionado_2, TODOS_NOS_2

def find_cycle(predecessors, num_nodes, root):
    """
    Encontra um ciclo no grafo de predecessores usando busca.
    'predecessors' é um dict {v: u} significando u -> v.
    Retorna uma lista de nós no ciclo, ou None se nenhum ciclo for encontrado.
    """
    visited_globally = [False] * num_nodes
    
    for i in range(num_nodes):
        if i == root or visited_globally[i]:
            continue
            
        path = []       # Nós no caminho atual
        path_set = set() # Nós no caminho atual (para busca rápida)
        curr = i
        
        # Segue a cadeia de predecessores
        while curr != -1 and not visited_globally[curr]:
            if curr == root:
                break
                
            if curr in path_set:
                # Ciclo encontrado! Retorna os nós do ciclo.
                cycle_start_index = path.index(curr)
                return path[cycle_start_index:]
            
            path.append(curr)
            path_set.add(curr)
            
            if curr not in predecessors:
                break  # Chegou a um nó sem aresta de entrada
                
            curr = predecessors[curr]
        
        # Marca todos os nós neste caminho como visitados globalmente
        # (eles levam à raiz ou a um ciclo já processado)
        for node in path:
            visited_globally[node] = True
            
    return None # Nenhum ciclo encontrado

def chu_liu_edmonds(edges, num_nodes, root):
    """
    Implementa o algoritmo de Chu-Liu/Edmonds para encontrar a
    arborescência de custo mínimo (MST em grafo dirigido).

    :param edges: Lista de tuplas (u, v, weight) representando arestas dirigidas.
    :param num_nodes: Número total de nós (inteiros de 0 a num_nodes-1).
    :param root: O nó raiz.
    :return: Uma tupla (custo_total, lista_de_arestas_da_mst)
    """

    # --- 1. Selecionar Arestas de Entrada de Custo Mínimo ---
    
    # min_in_edges: armazena a aresta de menor peso para cada nó {v: (u, v, w)}
    min_in_edges = {}
    # predecessors: apenas para detecção de ciclo {v: u}
    predecessors = {}
    cost = 0

    for v in range(num_nodes):
        if v == root:
            continue
            
        min_edge = None
        min_weight = float('inf')
        
        for u_edge, v_edge, w_edge in edges:
            if v_edge == v and w_edge < min_weight:
                min_weight = w_edge
                min_edge = (u_edge, v_edge, w_edge)
        
        if min_edge:
            min_in_edges[v] = min_edge
            predecessors[v] = min_edge[0] # u
            cost += min_weight

    # --- 2. Verificar Ciclos ---
    cycle = find_cycle(predecessors, num_nodes, root)
    
    # --- 3. Caso Base: Sem Ciclos ---
    # Se não houver ciclo, a seleção atual de arestas mínimas é a MST.
    if not cycle:
        return (cost, list(min_in_edges.values()))

    # --- 4. Contratar o Ciclo ---
    cycle_nodes = set(cycle)
    
    # Custo total das arestas *dentro* do ciclo (que já somamos em 'cost')
    cycle_cost = 0
    # Mapeia {v: (u, v, w)} para arestas *dentro* do ciclo
    cycle_in_edges = {} 
    
    for v in cycle:
        edge = min_in_edges[v] # (u, v, w) onde u também está no ciclo
        cycle_cost += edge[2]
        cycle_in_edges[v] = edge

    # Criar um novo "supernó" para representar o ciclo contraído.
    # Usaremos 'num_nodes' como o ID do supernó.
    supernode_id = num_nodes 
    
    # --- 5. Criar Novo Grafo Contraído ---
    new_edges = []
    
    # Mapeia arestas contraídas de volta para suas arestas originais
    # (new_u, new_v, new_w) -> (orig_u, orig_v, orig_w)
    contracted_edge_map = {} 

    for u, v, w in edges:
        u_in_cycle = u in cycle_nodes
        v_in_cycle = v in cycle_nodes

        # Ignora arestas totalmente internas ao ciclo
        if u_in_cycle and v_in_cycle:
            continue
        
        # Mapeia nós para o supernó, se aplicável
        u_new = supernode_id if u_in_cycle else u
        v_new = supernode_id if v_in_cycle else v

        # Ignora auto-loops no supernó
        if u_new == v_new:
            continue
            
        if v_new == supernode_id:
            # Aresta (u, v) entrando no ciclo.
            # Devemos recalcular o peso.
            # w_in_cycle é o peso da aresta *do ciclo* que entra em 'v'
            w_in_cycle = cycle_in_edges[v][2]
            new_weight = w - w_in_cycle
            
            new_edge = (u_new, v_new, new_weight)
            new_edges.append(new_edge)
            contracted_edge_map[new_edge] = (u, v, w) # Mapeia de volta
        else:
            # Aresta saindo do ciclo ou totalmente fora
            new_edge = (u_new, v_new, w)
            new_edges.append(new_edge)
            contracted_edge_map[new_edge] = (u, v, w) # Mapeia de volta

    # --- 6. Chamada Recursiva ---
    
    # Se a raiz estava no ciclo, o supernó se torna a nova raiz
    new_root = supernode_id if root in cycle_nodes else root
    
    # O 'custo' atual (da Etapa 1) inclui o custo do ciclo.
    # A 'recursive_cost' é o custo *adicional* (ou economia)
    # encontrado ao otimizar o grafo contraído.
    
    recursive_cost, recursive_edges = chu_liu_edmonds(
        new_edges, num_nodes + 1, new_root
    )
    
    # Custo total = custo original (etapa 1) + custo da recursão
    total_cost = cost + recursive_cost

    # --- 7. Expandir o Grafo (Reconstruir a Solução) ---
    final_edges = []
    
    # Rastreia qual nó do ciclo foi "entrado" pela solução recursiva
    node_entered_in_cycle = -1

    # Adiciona as arestas escolhidas pela recursão
    for u_rec, v_rec, w_rec in recursive_edges:
        original_edge = contracted_edge_map[(u_rec, v_rec, w_rec)]
        final_edges.append(original_edge)
        
        if v_rec == supernode_id:
            # Esta é a aresta que "quebrou" o ciclo
            # original_edge[1] é o nó 'v' original
            node_entered_in_cycle = original_edge[1]

    # Adiciona as arestas do ciclo original...
    for v_cycle, edge in cycle_in_edges.items():
        # ...exceto aquela que foi substituída pela aresta 'entrante'
        if v_cycle != node_entered_in_cycle:
            final_edges.append(edge)
            
    # Adiciona as arestas da seleção original (Etapa 1) 
    # que NÃO entravam no ciclo
    for v, edge in min_in_edges.items():
        if v not in cycle_nodes:
            final_edges.append(edge)
            
    # Remove duplicatas (caso a lógica de expansão adicione algo já 
    # presente na seleção original, embora isso não deva acontecer
    # se a lógica estiver correta, é mais seguro).
    # A lógica de expansão acima é mais limpa e deve evitar duplicatas.
    
    # Vamos refinar a Etapa 7 para ser mais clara:
    final_edges = []
    node_entered_in_cycle = -1
    
    # 1. Adiciona arestas da solução recursiva (mapeadas de volta)
    for u_rec, v_rec, w_rec in recursive_edges:
        original_edge = contracted_edge_map[(u_rec, v_rec, w_rec)]
        final_edges.append(original_edge)
        if v_rec == supernode_id:
            node_entered_in_cycle = original_edge[1] # O 'v' original

    # 2. Adiciona as arestas do ciclo...
    for v_cycle_node, cycle_edge in cycle_in_edges.items():
        # ... exceto a que entra no mesmo nó que a aresta da recursão
        if v_cycle_node != node_entered_in_cycle:
            final_edges.append(cycle_edge)

    # 3. Adiciona as arestas da seleção original (Etapa 1) que não tocavam o ciclo
    # (Esta etapa é coberta pela recursão, pois essas arestas
    # teriam sido passadas e selecionadas na chamada recursiva)
    # *Correção*: Não, elas não são. Arestas que *não entravam* no ciclo
    # (min_in_edges[v] onde v não está no ciclo) devem ser adicionadas.
    
    # Vamos tentar a Lógica de Expansão 7.C (mais robusta)
    final_edges_set = set()
    node_entered_in_cycle = -1
    
    # Adiciona arestas da solução recursiva
    for u_rec, v_rec, w_rec in recursive_edges:
        original_edge = contracted_edge_map[(u_rec, v_rec, w_rec)]
        final_edges_set.add(original_edge)
        if v_rec == supernode_id:
            node_entered_in_cycle = original_edge[1] # 'v' original
            
    # Adiciona arestas do ciclo
    for v_node, cycle_edge in cycle_in_edges.items():
        final_edges_set.add(cycle_edge)
        
    # Remove a aresta do ciclo que foi substituída
    if node_entered_in_cycle != -1:
        edge_to_remove = cycle_in_edges[node_entered_in_cycle]
        if edge_to_remove in final_edges_set:
            final_edges_set.remove(edge_to_remove)
            
    # Adiciona arestas da seleção original que não entravam no ciclo
    for v, edge in min_in_edges.items():
        if v not in cycle_nodes:
            final_edges_set.add(edge)

    return total_cost, list(final_edges_set)

def converter_grafo_para_lista(grafo_dict):
    """
    Converte o dicionário {u: {v: w}} (índice 1-based)
    para lista [(u-1, v-1, w)] (índice 0-based).
    """
    lista_arestas = []
    for u, vizinhos in grafo_dict.items():
        for v, w in vizinhos.items():
            # Subtrai 1 para trabalhar com índices 0-based internamente
            lista_arestas.append((u - 1, v - 1, w))
    return lista_arestas

# --- Bloco de Execução Principal ---
if __name__ == "__main__":

    print("Iniciando o processo da Arborescência Mínima (Chu-Liu/Edmonds)...")

    # 1. Preparar os dados
    print("Carregando e convertendo grafo de grafos.py...")
    arestas_formatadas = converter_grafo_para_lista(grafo_direcionado_2)
    num_nos = len(TODOS_NOS_2)
    
    # 2. Definir a raiz
    # O grafo da imagem tem Raiz no nó 1
    no_raiz_original = 1
    no_raiz_interno = no_raiz_original - 1 
    
    print(f"Executando o algoritmo com Raiz no nó {no_raiz_original}...")

    # 3. Executar o algoritmo
    custo_final, agm_final = chu_liu_edmonds(arestas_formatadas, num_nos, no_raiz_interno)

    # 4. Exibir os resultados
    print("\n--- Arborescência Mínima Encontrada ---")
    print("\nArestas (Formato: (Peso, Nó A, Nó B)):")
    
    # Ordenar para visualização limpa
    agm_final.sort(key=lambda x: x[0]) 
    
    for u, v, w in agm_final:
        # Converte de volta para 1-based para exibição
        print(f" ({w}, {u+1}, {v+1})")

    print("\n---------------------------------------")
    print(f"Custo Total da AGM: {custo_final}")
    print(f"Total de Arestas na AGM: {len(agm_final)}")
    print("---------------------------------------")