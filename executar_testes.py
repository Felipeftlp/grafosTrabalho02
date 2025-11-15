"""
Script para executar todos os testes do projeto.
Executa os testes de todos os algoritmos implementados.
"""

import subprocess
import sys

def executar_testes():
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "test/", "-v", "--tb=short"],
        cwd="."
    )
    return resultado.returncode

if __name__ == "__main__":
    sys.exit(executar_testes())