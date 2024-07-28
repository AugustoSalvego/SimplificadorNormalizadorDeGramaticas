 ## Simplificador e normalizador de gramáticas 

Projeto de um simplificador e normalizador de gramáticas livres de contexto feito na linguagem python.


## Funcionalidades

- Lê a gramática de um arquivo de texto e a armazena em um dicionário.
- Remove símbolos não geradores e não alcançáveis da gramática.
- Remove produções que geram a palavra vazia.
- Substitui produções que têm um único símbolo não terminal pelo seu conjunto de produções.
- Converte a gramática para a forma normal de Greibach.
- Realiza a fatoração à esquerda para remover indeterminismos à esquerda.
- Remove a recursão à esquerda direta de cada não terminal.
- Geração de resultados em tempo de execução.
    
    
### Como usar no terminal

Procure o caminho da pasta que contém os tres arquivos:

    FuncGramaticas.py
    entrada.txt
    main.py
    
Abra o cmd e digite:

    cd ' caminhoDaPasta '
    
Utilize o comando:
        
    python main.py
 

### O Código irá realizar a saída em tempo de execução

Saídas esperadas:
    
    Gramática lida: {'S': ['aA', 'bB'], 'A': ['a', 'ε'], 'B': ['b']}
    Iniciando remoção de símbolos inúteis...
    Símbolos inúteis removidos: {'S': ['aA', 'bB'], 'A': ['a', 'ε'], 'B': ['b']}
    Iniciando remoção de produções vazias...
    Produções vazias removidas: {'S': ['aA', 'bB', 'a', 'b'], 'A': ['a'], 'B': ['b']}
    Iniciando substituição de produções...
    Produções substituídas: {'S': ['aA', 'bB', 'a', 'b'], 'A': ['a'], 'B': ['b']}
    Iniciando conversão para forma normal de Greibach...
    Conversão para forma normal de Greibach concluída: {'S': ['aA', 'bB', 'a', 'b'], 'A': ['a'], 'B': ['b']}
    Iniciando fatoração à esquerda...
    Fatoração à esquerda concluída: {'S': ['aA', 'bB', 'a', 'b'], 'A': ['a'], 'B': ['b']}
    Iniciando remoção de recursão à esquerda...
    Remoção de recursão à esquerda concluída: {'S': ['aA\'', 'bB\'', 'a', 'b'], 'A': ['aA\'', 'ε'], 'B': ['bB\'', 'ε']}

    
