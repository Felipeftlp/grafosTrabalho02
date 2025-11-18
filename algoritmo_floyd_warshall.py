import math

INF = math.inf

def floyd_warshall(grafo, todos_nos):
    nos = sorted(todos_nos)

    dist = {i: {j: INF for j in nos} for i in nos}
    pred = {i: {j: -1 for j in nos} for i in nos}

    for i in nos:
        for j in nos:
            if j in grafo.get(i, {}):
                dist[i][j] = grafo[i][j]
                pred[i][j] = i

        dist[i][i] = 0
        pred[i][i] = i

    for k in nos:
        for i in nos:
            for j in nos:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def recuperar_caminho(pred, origem, destino):
    if pred[origem][destino] == -1:
        return None  

    caminho = [destino]
    atual = destino

    while atual != origem:
        atual = pred[origem][atual]
        caminho.append(atual)

    caminho.reverse()
    return caminho

def calcular_custo_caminho(caminho, grafo):
    custo = 0
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]
        custo += grafo[u][v]
    return custo

def exibir_resultados_floyd(dist, pred, origem, destino):
    nos = sorted(dist.keys())

    # ------------------------------
    # MATRIZ DE DISTÂNCIAS
    # ------------------------------
    print("\n==== MATRIZ DE DISTÂNCIAS (dist) ====")
    print("      " + "  ".join(f"{j:>4}" for j in nos))
    for i in nos:
        linha = []
        for j in nos:
            val = dist[i][j]
            if val == float("inf"):
                linha.append(" INF")
            else:
                linha.append(f"{val:4}")
        print(f"{i:>3} | " + "  ".join(linha))

    # ------------------------------
    # MATRIZ DE PREDECESSORES
    # ------------------------------
    print("\n==== MATRIZ DE PREDECESSORES (pred) ====")
    print("      " + "  ".join(f"{j:>4}" for j in nos))
    for i in nos:
        linha = []
        for j in nos:
            val = pred[i][j]
            linha.append(f"{val:4}")
        print(f"{i:>3} | " + "  ".join(linha))

    # ------------------------------
    # CAMINHO + CUSTO
    # ------------------------------
    print(f"\n==== CAMINHO MÍNIMO DE {origem} PARA {destino} ====")
    caminho = recuperar_caminho(pred, origem, destino)

    if caminho is None:
        print("Não existe caminho entre os dois nós.")
        return
    
    print("Caminho:", " → ".join(map(str, caminho)))

    custo = calcular_custo_caminho(caminho, grafo_direcionado)
    print("Custo total:", custo)

if __name__ == "__main__":
    from grafos import grafo_direcionado, TODOS_NOS
    
    print("Grafo do Trabalho: Direcionado e Ponderado (19 vértices)")
    print("Requisito: s=1 (vértice inicial)")
    print()
    
    dist, pred = floyd_warshall(grafo_direcionado, TODOS_NOS)
    
    origem = 1
    destino = 15

    caminho = recuperar_caminho(pred, origem, destino)
    
    exibir_resultados_floyd(dist, pred, origem, destino)