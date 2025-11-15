"""
Testes para o Algoritmo de Kruskal
"""

import pytest
from algoritmo_kruskal import kruskal, kruskal_direcionado, UnionFind


class TestUnionFind:
    """Testes para a estrutura Union-Find"""
    
    def test_inicializacao(self):
        """Testa inicialização do Union-Find"""
        vertices = [1, 2, 3, 4]
        uf = UnionFind(vertices)
        
        # Cada vértice deve ser seu próprio pai inicialmente
        for v in vertices:
            assert uf.find(v) == v
    
    def test_union_diferentes(self):
        """Testa união de vértices diferentes"""
        uf = UnionFind([1, 2, 3])
        
        assert uf.union(1, 2) == True
        assert uf.find(1) == uf.find(2)
    
    def test_union_mesmo_conjunto(self):
        """Testa união de vértices já no mesmo conjunto"""
        uf = UnionFind([1, 2, 3])
        
        uf.union(1, 2)
        assert uf.union(1, 2) == False  # Já estão unidos
    
    def test_compressao_caminho(self):
        """Testa compressão de caminho"""
        uf = UnionFind([1, 2, 3, 4])
        
        uf.union(1, 2)
        uf.union(2, 3)
        uf.union(3, 4)
        
        # Após find, todos devem apontar para a mesma raiz
        raiz = uf.find(1)
        assert uf.find(4) == raiz


