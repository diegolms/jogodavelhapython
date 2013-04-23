import os

tabuleiro = []

def montarTabuleiro():
    for i in range(0,3):
        linhas = []
        for j in range(0,3):
            linhas.append("")
        tabuleiro.append(linhas)
        

def mostrarTabuleiro():
    for i in tabuleiro:
        print(i)

def verificarGanhador():
	if (tabuleiro[0][0]=="O" and tabuleiro[0][1]=="O" and tabuleiro[0][2]=="O") or (tabuleiro[1][0]=="O" and tabuleiro[1][1]=="O" and tabuleiro[1][2]=="O") or (tabuleiro[2][0]=="O" and tabuleiro[2][1]=="O" and tabuleiro[2][2]=="O") or (tabuleiro[0][0]=="O" and tabuleiro[1][0]=="O" and tabuleiro[2][0]=="O") or (tabuleiro[0][1]=="O" and tabuleiro[1][1]=="O" and tabuleiro[2][1]=="O") or (tabuleiro[0][2]=="O" and tabuleiro[1][2]=="O" and tabuleiro[2][2]=="O") or (tabuleiro[0][0]=="O" and tabuleiro[1][1]=="O" and tabuleiro[2][2]=="O") or (tabuleiro[0][2]=="O" and tabuleiro[1][1]=="O" and tabuleiro[2][0]=="O"):
		return 1
		

	elif (tabuleiro[0][0]=="X" and tabuleiro[0][1]=="X" and tabuleiro[0][2]=="X") or (tabuleiro[1][0]=="X" and tabuleiro[1][1]=="X" and tabuleiro[1][2]=="X") or (tabuleiro[2][0]=="X" and tabuleiro[2][1]=="X" and tabuleiro[2][2]=="X") or (tabuleiro[0][0]=="X" and tabuleiro[1][0]=="X" and tabuleiro[2][0]=="X") or (tabuleiro[0][1]=="X" and tabuleiro[1][1]=="X" and tabuleiro[2][1]=="X") or (tabuleiro[0][2]=="X" and tabuleiro[1][2]=="X" and tabuleiro[2][2]=="X") or (tabuleiro[0][0]=="X" and tabuleiro[1][1]=="X" and tabuleiro[2][2]=="X") or (tabuleiro[0][2]=="X" and tabuleiro[1][1]=="X" and tabuleiro[2][0]=="X"):
		return 2
	


def jogada(jogador,linha,coluna):
	if jogador==1:
		jogador="O"
	elif jogador==2:
		jogador="X"
	for i in tabuleiro:
		tabuleiro[linha][coluna] = jogador

def mudarJogador(jogador):
	if jogador%2==0:
		return 1
	else:
		return 2


def menuJogo():
	opcao = int(input("1 - NovoJogo\n2 - Sair\n"))
	if opcao==1:
		return 1
	elif opcao==2:
		return 2
	


montarTabuleiro()
continuar=True
contJogadas=0
acabou=False

while continuar:
	mostrarTabuleiro()	
	jogador = mudarJogador(contJogadas)
	print("JOGADOR " +str(jogador))
	linha = int(input("Digite a linha - 1 a 3\n"))
	linha-=1
	coluna = int(input("Digite a coluna - 1 a 3\n"))
	coluna-=1
	if linha > 2 or linha < 0 or coluna > 2 or coluna < 0 or tabuleiro[linha][coluna] != "":
	    print("Linha ou coluna invalida")
	    continue
	jogada(jogador,linha,coluna)
	contJogadas += 1
	if contJogadas>=9:
		print("EMPATE")
		acabou=True
	if verificarGanhador()==1:
            mostrarTabuleiro()	
            print("O ganhou")
            acabou=True
	elif verificarGanhador()==2:
            mostrarTabuleiro()	
            print("X ganhou")
            acabou=True
	if acabou==True:
		opcao = menuJogo()
		if opcao==1:
			os.system("clear")
			tabuleiro = []
			montarTabuleiro()
			contJogadas=0
			acabou=False
		elif opcao==2:
			continuar=False
		
      

            
        
  
	    
	
	
	
	
			

        
        
        
