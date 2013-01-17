# coding: utf-8

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates

#configurações

def config():
  pygame.init() # inicializa o pygame
	TAMANHO_TELA = (800, 600)
	NOME = "RPG"
	c_tela = pygame.display.set_mode(TAMANHO_TELA) #Configura a tela
	pygame.display.set_caption(NOME)
	c_clock = pygame.time.Clock() 
	c_fundo = pygame.image.load("imagens/cenario2.png")
	c_tela.blit(c_fundo, (0, 0))
	return c_fundo, c_tela, c_clock	

	
