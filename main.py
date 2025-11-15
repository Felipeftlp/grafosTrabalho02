"""
Script Principal - Execução dos Algoritmos no Grafo do Trabalho

Este script executa os algoritmos de Kruskal e Bellman-Ford chamando
os mains de cada arquivo de implementação.

Requisitos do trabalho:
- AGM (Kruskal): s=1 (vértice inicial)
- Caminho Mais Curto (Bellman-Ford): s=1 (origem), destino=15

Autor: Ianco
"""

import runpy


def main():
    """
    Função principal que executa os mains dos algoritmos.
    """
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "TRABALHO UNIDADE 02 - GRAFOS" + " " * 24 + "║")
    print("║" + " " * 18 + "Algoritmos: Kruskal e Bellman-Ford" + " " * 16 + "║")
    print("║" + " " * 30 + "Autor: Ianco" + " " * 26 + "║")
    print("╚" + "═" * 68 + "╝")
    print("\n")
    
    # Executa o main do Kruskal
    runpy.run_module('algoritmo_kruskal', run_name='__main__')
    
    print("\n\n")
    
    # Executa o main do Bellman-Ford
    runpy.run_module('algoritmo_bellman_ford', run_name='__main__')
    
    print("\n")


if __name__ == "__main__":
    main()
