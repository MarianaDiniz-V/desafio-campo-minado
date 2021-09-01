from random import randint


def tabuleiro0(matriz_zerada):
    """Função que recebe uma matriz zerada e a imprime em outro formato.
    list -> list"""

    for i in range(9):
        print('|', end=' ')
        for j in range(9):
            print(matriz_zerada[i][j], end=' ')
        print('|')
    return matriz_zerada


def tabuleiro(matriz):
    """função que recebe a matriz gabarito e a imprime em outro formato
    quando o jogador perde.
    list -> list"""
    for i in range(9):
        print('|', end=' ')
        for j in range(9):
            print(matriz[i][j], end=' ')
        print('|')


def insere_bombas(matriz):
    """função responsável por inserir as bombas no tabuleiro. Recebe uma
    matriz, inicialmente vazia, e retorna com 9 bombas m
    list -> list"""
    for num in range(9):
        while True:
            x = randint(0, 8)
            y = randint(0, 8)
            if matriz[x][y] != 'm':
                matriz[x][y] = 'm'
                break
    return matriz


def minas_adjacentes(matriz):
    """função que recebe uma matriz preenchida apenas por 9 bombas e retorna
    uma matriz numerada, onde cada número corresponde ao número de bombas
    proóximas àquela casa.
    list -> list"""
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 'm': continue

            cont_minas_adj = 0

            for a in range(i - 1 if i > 0 else 0, i + 2 if i < 8 else 9):
                for b in range(j - 1 if j > 0 else 0, j + 2 if j < 8 else 9):
                    if matriz[a][b] == 'm': cont_minas_adj += 1
            matriz[i][j] = str(cont_minas_adj)

    return matriz


def atribui(matriz0, matriz, linha, coluna):
    """função que altera a linha e coluna da matriz que esta zerada. Ela substituir
    pelo correspondente a essa linha/coluna na matriz gabarito.
    list, list, int, int -> list"""
    matriz0[linha-1][coluna-1] = matriz[linha-1][coluna-1]
    for i in range(9):
        print('|', end=' ')
        for j in range(9):
            print(matriz0[i][j], end=' ')
        print('|')
    return matriz0


def main():
    
    matriz = [['.' for x in range(9)] for x in range(9)]
    matriz_zerada = [['.' for x in range(9)] for x in range(9)]
    
    print('******Olá, bem vindo ao Campo Minado!******')
    tabuleiro0(matriz_zerada)
    entrada1 = input('Digite (S)im para iniciar e (X) para sair: ')
    matriz = insere_bombas(matriz)
    matriz = minas_adjacentes(matriz)
    

    while entrada1.upper() not in 'SX' or entrada1 == '':
        entrada1 = input('Digite (S)im para iniciar e (X) para sair: ')
    
    while entrada1.upper() == 'X':
        print('Que pena :(\nVolte sempre!')
        break
    cont = 0
    par = [[]]
    while entrada1.upper() == 'S':
        linha = input('Escolha uma linha (de 1 a 9): ')
        while linha not in '123456789' or linha == '' or int(linha) > 9:
            linha = input('Escolha uma linha (de 1 a 9): ')
        linha = int(linha)
        coluna = input('Escolha uma coluna (de 1 a 9): ')
        while coluna not in '123456789' or coluna == '' or int(coluna) > 9:
            coluna = input('Escolha uma coluna (de 1 a 9): ')
        coluna = int(coluna)
        if matriz[linha-1][coluna-1] == 'm':
            print('Você perdeu!:(')
            matriz[linha-1][coluna-1] = 'M'
            tabuleiro(matriz)
            break
        atribui(matriz_zerada, matriz, linha, coluna)
        cont += 1
        jogada = [linha-1,coluna-1]
        if jogada in par:
            print('Essa casa já está ocupada. Tente novamente!')
            cont -= 1
        par += [jogada] 
        entrada2 = input('Digite (X) se desejar sair ou aperte qualquer tecla para continuar: ')
        """while entrada2 not in 'sSnN':
            entrada2 = input('Digite (X) se desejar sair ou aperte qualquer tecla para continuar: ')"""
            
        
        if entrada2.upper() == 'X':
            print('Obrigada por chegar até aqui :)\nAté a próxima!')
            break
        if cont == 72:
            print('Parabéns, você ganhou!:)')
            break
if __name__=="__main__":
    main()
