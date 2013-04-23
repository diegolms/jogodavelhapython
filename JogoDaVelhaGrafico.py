# -*- coding: utf-8 -*-

import pygame,sys  
from pygame.locals import* 
pygame.init()

tela = pygame.display.set_mode((610,550)) 
pygame.display.set_caption("Jogo da Velha")
xis = pygame.image.load("xis.png").convert_alpha()
bola = pygame.image.load("bola.png").convert_alpha()

text = pygame.font.SysFont("Arial.ttf", 32)

aviso = pygame.Surface((0,0))
pontosJogadorBola = pygame.Surface((0,0))
pontosJogadorXis = pygame.Surface((0,0))


continuar = True

terminou = False
comecou = False

jogadorBola = True
jogadorXis = False

posX = -50
posY = -50

contadorPontosBola = 0
contadorPontosXis = 0

casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
posicoes = [(80,45),(250,45),(430,45),(80,180),(250,180),(430,180),(80,325),(250,325),(430,325)]

jogada = True

contJogadas = 0

def preencherCasas():
	for i in range(len(casas)):
			if casas[i] == 0:
				tela.blit(bola,(posicoes[i]))
					
			elif casas[i] == 1:
				tela.blit(xis,(posicoes[i]))

				
def montarTabuleiro():
	tela.fill((255,255,255))
	tela.blit(aviso,(230,10))
	tela.blit(novoJogo,(30,500))
	tela.blit(pontosJogadorBola,(10,10))
	tela.blit(pontosJogadorXis,(440,10))
	pygame.draw.line(tela,(0,0,0),(200,50),(200,420),5)
	pygame.draw.line(tela,(0,0,0),(400,50),(400,420),5)
	pygame.draw.line(tela,(0,0,0),(80,150),(530,150),5)
	pygame.draw.line(tela,(0,0,0),(80,300),(530,300),5)

while(continuar):
	for event in pygame.event.get(): 
		if event.type==QUIT:
			sys.exit()
	
		
		posX = pygame.mouse.get_pos()[0]
		posY = pygame.mouse.get_pos()[1]
		
	
		teclas  = pygame.key.get_pressed()
	
		if terminou == False and comecou == True:
			if ((posX >= 81 and posX <= 195) and (posY >= 50 and posY <= 144)):	
				if casas[0] == -1:
					if (pygame.mouse.get_pressed()[0] or teclas[K_LEFT]) and jogadorBola == True:
						casas[0] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[0] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 203 and posX <= 398) and (posY >= 50 and posY <= 144)):	
				if casas[1] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[1] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[1] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
											
					
			if ((posX >= 404 and posX <= 531) and (posY >= 50 and posY <= 144)):	
				if casas[2] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[2] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[2] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 81 and posX <= 195) and (posY >= 153 and posY <= 295)):	
				if casas[3] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[3] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[3] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						


			if ((posX >= 203 and posX <= 398) and (posY >= 153 and posY <= 295)):	
				if casas[4] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[4] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[4] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 404 and posX <= 531) and (posY >= 153 and posY <= 295)):	
				if casas[5] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[5] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas+=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[5] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 81 and posX <= 195) and (posY >= 304 and posY <= 420)):	
				if casas[6] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[6] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[6] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 203 and posX <= 398) and (posY >= 304 and posY <= 420)):	
				if casas[7] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[7] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[7] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
						

			if ((posX >= 404 and posX <= 531) and (posY >= 304 and posY <= 420)):	
				if casas[8] == -1:
					if pygame.mouse.get_pressed()[0] and jogadorBola == True:
						casas[8] = 0
						jogadorBola = False
						jogadorXis = True
						contJogadas +=1
						
					elif pygame.mouse.get_pressed()[2] and jogadorXis == True:
						casas[8] = 1
						jogadorBola = True
						jogadorXis = False
						contJogadas +=1
	
			if (casas[0] == 1 and casas[1] == 1 and casas[2] == 1) or (casas[3] == 1 and casas[4] == 1 and casas[5] == 1) or (casas[6] == 1 and casas[7] == 1 and casas[8] == 1) or (casas[0] == 1 and casas[3] == 1 and casas[6] == 1) or (casas[1] == 1 and casas[4] == 1 and casas[7] == 1) or (casas[2] == 1 and casas[5] == 1 and casas[8] == 1) or (casas[0] == 1 and casas[4] == 1 and casas[8] == 1) or (casas[2] == 1 and casas[4] == 1 and casas[6] == 1):
				aviso = text.render("Jogador 2 Ganhou", True, (0, 0, 0))
				terminou = True
				comecou=False
				contadorPontosXis +=1
				pontosJogadorXis = text.render("Jogador ""X"" = " +str(contadorPontosXis), True, (0,0,255))	
				
			
			
			elif (casas[0] == 0 and casas[1] == 0 and casas[2] == 0) or (casas[3] == 0 and casas[4] == 0 and casas[5] == 0) or (casas[6] == 0 and casas[7] == 0 and casas[8] == 0) or (casas[0] == 0 and casas[3] == 0 and casas[6] == 0) or (casas[1] == 0 and casas[4] == 0 and casas[7] == 0) or (casas[2] == 0 and casas[5] == 0 and casas[8] == 0) or (casas[0] == 0 and casas[4] == 0 and casas[8] == 0) or (casas[2] == 0 and casas[4] == 0 and casas[6] == 0):
					aviso = text.render("Jogador 1 ganhou", True, (0, 0, 0))
					terminou = True
					comecou=False
					contadorPontosBola +=1
					pontosJogadorBola = text.render("Jogador ""O"" = " +str(contadorPontosBola), True, (0,0,255))
					
					
			elif contJogadas >= 9:
					aviso = text.render("Empate", True, (0, 0, 0))
					terminou = True
					terminou = True
					comecou=False
		
	
		
	
	if comecou==False:
		novoJogo = text.render("Novo Jogo", True, (0,0,0))
		novoJogoRect = novoJogo.get_rect().move(30,500)
	
	elif comecou==True:
		novoJogo = pygame.Surface((0,0))
		pontosJogadorBola = text.render("Jogador ""O"" = " +str(contadorPontosBola), True, (0,0,255))
		pontosJogadorXis = text.render("Jogador ""X"" = " +str(contadorPontosXis), True, (0,0,255))	
		
	if novoJogoRect.collidepoint(pygame.mouse.get_pos()) and comecou==False:
		novoJogo = text.render("Novo Jogo", True, (255,0,0))
		if pygame.mouse.get_pressed()[0]:
			comecou=True
			terminou=False
			contJogadas=0
			casas = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
			aviso = pygame.Surface((0,0))
	
	montarTabuleiro()
	preencherCasas()

			
	pygame.display.flip()    