class TestKruskal:
    """Testes para o algoritmo de Kruskal"""
    
    def test_grafo_vazio(self):
        """Testa com grafo vazio"""
        grafo = {}
        arestas, custo = kruskal(grafo)
        
        assert arestas == []
        assert custo == 0
    
    def test_um_vertice(self):
        """Testa com grafo de um único vértice"""
        grafo = {1: {}}
        arestas, custo = kruskal(grafo, vertices=[1])
        
        assert arestas == []
        assert custo == 0
    
    def test_dois_vertices_conectados(self):
        """Testa com dois vértices conectados"""
        grafo = {1: {2: 5}}
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 1
        assert custo == 5
        assert (1, 2, 5) in arestas or (2, 1, 5) in arestas
    
    def test_grafo_simples_triangulo(self):
        """Testa com grafo triangular simples"""
        grafo = {
            1: {2: 1, 3: 3},
            2: {3: 2}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 2  # n-1 = 3-1 = 2
        assert custo == 3  # 1 + 2
    
    def test_grafo_exemplo_aula(self):
        """Testa com o grafo exemplo da aula"""
        grafo = {
            'a': {'c': 7},
            'b': {'c': 2, 'e': 8, 'f': 7},
            'c': {'d': 6, 'f': 1},
            'd': {'g': 6},
            'e': {'f': 2, 'h': 1},
            'f': {'h': 4, 'i': 1, 'g': 5},
            'g': {'j': 2},
            'h': {'i': 6},
            'i': {'j': 5}
        }
        
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 9  # 10 vértices - 1 = 9 arestas
        # AGM: c-f(1), e-h(1), f-i(1), b-c(2), e-f(2), g-j(2), f-g(5), c-d(6), a-c(7)
        assert custo == 27
    
    def test_pesos_iguais(self):
        """Testa grafo com todos os pesos iguais"""
        grafo = {
            1: {2: 1, 3: 1},
            2: {3: 1, 4: 1},
            3: {4: 1}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 3  # n-1 = 4-1 = 3
        assert custo == 3  # 3 arestas de peso 1
    
    def test_pesos_negativos(self):
        """Testa grafo com pesos negativos"""
        grafo = {
            1: {2: -5, 3: 2},
            2: {3: 1}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 2
        assert custo == -4  # -5 + 1
    
    def test_grafo_linha(self):
        """Testa grafo em forma de linha (caminho)"""
        grafo = {
            1: {2: 1},
            2: {3: 2},
            3: {4: 3},
            4: {5: 4}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 4  # 5-1 = 4
        assert custo == 10  # 1+2+3+4
    
    def test_grafo_completo_4_vertices(self):
        """Testa grafo completo com 4 vértices"""
        grafo = {
            1: {2: 1, 3: 4, 4: 3},
            2: {3: 2, 4: 5},
            3: {4: 6}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 3  # 4-1 = 3
        assert custo == 6  # 1+2+3 (arestas de menor peso)
    
    def test_grafo_multiplas_componentes(self):
        """Testa grafo desconexo (múltiplas componentes)"""
        grafo = {
            1: {2: 1},
            2: {},
            3: {4: 2},
            4: {}
        }
        vertices = [1, 2, 3, 4]
        arestas, custo = kruskal(grafo, vertices)
        
        # Deve retornar árvore de cada componente conexa
        assert len(arestas) == 2  # Uma aresta por componente
        assert custo == 3  # 1 + 2
    
    def test_pesos_decimais(self):
        """Testa grafo com pesos decimais"""
        grafo = {
            1: {2: 1.5, 3: 2.7},
            2: {3: 0.8}
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 2
        assert abs(custo - 2.3) < 0.001  # 0.8 + 1.5
    
    def test_arestas_duplicadas(self):
        """Testa grafo com arestas duplicadas (mesma aresta com pesos diferentes)"""
        # Kruskal deve escolher a aresta de menor peso
        grafo = {
            1: {2: 5},
            2: {1: 3}  # Aresta duplicada com peso diferente
        }
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 1
        assert custo == 3  # Deve escolher o menor peso


class TestKruskalDirecionado:
    """Testes para kruskal_direcionado"""
    
    def test_grafo_direcionado_simples(self):
        """Testa conversão de grafo direcionado para não direcionado"""
        grafo = {
            1: {2: 3},
            2: {3: 2},
            3: {1: 4}
        }
        
        arestas, custo = kruskal_direcionado(grafo)
        
        assert len(arestas) == 2  # 3-1 = 2
        assert custo == 5  # 2 + 3
    
    def test_grafo_direcionado_bidirecional(self):
        """Testa grafo direcionado com arestas bidirecionais"""
        grafo = {
            1: {2: 5},
            2: {1: 3, 3: 2},
            3: {2: 4}
        }
        
        arestas, custo = kruskal_direcionado(grafo)
        
        assert len(arestas) == 2
        # Deve escolher os menores pesos: 3 (entre 1-2) e 2 (entre 2-3)
        assert custo == 5


class TestCasosEspeciais:
    """Testes para casos especiais e de borda"""
    
    def test_ciclo_simples(self):
        """Testa detecção de ciclo em grafo cíclico"""
        grafo = {
            1: {2: 1, 4: 4},
            2: {3: 2},
            3: {4: 3},
            4: {}
        }
        
        arestas, custo = kruskal(grafo)
        
        # Deve escolher apenas 3 arestas para 4 vértices (evitando ciclo)
        assert len(arestas) == 3
        assert custo == 6  # 1+2+3 (evita a aresta de peso 4)
    
    def test_estrela(self):
        """Testa grafo em forma de estrela"""
        grafo = {
            'centro': {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        }
        
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 4  # 5-1 = 4
        assert custo == 10  # 1+2+3+4
    
    def test_grafo_bipartido(self):
        """Testa grafo bipartido"""
        grafo = {
            'a1': {'b1': 1, 'b2': 2},
            'a2': {'b1': 3, 'b2': 4},
            'b1': {},
            'b2': {}
        }
        
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 3  # 4-1 = 3
        assert custo == 6  # 1+2+3 (menores pesos)
    
    def test_peso_zero(self):
        """Testa grafo com aresta de peso zero"""
        grafo = {
            1: {2: 0, 3: 5},
            2: {3: 1}
        }
        
        arestas, custo = kruskal(grafo)
        
        assert len(arestas) == 2
        assert custo == 1  # 0 + 1


if __name__ == "__main__":
    # Executa os testes com pytest
    pytest.main([__file__, "-v"])
