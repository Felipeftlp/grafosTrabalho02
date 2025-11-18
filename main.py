"""
Script Principal - Execução dos Algoritmos no Grafo do Trabalho

Este script executa os algoritmos implementados chamando os mains de cada arquivo.
"""

import runpy


def main():
    """
    Função principal que executa os mains dos algoritmos.
    """
    print("\n")
    print("═" * 68)
    print(" " * 15 + "TRABALHO UNIDADE 02 - GRAFOS")
    print(" " * 10 + "Algoritmos: Kruskal, Prim, Chu-Liu/Edmonds,")
    print(" " * 15 + "Bellman-Ford, Dijkstra e Hierholzer")
    print("═" * 68)
    print("\n")
    
    # === ÁRVORES GERADORAS MÍNIMAS ===
    print("=" * 70)
    print("ÁRVORES GERADORAS MÍNIMAS (AGM)")
    
    # Kruskal
    print("\n" + "─" * 70 + "\n")
    runpy.run_module('algoritmo_kruskal', run_name='__main__')
    print("\n" + "─" * 70 + "\n")
    
    # Prim
    print(">>> Algoritmo de Prim")
    runpy.run_module('algoritmo_prim', run_name='__main__')
    print("\n" + "─" * 70 + "\n")
    
    # Chu-Liu/Edmonds
    print(">>> Algoritmo de Chu-Liu/Edmonds")
    runpy.run_module('algoritmo_chu_liu_edmonds', run_name='__main__')

    print("=" * 70)
    print("\n\n")

    
    
    # === CAMINHOS MAIS CURTOS ===
    print("=" * 70)
    print("CAMINHOS MAIS CURTOS")
    
    # Bellman-Ford
    print("\n" + "─" * 70 + "\n")
    runpy.run_module('algoritmo_bellman_ford', run_name='__main__')
    print("\n" + "─" * 70 + "\n")
    
    # Dijkstra
    print(">>> Algoritmo de Dijkstra")
    runpy.run_module('algoritmo_dijkstra', run_name='__main__')
    
    print("=" * 70)
    print("\n\n")

    # === GRAFOS EULERIANOS ===
    print("=" * 70)
    print("GRAFOS EULERIANOS")
    print("\n" + "─" * 70 + "\n")

    # Hierholzer - CICLOS
    print(">>> Algoritmo de Hierholzer (CICLOS)")
    runpy.run_module('algoritmo_hierholzer_ciclos', run_name='__main__')
    print("\n" + "─" * 70 + "\n")

    # Hierholzer - CAMINHOS
    print(">>> Algoritmo de Hierholzer (CAMINHOS)")
    runpy.run_module('algoritmo_hierholzer_caminhos', run_name='__main__')

    print("=" * 70)
    print("\n\n")


if __name__ == "__main__":
    main()
