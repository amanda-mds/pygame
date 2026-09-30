import pygame
import random

pygame.init()

LARGURA, ALTURA = (400
                       , 400)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de colisão - Pontos e vidas")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0 ,255)
VERMELHO = (255, 0, 0)

fonte = pygame.font.SysFont("Arial", 40)
fonte_grande = pygame.font.SysFont("Arial", 60)

jogador = pygame.Rect(275,350,50,30)
velocidade = 6
alvo = pygame.Rect(random.randint(0, LARGURA - 30), 0, 30, 30)
velocidade_alvo = 4

pontos = 9999
vidas = 3
relogio = pygame.time.Clock()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    teclas = pygame.key.get_pressed()
    if vidas > 0:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador.left > 0:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT] and jogador.right < LARGURA:
            jogador.x += velocidade

        alvo.y += velocidade_alvo

        if alvo.top > ALTURA:
            alvo.x = random.randint(0, LARGURA - 30)
            alvo.y = 0
            vidas -= 1

        if jogador.colliderect(alvo):
            pontos += 1
            alvo.x = random.randint(0, LARGURA - 30)
            alvo.y = 0

    tela.fill(BRANCO)
    if vidas > 0:
        pygame.draw.rect(tela, AZUL, jogador)
        pygame.draw.rect(tela, VERMELHO, alvo)

        texto = fonte.render("Pontos: " + str(pontos), True, PRETO)
        tela.blit(texto, (10, 10))

        texto_vidas = fonte.render("Vidas: " + str(vidas), True, VERMELHO)
        tela.blit(texto_vidas, (LARGURA - 170, 10))

    else:
        texto_fim = fonte_grande.render("Fim de jogo", True, PRETO)
        tela.blit(texto_fim, (LARGURA // 2 - 160, ALTURA // 2 - 30))

    pygame.display.flip()

    relogio.tick(60)
pygame.quit()