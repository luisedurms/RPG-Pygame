# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Cores import *

listaImagensFrente = ["sprites/danteFrente1.png",
                      "sprites/danteFrente2.png", "sprites/danteFrente3.png"]
listaImagensLadoEsquerdo = ["sprites/danteLadoEsquerdo1.png",
                            "sprites/danteLadoEsquerdo2.png", "sprites/danteLadoEsquerdo3.png"]
listaImagensLadoDireito = ["sprites/danteLadoDireito1.png",
                           "sprites/danteLadoDireito2.png", "sprites/danteLadoDireito3.png"]
listaImagensCostas = ["sprites/danteCostas1.png",
                      "sprites/danteCostas2.png", "sprites/danteCostas3.png"]


#Classes
class Personagem(Sprite):
    '''
    Classe que contem os dados do personagem, alem de carregar imagens e trata-las
    '''
    def __init__(self, pxInicial, pyInicial, *grupos):
        Sprite.__init__(self, *grupos)
        self.pxInicial = pxInicial
        self.pyInicial = pyInicial
        self.px = 0
        self.py = 0
        self.rect = Rect(self.pxInicial, self.pyInicial, 0, 0)
        global listaImagensFrente, listaImagensCostas, listaImagensLadoDireito, listaImagensLadoEsquerdo
        self.image = pygame.image.load(listaImagensLadoDireito[0])
        self.image.set_alpha(None, RLEACCEL)  # disable alpha
        self.image.convert()
        self.image.set_colorkey(magenta, RLEACCEL)
        pygame.draw.rect(self.image, preto, self)

    def mover(self, x, y):
        self.rect.move_ip(x, y)

    def converterImagem(self):
        self.image.set_alpha(None, RLEACCEL)  # disable alpha
        self.image.convert()
        self.image.set_colorkey(magenta, RLEACCEL)


class Npcs(Sprite):
    def __init__(self, posX, posY, arquivoDeImagem, *grupos):
        self.posX = posX
        self.posY = posY
        Sprite.__init__(self, *grupos)
        self.rect = Rect(self.posX, self.posY, 0, 0)
        self.image = pygame.image.load(arquivoDeImagem)
        self.image.set_alpha(None, RLEACCEL)  # disable alpha
        self.image.convert()
        self.image.set_colorkey(magenta, RLEACCEL)
        pygame.draw.rect(self.image, preto, self)

    def converterImagem(self):
        self.image.set_alpha(None, RLEACCEL)  # disable alpha
        self.image.convert()
        self.image.set_colorkey(magenta, RLEACCEL)


class Textos():
    '''
    Classe que gerencia todos os textos do jogo.
    '''

    def __init__(self, tamanho, dialogo, arquivoDeFonte, cor=branco, antialias=True):  # antialias faz um tratamento na imagem
        #pygame.font.init()
        self.tamanho = tamanho  # tamanho da frase
        self.dialogo = dialogo  # frase
        self.cor = cor  # cor
        self.antialias = antialias
        self.fonte = pygame.font.SysFont(arquivoDeFonte, self.tamanho)
        self.frases = self.fonte.render(
            self.dialogo, self.antialias, self.cor)

    def alterarDialogo(self, novodialogo):
        self.dialogo = novodialogo

    def alterarCor(self, novaCor):
        self.cor = novaCor

    def alterarTamanho(self, novoTamanho):
        self.tamanho = novoTamanho


class Eventos():
    '''
    Classe que gerencia os eventos do jogo
    '''

    def __init__(self, py, px):
        self.px = px
        self.py = py

    def estaDentro(self, pontoY, pontoX):
        if pontoY in self.py and pontoX == self.px:
            return True
        return False


'''class PontosDeColisao():

    def __init__(self, px, py):
        self.px = px
        self.py = py

    def Colidiu(self, pontoX, pontoY):
      if pontoX
'''
