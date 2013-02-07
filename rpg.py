# -*- coding: utf-8 -*-


from config import *
from Classes import *
from Cores import *
import sys
from pygame.sprite import Sprite, RenderUpdates


FPS = 16

filaF, filaC, filaE, filaD = 0, 0, 0, 0

# mover personagem para a esquerda


def MPE():
    global filaE
    if teclas[K_LEFT] and not teclas[K_DOWN] and not teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensLadoEsquerdo[filaE])
        personagem.converterImagem()
        personagem.mover(-10, 0)
        personagem.px -= 1
        filaE += 1
        if filaE > 2:
            filaE = 0
#mover personagem para a direita


def MPD():
    global filaD
    if teclas[K_RIGHT] and not teclas[K_DOWN] and not teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensLadoDireito[filaD])
        personagem.converterImagem()
        personagem.mover(10, 0)
        personagem.px += 1
        filaD += 1
        if filaD > 2:
            filaD = 0

# mover personagem para cima


def MPC():
    global filaC
    if teclas[K_UP]:
        personagem.image = pygame.image.load(listaImagensCostas[filaC])
        personagem.converterImagem()
        personagem.mover(0, -10)
        personagem.py -= 1
        filaC += 1
        if filaC > 2:
            filaC = 0

# mover personagem para baixo


def MPB():
    global filaF
    if teclas[K_DOWN]:
        personagem.image = pygame.image.load(listaImagensFrente[filaF])
        personagem.converterImagem()
        personagem.mover(0, 10)
        personagem.py += 1
        filaF += 1
        if filaF > 2:
            filaF = 0

#=======================

fundo, tela, clock = config()

#================================
#Criação de objetos
musica = pygame.mixer.Sound("BGM/Firelink Shrine.wav")
grupo = RenderUpdates()
personagem = Personagem(20, 290, grupo)
npc = Npcs(650, 280, 'sprites/personagem2.png', grupo)
npc2 = Npcs(675, 240, "sprites/personagem.png", grupo)
npc3 = Npcs(675, 340, "sprites/personagem.png", grupo)
pygame.font.init()
frase = Textos(40, 'Quem eh voce e oque faz aqui?', 'carolingia.ttf')

#===================================

lx = [b for b in range(-4, 76)]
l1 = [-10]
l2 = [6]

#parede esquerda
parede = [x for x in range(-10, 16)]
colisaoParedeLateral = Eventos(parede, -2)


#===================================
iniciarConversa = [43, 0]

teclas = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
          K_RETURN: False, 27: False}  # obs 27 = tecla 'esc'

musica.play()
fundo = fundo.convert()
pygame.display.flip()
while True:
    clock.tick(FPS)

    for e in pygame.event.get([KEYUP, KEYDOWN]):
        valor = (e.type == KEYDOWN)
        if e.key in teclas.keys():
            teclas[e.key] = valor

    if teclas[27]:  # tecla ESC
        pygame.quit()
        sys.exit()
    if  colisaoParedeLateral.estaDentro(personagem.py, personagem.px):
        MPD()
        MPB()
        MPC()
    elif personagem.px in lx:
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

    if personagem.px == iniciarConversa[0] and personagem.py == iniciarConversa[1]:
        tela.blit(frase.frases, (200, 500))
        pygame.display.flip()

    #print(personagem.px, personagem.py)

    grupo.clear(tela, fundo)
    pygame.display.update(grupo.draw(tela))
