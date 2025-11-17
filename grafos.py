# Grafo 1 do documento ponderado e direcionado
# Formato: {no_origem: {no_destino: peso, ...}}
grafo_direcionado = {
    1: {6: 3, 11: 1},
    2: {1: 2},
    3: {2: 1, 4: 2, 9: 2, 8: 10},
    4: {5: 4},
    5: {10: 5},
    6: {2: 7, 7: 2, 11: 0},
    7: {3: 9, 8: 8, 12: 1},
    8: {13: 5},
    9: {4: 9, 14: 1},
    10: {5: 7, 9: 6, 15: 9},
    11: {12: 4},
    12: {11: 4, 17: 1},
    13: {9: 15, 18: 4},
    14: {15: 1, 19: 18},
    15: {},  # Nó sumidouro (sem saídas)
    16: {11: 2, 12: 3},
    17: {12: 1, 18: 20},
    18: {19: 5},
    19: {}   # Nó sumidouro (sem saídas)
}

# O grafo tem nós de 1 a 19.
TODOS_NOS = set(range(1, 20))

# Grafo 2 do documento (Ponderado e Direcionado)
# Formato: {no_origem: {no_destino: peso, ...}}
grafo_direcionado_2 = {
    1: {2: 1, 3: 8, 6: 5},
    2: {3: 8, 6: 2},
    3: {5: 6},
    4: {2: 7, 3: 4, 6: 8},
    5: {4: 3, 6: 8},
    6: {4: 8} 
}

# O grafo tem nós de 1 a 6
TODOS_NOS_2 = set(range(1, 7))