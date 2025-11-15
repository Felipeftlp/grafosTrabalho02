"""
Testes para o Algoritmo de Bellman-Ford
"""

import pytest
from algoritmo_bellman_ford import bellman_ford, reconstruir_caminho


class TestBellmanFordBasico:
    """Testes básicos do algoritmo de Bellman-Ford"""
    
    def test_grafo_um_vertice(self):
        """Testa com grafo de um único vértice"""
        grafo = {1: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert predecessores[1] is None
        assert tem_ciclo == False
    
    def test_dois_vertices_conectados(self):
        """Testa com dois vértices conectados"""
        grafo = {1: {2: 5}, 2: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 5
        assert predecessores[2] == 1
        assert tem_ciclo == False
    
    def test_caminho_linear(self):
        """Testa caminho linear simples"""
        grafo = {
            1: {2: 1},
            2: {3: 2},
            3: {4: 3},
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 1
        assert distancias[3] == 3
        assert distancias[4] == 6
        assert tem_ciclo == False
    
    def test_grafo_exemplo1_aula(self):
        """Testa com o exemplo 1 da aula (sem ciclo negativo)"""
        grafo = {
            'A': {'B': 10, 'F': 8},
            'B': {'D': 1},
            'C': {'B': 1},
            'D': {'C': -2},
            'E': {'B': -4, 'D': -1},
            'F': {'E': 1}
        }
        
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 'A')
        
        # Caminho: A->F(8)->E(9)->B(5)->D(6)->C(4)
        assert distancias['A'] == 0
        assert distancias['B'] == 5
        assert distancias['C'] == 4
        assert distancias['D'] == 6
        assert distancias['E'] == 9
        assert distancias['F'] == 8
        assert tem_ciclo == False
    
    def test_grafo_exemplo2_aula(self):
        """Testa com o exemplo 2 da aula"""
        grafo = {
            1: {2: 2, 4: 1},
            2: {3: 2, 4: 2},
            3: {5: 2},
            4: {3: 4, 5: 4},
            5: {6: 1, 7: 2},
            6: {3: 3, 7: 4},
            7: {}
        }
        
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 2
        assert distancias[3] == 4
        assert distancias[4] == 1
        assert distancias[5] == 5
        assert distancias[6] == 6
        assert distancias[7] == 7
        assert tem_ciclo == False


class TestPesosNegativos:
    """Testes com arestas de peso negativo"""
    
    def test_aresta_negativa_simples(self):
        """Testa grafo com uma aresta negativa"""
        grafo = {
            1: {2: -5, 3: 2},
            2: {3: 1},
            3: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == -5
        assert distancias[3] == -4  # Via 1->2->3 (-5+1)
        assert tem_ciclo == False
    
    def test_multiplas_arestas_negativas(self):
        """Testa grafo com múltiplas arestas negativas"""
        grafo = {
            1: {2: 4, 3: 2},
            2: {3: -5},
            3: {4: 3},
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 4
        assert distancias[3] == -1  # Via 1->2->3
        assert distancias[4] == 2
        assert tem_ciclo == False
    
    def test_peso_negativo_nao_melhora(self):
        """Testa quando aresta negativa não melhora o caminho"""
        grafo = {
            1: {2: 1, 3: 10},
            2: {3: -3},  # 1->2->3 = -2, melhor que 1->3 = 10
            3: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[3] == -2
        assert predecessores[3] == 2


class TestCiclosNegativos:
    """Testes para detecção de ciclos de peso negativo"""
    
    def test_ciclo_negativo_simples(self):
        """Testa detecção de ciclo negativo simples"""
        grafo = {
            'A': {'B': 1},
            'B': {'C': -3},
            'C': {'A': 1},  # Ciclo: A->B->C->A = 1-3+1 = -1
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 'A')
        
        assert tem_ciclo == True
    
    def test_ciclo_negativo_triangulo(self):
        """Testa ciclo negativo em triângulo"""
        grafo = {
            1: {2: 1},
            2: {3: 1},
            3: {1: -5}  # Ciclo: 1->2->3->1 = 1+1-5 = -3
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert tem_ciclo == True
    
    def test_ciclo_positivo(self):
        """Testa que ciclo positivo não é detectado como erro"""
        grafo = {
            1: {2: 1},
            2: {3: 1},
            3: {1: 5}  # Ciclo: 1->2->3->1 = 1+1+5 = 7 (positivo)
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert tem_ciclo == False
    
    def test_ciclo_negativo_desconectado(self):
        """Testa ciclo negativo em componente desconectada"""
        grafo = {
            1: {2: 1},
            2: {},
            3: {4: 1},
            4: {5: 1},
            5: {3: -5}  # Ciclo negativo em componente separada
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1, vertices=[1,2,3,4,5])
        
        # Não deve detectar se o ciclo não é alcançável da origem
        assert tem_ciclo == False
    
    def test_ciclo_negativo_alcancavel(self):
        """Testa ciclo negativo alcançável da origem"""
        grafo = {
            1: {2: 1},
            2: {3: 1},
            3: {4: 1},
            4: {5: 1},
            5: {3: -5}  # Ciclo negativo: 3->4->5->3 = 1+1-5 = -3
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert tem_ciclo == True


class TestReconstrucaoCaminho:
    """Testes para reconstrução de caminhos"""
    
    def test_caminho_direto(self):
        """Testa reconstrução de caminho direto"""
        grafo = {1: {2: 5}, 2: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        caminho = reconstruir_caminho(predecessores, 1, 2)
        assert caminho == [1, 2]
    
    def test_caminho_multiplos_vertices(self):
        """Testa reconstrução de caminho com vários vértices"""
        grafo = {
            1: {2: 1},
            2: {3: 1},
            3: {4: 1},
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        caminho = reconstruir_caminho(predecessores, 1, 4)
        assert caminho == [1, 2, 3, 4]
    
    def test_caminho_inexistente(self):
        """Testa reconstrução quando não há caminho"""
        grafo = {1: {}, 2: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1, vertices=[1, 2])
        
        caminho = reconstruir_caminho(predecessores, 1, 2)
        assert caminho is None
    
    def test_caminho_para_origem(self):
        """Testa caminho da origem para ela mesma"""
        grafo = {1: {2: 5}, 2: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        caminho = reconstruir_caminho(predecessores, 1, 1)
        assert caminho == [1]
    
    def test_caminho_com_pesos_negativos(self):
        """Testa reconstrução de caminho com pesos negativos"""
        grafo = {
            1: {2: 5, 3: 1},
            2: {4: 1},
            3: {2: -10},  # Melhro Caminho: 1->3->2->4
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        caminho = reconstruir_caminho(predecessores, 1, 4)
        assert caminho == [1, 3, 2, 4]
        assert distancias[4] == -8  # 1 + (-10) + 1


class TestVerticesInacessiveis:
    """Testes com vértices inacessíveis"""
    
    def test_vertice_desconectado(self):
        """Testa vértice completamente desconectado"""
        grafo = {1: {2: 1}, 2: {}, 3: {}}
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1, vertices=[1, 2, 3])
        
        assert distancias[1] == 0
        assert distancias[2] == 1
        assert distancias[3] == float('inf')
        assert predecessores[3] is None
    
    def test_componentes_separadas(self):
        """Testa grafo com múltiplas componentes"""
        grafo = {
            1: {2: 1},
            2: {},
            3: {4: 2},
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1, vertices=[1,2,3,4])
        
        assert distancias[1] == 0
        assert distancias[2] == 1
        assert distancias[3] == float('inf')
        assert distancias[4] == float('inf')
    
    def test_no_sumidouro(self):
        """Testa vértice sumidouro (sem saídas)"""
        grafo = {
            1: {2: 5, 3: 10},
            2: {3: 2},
            3: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[3] == 7  # Via 1->2->3


class TestCasosEspeciais:
    """Testes para casos especiais e de borda"""
    
    def test_grafo_completo_pequeno(self):
        """Testa grafo completo pequeno"""
        grafo = {
            1: {2: 1, 3: 4},
            2: {1: 2, 3: 2},
            3: {1: 3, 2: 1}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 1
        assert distancias[3] == 3  # Via 1->2->3
    
    def test_multiplos_caminhos_mesmo_custo(self):
        """Testa quando há múltiplos caminhos com mesmo custo"""
        grafo = {
            1: {2: 2, 3: 2},
            2: {4: 2},
            3: {4: 2},
            4: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[4] == 4
        # Pode ser qualquer caminho válido
        assert predecessores[4] in [2, 3]
    
    def test_peso_zero(self):
        """Testa aresta com peso zero"""
        grafo = {
            1: {2: 0, 3: 5},
            2: {3: 0},
            3: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0
        assert distancias[2] == 0
        assert distancias[3] == 0  # Via 1->2->3
    
    def test_autoloop_positivo(self):
        """Testa auto-loop (aresta para si mesmo) com peso positivo"""
        grafo = {
            1: {1: 5, 2: 1},  # Auto-loop
            2: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[1] == 0  # Auto-loop positivo é ignorado
        assert distancias[2] == 1
    
    def test_autoloop_negativo(self):
        """Testa auto-loop com peso negativo"""
        grafo = {
            1: {1: -5, 2: 1},  # Auto-loop negativo
            2: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        # Auto-loop negativo é um ciclo negativo
        assert tem_ciclo == True
    
    def test_pesos_grandes(self):
        """Testa com pesos muito grandes"""
        grafo = {
            1: {2: 1000000},
            2: {3: 2000000},
            3: {}
        }
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[3] == 3000000
    
    def test_muitas_arestas_paralelas(self):
        """Testa otimização com muitas arestas"""
        # Cria um grafo linear longo
        grafo = {}
        for i in range(1, 51):
            grafo[i] = {i+1: 1} if i < 50 else {}
        
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[50] == 49
        assert tem_ciclo == False


class TestConvergenciaPrecoce:
    """Testes para verificar otimização de convergência precoce"""
    
    def test_convergencia_rapida(self):
        """Testa que o algoritmo para quando não há mais mudanças"""
        grafo = {
            1: {2: 1},
            2: {3: 1},
            3: {}
        }
        
        # Com apenas 3 vértices, deve convergir em 2 iterações
        distancias, predecessores, tem_ciclo = bellman_ford(grafo, 1)
        
        assert distancias[3] == 2
        assert tem_ciclo == False


if __name__ == "__main__":
    # Executa os testes com pytest
    pytest.main([__file__, "-v"])
