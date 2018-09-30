import pygame, sys
from pygame.locals import*
from j2048_motor_42346 import novo_jogo
from j2048_motor_42346 import valor
from j2048_motor_42346 import terminou
from j2048_motor_42346 import esquerda
from j2048_motor_42346 import pontuacao
from j2048_motor_42346 import direita
from j2048_motor_42346 import acima
from j2048_motor_42346 import abaixo
from j2048_motor_42346 import pontuacao
from j2048_motor_42346 import ganhou_ou_perdeu
from j2048_motor_42346 import inserir_2ou4

from j2048_gestor_42346 import inicializa_semente
from j2048_gestor_42346 import le_identificacao
from j2048_gestor_42346 import regista_grelha_inicial
from j2048_gestor_42346 import regista_jogada
from j2048_gestor_42346 import regista_pontos
from j2048_gestor_42346 import escreve_registo

#inicia o modulo pygame
pygame.init()

pygame.time.Clock()

# Musica
pygame.mixer.music.load("SonicLiveandLearn.mp3")
            
# Dimensoes da janela
largura = 1152
altura = 648
janela = pygame.display.set_mode((largura,altura))
 
# Nome da janela pygame
pygame.display.set_caption("Speed2048")

# Load imagens e converte-as
background = pygame.image.load('back.png')
title1 = pygame.image.load('title.png')
sonic = pygame.image.load('sonic.png')

# Cores RGB necessarias
preto = (0,0,0)
azul = (35,135,210)
Vermelho = (255,0,0)

c0 = (0,0,0)
c2 = (255,0,0)
c4 = (255,255,0)
c8 = (0,255,255)
c16 = (0,255,0)
c32 = (255,0,255)
c64 = (0,0,255)
c128 = (0,150,100)
c256 = (150,150,0)
c512 = (0,200,150)
c1024 = (150,150,150)
c2048 = (255,255,155)


# Dicionario para os valores dos quadrados terem diferentes cores
cores = {0:c0,2:c2,4:c4,8:c8,16:c16,32:c32,64:c64,128:c128,256:c256,512:c512,1024:c1024,2048:c2048}


# Cria os quadrados da grelha
def grelha(jogo):
    grande = pygame.draw.rect(janela, azul, (140, 220, 390, 390))
    for i in range(4):
        for j in range(4):
            quad = pygame.draw.rect(janela, preto, (150+(i*95), 230+(j*95), 85, 85))  
            preencher_grelha(valor(jogo,j+1,i+1),quad)
            # A funcao preencher_grelha recebe as dimensoes do quadrado e preenche com o valor do dicionario respectivo ao da grelha

#esta funcao recebe como parametros o valor e as dimensoes do quadrado
def preencher_grelha(valor,quad):
    
    font = pygame.font.SysFont('Comicsansms', 30)
    
    if valor == 0:
        # funcao render(Texto,Anti-aliasing,cor)
        texto = font.render('',1,cores[valor])
        janela.blit(texto,quad)                   
    elif valor < 10:
        texto = font.render(str(valor),1,cores[valor])
        #O texto vai aparecer na meio da area do quadrado
        janela.blit(texto,(quad[0]+30,quad[1]+20)) 
    elif valor < 100:
        texto = font.render(str(valor),1,cores[valor])
        janela.blit(texto,(quad[0]+25,quad[1]+20))
    elif valor < 1000:
        texto = font.render(str(valor),1,cores[valor])
        janela.blit(texto,(quad[0]+15,quad[1]+20))
    else:
        texto = font.render(str(valor),1,cores[valor])
        janela.blit(texto,(quad[0]+5,quad[1]+20))
        

# Esta funcao serve para preencher os retângulos criados na funcao mostrar_score()
def meter_score(jogo):

    font = pygame.font.SysFont('Magneto',30) # SysFont(('nome da fonte'),tamanho)
                    
    text = font.render('Score',20,azul)            
    janela.blit(text,(70,10))  
                    
    text2 = font.render(str(pontuacao(jogo)),1,azul) 
    janela.blit(text2,(90,40))


# Informacao visivel na janela (titulo, imagens, teclas)          
def title():
    janela.blit(title1,(0,0))

    font = pygame.font.SysFont('Copperplate Gothic Bold',26)

    novoJogo = font.render('N - New Game',20,preto)
    janela.blit(novoJogo,(1020,620))


def write_best(pontos):
    
    ficheiro = open('pontos.txt','w')
    ficheiro.write(pontos)
    ficheiro.close()

