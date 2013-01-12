# coding: utf-8

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates
from Classes import *
from Cores import *

# FPS
FPS = 18

filaF, filaC, filaE, filaD = 0, 0, 0, 0

# mover personagem para a esquerda
def MPE():
    global filaE
    if teclas[K_LEFT] and not teclas[K_DOWN] and not teclas[K_UP]:
        filaE += 1
        if filaE == 2:
            filaE = 0
        personagem.image = pygame.image.load(listaImagensLadoEsquerdo[filaE])
        personagem.converterImagem()
        personagem.mover(-10, 0)
        personagem.px -= 1
#mover personagem para a direita
def MPD():
    global filaD
    if teclas[K_RIGHT] and not teclas[K_DOWN] and not teclas[K_UP]:
        filaD += 1
        if filaD == 2:
            filaD = 0
        personagem.image = pygame.image.load(listaImagensLadoDireito[filaD])
        personagem.converterImagem()
        personagem.mover(10, 0)
        personagem.px += 1

# mover personagem para cima
def MPC():
    global filaC
    if teclas[K_UP]:
        filaC += 1
        if filaC == 2:
            filaC = 0
        personagem.image = pygame.image.load(listaImagensCostas[filaC])
        personagem.converterImagem()
        personagem.mover(0, -10)
        personagem.py -= 1

# mover personagem para baixo
def MPB():
    global filaF
    if teclas[K_DOWN]:
        filaF += 1
        if filaF == 2:
            filaF = 0
        personagem.image = pygame.image.load(listaImagensFrente[filaF])
        personagem.converterImagem()
        personagem.mover(0, 10)
        personagem.py += 1

#=======================

# Configurações iniciais
pygame.init()
pygame.font.init()

musica = pygame.mixer.Sound("BGM/Firelink Shrine.wav")
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("rpg")
clock = pygame.time.Clock()
fundo = pygame.image.load("imagens/cenario2.png")
tela.blit(fundo, (0, 0))

#================================
#Criação de objetos
grupo = RenderUpdates()
personagem = Personagem(20, 290, grupo)
npc = Npcs(650, 290, grupo)
npc.image = pygame.image.load("sprites/personagem2.png")
npc.converterImagem()

npc2 = Npcs(675, 240, grupo)
npc2.image = pygame.image.load("sprites/personagem.png")
npc2.converterImagem()

npc3 = Npcs(675, 340, grupo)
npc3.image = pygame.image.load("sprites/personagem.png")
npc3.converterImagem()
frase = Textos(20, 'Quem é você e oque faz aqui?')

#===================================

# Lista com pontos onde o personagem não poderá se mover
lx = []
a = -3
for b in range(-4, 76):
    lx.append(a)
    a += 1
l1 = [-10]
l2 = [6]
iniciarConversa = [43, 0]
#===================================
teclas = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False, K_RETURN: False, 27: False}  # obs 27 = tecla 'esc'
musica.play()
fundo = fundo.convert()
pygame.display.flip()
while True:
    clock.tick(FPS)

    for evento in pygame.event.get([KEYUP, KEYDOWN]):
        valor = (evento.type == KEYDOWN)
        print(evento)
        if evento.key in teclas.keys():
            teclas[evento.key] = valor
    if teclas[27]:
        pygame.exit()
        sys.exit()
    if personagem.px in lx:
        if personagem.py in l1:
            MPB()
            MPD()
            MPE()
        elif personagem.py in l2:
            MPC()
            MPD()
            MPE()
        else:
            MPE()
            MPD()
            MPC()
            MPB()

    if personagem.px == iniciarConversa[0]:
        if personagem.py == iniciarConversa[1]:
            tela.blit(frase.frases, (200, 500))
            pygame.display.flip()

    #print(personagem.px,personagem.py)

    grupo.clear(tela, fundo)
    pygame.display.update(grupo.draw(tela))
