# Jogo de Colisão - Pontos e Vidas

Jogo 2D simples desenvolvido em Python com a biblioteca Pygame, criado durante as aulas do curso de Programação em Python do SENAI.

## Como funciona

O jogador controla um bloco azul na parte de baixo da tela. Blocos vermelhos caem do topo em posições aleatórias, e o objetivo é pegá-los antes que cheguem ao chão.

- Cada bloco pego vale 1 ponto
- Cada bloco que passa pelo jogador custa 1 vida
- O jogador começa com 3 vidas
- Quando as vidas acabam, aparece a tela de "Fim de jogo"

## Controles

| Tecla | Ação |
|-------|------|
| Seta para a esquerda | Move o jogador para a esquerda |
| Seta para a direita | Move o jogador para a direita |

## Conceitos praticados

- Loop principal de jogo (game loop) com controle de FPS
- Captura de eventos e leitura do teclado
- Movimentação de objetos e limites da tela
- Detecção de colisão com `pygame.Rect` e `colliderect`
- Geração de posições aleatórias com `random`
- Renderização de texto na tela (pontuação e vidas)
- Controle de estado do jogo (em andamento e fim de jogo)

## Tecnologias

- Python 3
- Pygame

## Como executar

1. Clone o repositório:
   git clone https://github.com/amanda-mds/pygame.git

2. Instale o Pygame:
   pip install pygame

3. Execute o jogo:
   python main.py
