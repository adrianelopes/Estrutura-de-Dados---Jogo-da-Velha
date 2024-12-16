from random import randint
from tabuleiro import Tabuleiro


def R1_Vence(matriz):
     for l in range(3):
        soma = matriz[l][0] + matriz[l][1] + matriz[l][2]
        if soma == 2: 
            for c in range(3): 
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

     for c in range(3):
        soma = matriz[0][c] + matriz[1][c] + matriz[2][c]
        if soma == 2:  
            for l in range(3):  
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

     soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
     if soma == 2:
        for i in range(3):
            if matriz[i][i] == Tabuleiro.DESCONHECIDO:
                return (i, i)

     soma = matriz[0][2] + matriz[1][1] + matriz[2][0]
     if soma == 2:
        for i in range(3):
            if matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                return (i, 2 - i)

     return None
 
def R1_Perde(matriz):
     for l in range(3):
        soma = matriz[l][0] + matriz[l][1] + matriz[l][2]
        if soma == 8: 
            for c in range(3): 
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

     for c in range(3):
        soma = matriz[0][c] + matriz[1][c] + matriz[2][c]
        if soma == 8:  
            for l in range(3):  
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

     soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
     if soma == 8:
        for i in range(3):
            if matriz[i][i] == Tabuleiro.DESCONHECIDO:
                return (i, i)

     soma = matriz[0][2] + matriz[1][1] + matriz[2][0]
     if soma == 8:
        for i in range(3):
            if matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                return (i, 2 - i)

     return None
 
 

def R2(matriz):
    for l in range(3):
        for c in range(3):
            if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                matriz[l][c] = Tabuleiro.JOGADOR_0

                sequencias = 0

                if sum(matriz[l]) == 2 and matriz[l].count(Tabuleiro.DESCONHECIDO) == 1:
                    sequencias += 1

                coluna = [matriz[0][c], matriz[1][c], matriz[2][c]]
                if sum(coluna) == 2 and coluna.count(Tabuleiro.DESCONHECIDO) == 1:
                    sequencias += 1

                if l == c:
                    diagonal_principal = [matriz[0][0], matriz[1][1], matriz[2][2]]
                    if sum(diagonal_principal) == 2 and diagonal_principal.count(Tabuleiro.DESCONHECIDO) == 1:
                        sequencias += 1

                if l + c == 2:
                    diagonal_secundaria = [matriz[0][2], matriz[1][1], matriz[2][0]]
                    if sum(diagonal_secundaria) == 2 and diagonal_secundaria.count(Tabuleiro.DESCONHECIDO) == 1:
                        sequencias += 1

                matriz[l][c] = Tabuleiro.DESCONHECIDO

                if sequencias >= 2:
                    return (l, c)

    return None

     


def R3(matriz):

    if matriz[1][1] == Tabuleiro.DESCONHECIDO:
        return (1, 1)
    return None

def R4(matriz):
 
    cantos_opostos = {
        (0, 0): (2, 2),
        (2, 2): (0, 0),
        (0, 2): (2, 0),
        (2, 0): (0, 2),
    }

    for canto, oposto in cantos_opostos.items():
        l, c = canto
        if matriz[l][c] == Tabuleiro.JOGADOR_X and matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
            return oposto
    return None

def R5(matriz):

    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for l, c in cantos:
        if matriz[l][c] == Tabuleiro.DESCONHECIDO:
            return (l, c)
    return None

def R6(matriz):
 
    lista = [(l, c) for l in range(3) for c in range(3) if matriz[l][c] == Tabuleiro.DESCONHECIDO]

    if len(lista) > 0:
        p = randint(0, len(lista) - 1)
        return lista[p]
    return None
