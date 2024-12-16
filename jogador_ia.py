# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro
from jogadas import R1_Vence
from jogadas import R1_Perde
from jogadas import R2
from jogadas import R3 
from jogadas import R4
from jogadas import R5 
from jogadas import R6 



class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        # Chama a função R3 para verificar o quadrado central
       
        jogada = R1_Vence(self.matriz)
        if jogada:
            return jogada
        
        jogada = R1_Perde(self.matriz)
        if jogada:
            return jogada
        
        jogada = R2(self.matriz)
        if jogada:
            return jogada
        
        jogada = R3(self.matriz)
        if jogada:
            return jogada
        
        jogada = R4(self.matriz)
        if jogada:
            return jogada
        
        jogada = R5(self.matriz)
        if jogada:
            return jogada

        jogada = R6(self.matriz)
        if jogada:
            return jogada
        
        return None

        