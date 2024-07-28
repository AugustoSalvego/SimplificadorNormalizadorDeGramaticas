import FuncGramaticas
import os

def main():
    # Usando caminhos absolutos
    arquivo_entrada = 'C:/Users/Danilo/Desktop/Simplificador/entrada.txt'

    # Ler a gramática do arquivo de entrada
    gramatica = FuncGramaticas.ler_gramatica(arquivo_entrada)
    print("Gramática lida:", gramatica)  # Diagnóstico

    # Aplicar simplificações e normalizações
    gramatica = FuncGramaticas.remover_simbolos_inuteis(gramatica)
    gramatica = FuncGramaticas.remover_producoes_vazias(gramatica)
    gramatica = FuncGramaticas.substituir_producoes(gramatica)
    gramatica = FuncGramaticas.converter_greibach(gramatica)
    gramatica = FuncGramaticas.fatorar_a_esquerda(gramatica)
    gramatica = FuncGramaticas.remover_recursao_a_esquerda(gramatica)

if __name__ == '__main__':
    main()