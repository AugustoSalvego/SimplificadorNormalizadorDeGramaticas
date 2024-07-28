import os

def ler_gramatica(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return {}
    with open(caminho_arquivo, 'r') as arquivo:
        gramatica = {}
        for linha in arquivo:
            cabeca, producoes = linha.strip().split(" -> ")
            gramatica[cabeca] = producoes.split(" | ")
    return gramatica


def remover_simbolos_inuteis(gramatica):
    print("Iniciando remoção de símbolos inúteis...")    
    geradores = set()
    mudou = True
    while mudou:
        mudou = False
        for cabeca, producoes in gramatica.items():
            for producao in producoes:
                if all(simbolo in geradores or simbolo.islower() for simbolo in producao):
                    if cabeca not in geradores:
                        geradores.add(cabeca)
                        mudou = True

    alcancaveis = set()
    simbolo_inicial = 'S'
    a_processar = [simbolo_inicial]
    while a_processar:
        simbolo = a_processar.pop()
        if simbolo not in alcancaveis:
            alcancaveis.add(simbolo)
            if simbolo in gramatica:
                for producao in gramatica[simbolo]:
                    for simb in producao:
                        if simb.isupper() and simb not in alcancaveis:
                            a_processar.append(simb)

    nova_gramatica = {}
    for cabeca in gramatica:
        if cabeca in geradores and cabeca in alcancaveis:
            novas_producoes = []
            for producao in gramatica[cabeca]:
                if all(simbolo in geradores or simbolo.islower() for simbolo in producao):
                    novas_producoes.append(producao)
            if novas_producoes:
                nova_gramatica[cabeca] = novas_producoes
    print("Símbolos inúteis removidos:", nova_gramatica)
    return nova_gramatica

def remover_producoes_vazias(gramatica):
    print("Iniciando remoção de produções vazias...")
    produtores_de_vazio = set()
    mudou = True
    while mudou:
        mudou = False
        for cabeca, producoes in gramatica.items():
            for producao in producoes:
                if producao == '' or all(simbolo in produtores_de_vazio for simbolo in producao):
                    if cabeca not in produtores_de_vazio:
                        produtores_de_vazio.add(cabeca)
                        mudou = True

    nova_gramatica = {}
    for cabeca, producoes in gramatica.items():
        novas_producoes = []
        for producao in producoes:
            partes_vazias = [""]
            for simbolo in producao:
                if simbolo in produtores_de_vazio:
                    partes_vazias.extend([parte + simbolo for parte in partes_vazias])
                else:
                    partes_vazias = [parte + simbolo for parte in partes_vazias]
            novas_producoes.extend(partes_vazias)
        nova_gramatica[cabeca] = list(set(novas_producoes))  # Remover duplicatas
    print("Produções vazias removidas:", nova_gramatica)
    return nova_gramatica

def substituir_producoes(gramatica):
    print("Iniciando substituição de produções...")
    substituicoes = {}
    for cabeca, producoes in gramatica.items():
        for producao in producoes:
            if len(producao) == 1 and producao.isupper():
                substituicoes[cabeca] = producao

    nova_gramatica = {}
    for cabeca, producoes in gramatica.items():
        novas_producoes = []
        for producao in producoes:
            while len(producao) == 1 and producao.isupper() and producao in substituicoes:
                producao = substituicoes[producao]
            novas_producoes.append(producao)
        nova_gramatica[cabeca] = novas_producoes
    print("Produções substituídas:", nova_gramatica)
    return nova_gramatica

def converter_greibach(gramatica):
    print("Iniciando conversão para forma normal de Greibach...")
    nova_gramatica = {}
    novas_producoes = {}

    for cabeca, producoes in gramatica.items():
        novas_producoes[cabeca] = []
        for producao in producoes:
            if producao[0].islower():
                novas_producoes[cabeca].append(producao)
            else:
                novo_simbolo = "X" + str(len(nova_gramatica) + 1)
                nova_gramatica[novo_simbolo] = [producao[1:]]
                novas_producoes[cabeca].append(producao[0] + novo_simbolo)

    nova_gramatica.update(novas_producoes)
    print("Conversão para forma normal de Greibach concluída:", nova_gramatica)
    return nova_gramatica

def fatorar_a_esquerda(gramatica):
    print("Iniciando fatoração à esquerda...")
    nova_gramatica = {}
    for cabeca, producoes in gramatica.items():
        prefixos = {}
        for producao in producoes:
            prefixo = producao[0]
            if prefixo not in prefixos:
                prefixos[prefixo] = []
            prefixos[prefixo].append(producao[1:] if len(producao) > 1 else '')

        novas_producoes = []
        for prefixo, sufixos in prefixos.items():
            if len(sufixos) > 1:
                novo_simbolo = cabeca + "'"
                nova_gramatica[novo_simbolo] = [sufixo + novo_simbolo if sufixo else '' for sufixo in sufixos]
                novas_producoes.append(prefixo + novo_simbolo)
            else:
                novas_producoes.append(prefixo + sufixos[0])
        nova_gramatica[cabeca] = novas_producoes
    print("Fatoração à esquerda concluída:", nova_gramatica)
    return nova_gramatica

def remover_recursao_a_esquerda(gramatica):
    print("Iniciando remoção de recursão à esquerda...")
    nova_gramatica = {}
    for cabeca, producoes in gramatica.items():
        recursivas = []
        nao_recursivas = []
        for producao in producoes:
            if producao.startswith(cabeca):
                recursivas.append(producao[len(cabeca):] + cabeca + "'")
            else:
                nao_recursivas.append(producao + cabeca + "'")
        nova_gramatica[cabeca] = nao_recursivas
        nova_gramatica[cabeca + "'"] = recursivas + ['']
    print("Remoção de recursão à esquerda concluída:", nova_gramatica)
    return nova_gramatica