def read_best():
    
    ficheiro = open('pontos.txt','r')
    linha1 = ficheiro.read()
    ficheiro.close()    
    return(linha1)


def meter_best_score(jogo):
    
    font = pygame.font.SysFont('Magneto',30)

    text = font.render('Best Score',20,azul)  
    janela.blit(text,(940,10))
    
    if int(read_best()) > int(pontuacao(jogo)):
        text2 = font.render(str(read_best()),1,azul)
        
    else:
        text2 = font.render(str(pontuacao(jogo)),1,azul)

    janela.blit(text2,(960,40))

        

def end_game(jogo):

    regista_pontos(pontuacao(jogo))
    mensagem_cloud = escreve_registo()
    print(mensagem_cloud)
        
    font = pygame.font.SysFont('Copperplate Gothic Bold',80)

    text = font.render('GAME OVER',30,Vermelho)
    janela.blit(text,(340,60))

    pygame.display.flip()
 
    if int(pontuacao(jogo)) > int(read_best()):
        write_best(str(pontuacao(jogo)))
        
    while True:
            
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN and (event.key == K_n):
                main()
                    


def main():

    pygame.mixer.music.play(-1)
    
    janela.blit(background,(0,0)) #define o background
    janela.blit(sonic,(800,170))
    title()
    le_identificacao()
    inicializa_semente(None)
    jogo = novo_jogo()
    grelha(jogo)
    meter_score(jogo)
    meter_best_score(jogo)

    regista_grelha_inicial(valor(jogo,1,1), valor(jogo,1,2), valor(jogo,1,3), valor(jogo,1,4),
                           valor(jogo,2,1), valor(jogo,2,2), valor(jogo,2,3), valor(jogo,2,4),
                           valor(jogo,3,1), valor(jogo,3,2), valor(jogo,3,3), valor(jogo,3,4),
                           valor(jogo,4,1), valor(jogo,4,2), valor(jogo,4,3), valor(jogo,4,4))

    musicplay = True
    while True and (not terminou(jogo)):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (not terminou(jogo)):  # Funcoes direita, esquerda, acima, abaixo feitas no motor
                if event.type == KEYDOWN and (event.key == K_UP or event.key == K_w):#para fazer a jogada acima usamos as teclas key_up ou w,sempre que usarmos estas teclas ao jogarmos o jogo, ele vai actualizar a grelha e os scores.
                    jogo = acima(jogo)                                                           #o mesmo se passa com as outras, ao usarmos as teclas, actualiza a grelha no jogo.
                    title()
                    grelha(jogo)               
                    meter_score(jogo)
                    meter_best_score(jogo)
                    regista_jogada('w')
                                
                elif event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_s):
                    jogo = abaixo(jogo)
                    title()
                    grelha(jogo)
                    meter_score(jogo)
                    meter_best_score(jogo)
                    regista_jogada('s')
                    
                elif event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_a):
                    jogo = esquerda(jogo)
                    title()
                    grelha(jogo)
                    meter_score(jogo)
                    meter_best_score(jogo)
                    regista_jogada('a')
                    
                elif event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_d):
                    jogo = direita(jogo)
                    title()
                    grelha(jogo)
                    meter_score(jogo)
                    meter_best_score(jogo)
                    regista_jogada('d')

                elif event.type == KEYDOWN and event.key == K_n:

                    regista_pontos(pontuacao(jogo))
                    mensagem_cloud = escreve_registo()
                    print(mensagem_cloud)
                    
                    if int(pontuacao(jogo)) > int(read_best()):
                        write_best(str(pontuacao(jogo)))
                        
                    inicializa_semente(None)
                    jogo = novo_jogo()

                    regista_grelha_inicial(valor(jogo,1,1), valor(jogo,1,2), valor(jogo,1,3), valor(jogo,1,4),
                                           valor(jogo,2,1), valor(jogo,2,2), valor(jogo,2,3), valor(jogo,2,4),
                                           valor(jogo,3,1), valor(jogo,3,2), valor(jogo,3,3), valor(jogo,3,4),
                                           valor(jogo,4,1), valor(jogo,4,2), valor(jogo,4,3), valor(jogo,4,4))
                    title()
                    grelha(jogo)
                    meter_score(jogo)
                    meter_best_score(jogo)
                    
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()


                if ganhou_ou_perdeu(jogo) == True:
                    janela.blit(imgwin,(0,0))

##                if pygame.time.get_ticks() > 5000:
##                    inserir_2ou4(jogo[0])
##                    pygame.time.Clock()

        pygame.display.update()
    end_game(jogo)
    

    
main()
regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()

print(mensagem_cloud)
