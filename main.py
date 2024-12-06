import pygame 
import random 

# Iniciar o pygame
pygame.init()

pygame.display.set_caption("Jogo da Cobrinha")
LARGURA, ALTURA  = 1200, 800
tela = pygame.display.set_mode((LARGURA, ALTURA))

relogio = pygame.time.Clock()

# Cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

tamanho_quadrado = 20
velocidade_jogo = 15

# Função para desenhar o texto na tela
def desenhar_texto(texto, cor, fonte, tamanho, x, y):
    fonte = pygame.font.SysFont(fonte, tamanho)
    texto_formatado = fonte.render(texto, True, cor)
    tela.blit(texto_formatado, (x, y))

# Tela inicial
def tela_inicial():
    tela.fill(preta)
    desenhar_texto("Bem-vindo ao Jogo da Cobrinha!", verde, "Coperplate", 60, LARGURA / 4.9, ALTURA / 2.8)
    desenhar_texto("Pressione Enter para começar", branca, "Coperplate", 40, LARGURA / 3.2, ALTURA / 2)
    desenhar_texto("Use as setas para mover", branca, "Coperplate", 40, LARGURA / 3, ALTURA / 1.6)
    pygame.display.update()

    esperando_inicio = True
    while esperando_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando_inicio = False

# Tela de Game Over
def game_over(pontos):
    tela.fill(preta)
    desenhar_texto(f"Game Over! Pontuação final: {pontos}", vermelha, "Coperplate", 60, LARGURA / 4.5, ALTURA / 2.8)
    desenhar_texto("Pressione Enter para reiniciar", branca, "Coperplate", 40, LARGURA / 3.2, ALTURA / 2)
    pygame.display.update()

    esperando_reiniciar = True
    while esperando_reiniciar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando_reiniciar = False
                    main()  # Reiniciar o jogo

# Função principal do jogo
def main():
    # Gera a comida inicial
    comida_x = round(random.randrange(0, LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    # Posição inicial da cabeça da cobra
    x = LARGURA / 2
    y = ALTURA / 2
    velocidade_x = 0
    velocidade_y = 0

    # Comprimento inicial da cobra
    tamanho_cobra = 1
    # Corpo da cobra
    segmentos_cobra = []

    fim_jogo = False

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = tamanho_quadrado
                elif evento.key == pygame.K_UP:
                    velocidade_x = 0
                    velocidade_y = -tamanho_quadrado
                elif evento.key == pygame.K_RIGHT:
                    velocidade_x = tamanho_quadrado
                    velocidade_y = 0
                elif evento.key == pygame.K_LEFT:
                    velocidade_x = -tamanho_quadrado
                    velocidade_y = 0

        # Atualizar a posição da cobrinha
        x += velocidade_x
        y += velocidade_y

        # Atualizar o corpo da cobrinha
        segmentos_cobra.append([x, y])
        if len(segmentos_cobra) > tamanho_cobra:
            del segmentos_cobra[0]

        # Verificar colisão com o próprio corpo
        for lista in segmentos_cobra[:-1]:
            if lista == [x, y]:
                fim_jogo = True

        # Verificar colisão na parede
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            fim_jogo = True

        # Desenhar a cobrinha
        for lista in segmentos_cobra:
            pygame.draw.rect(tela, verde, [lista[0], lista[1], tamanho_quadrado, tamanho_quadrado])

        # Desenhar a comida
        pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

        # Desenhar a pontuação
        fonte = pygame.font.SysFont("Arial", 32)
        texto = fonte.render(f"Pontos: {tamanho_cobra - 1}", True, vermelha)
        tela.blit(texto, [1, 1])

        pygame.display.update()

        # Verificar se a cobrinha comeu a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x = round(random.randrange(0, LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
            comida_y = round(random.randrange(0, ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

        relogio.tick(velocidade_jogo)

    # Tela de Game Over
    game_over(tamanho_cobra - 1)

# Iniciar o jogo com a tela inicial
tela_inicial()

# Iniciar o jogo
main()

pygame.quit()
