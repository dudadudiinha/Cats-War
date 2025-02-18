import pygame

class RatinhosSprite(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    ratinho_img  = pygame.image.load('ratinho.png').convert_alpha()
    ratinho_img = pygame.transform.scale(ratinho_img, (230//3, 100//3))
    self.image = ratinho_img
    self.rect = ratinho_img.get_rect()
    self.rect.topleft = (x, y)
    # ver como fazer a locomoção dos ratos
'''
# tentanto enter esse trecho do código de Alexandre e como ele pode contribuir para o código
class GatinhoSprite(pygame.sprite.Sprite):
  def __init__(self, img):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load('pacman.png').convert_alpha()
    self.img_1 = pygame.transform.scale(img, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.topleft = (320, 430)
    # variáveis para controlar a movimentação do pacman
    self.velocidade = 5
    self.sentido = 1 # 1 = para a direita, -1 = para a esquerda
    '''

def desenhar_texto(texto, fonte, cor, y):
    render = fonte.render(texto, True, cor)
    x = (640//2) - (render.get_width()//2)
    screen.blit(render, (x, y))

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

letra_grande = pygame.font.Font(None, 50)
letra_pequena = pygame.font.Font(None, 25)

lista_ratinhos = [RatinhosSprite(250, 5), RatinhosSprite(10, 100), RatinhosSprite(500, 50), RatinhosSprite(190, 150), RatinhosSprite(400, 200), RatinhosSprite(80, 250), RatinhosSprite(300, 300)]
sprites_ratinhos = pygame.sprite.Group([lista_ratinhos])

gatinho_escolhido = None

tela_atual = "inicio" 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if tela_atual == "inicio" and event.key == pygame.K_RETURN:
                tela_atual = "selecao"
            elif tela_atual == "selecao":
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    gatinho_escolhido = event.key
                    tela_atual = "dificuldade"
            elif tela_atual == "dificuldade":
                if event.key in [pygame.K_1, pygame.K_2]:
                    if event.key == pygame.K_1:
                        tela_atual = "jogofacil"
                    elif event.key == pygame.K_2:
                        tela_atual = "jogodificil"
            elif tela_atual == "jogofacil":
                if event.key == pygame.K_w:
                    tela_atual = "vitoria" # tá assim só pra dar pra ver a tela tanto de vitória quanto derrota
                elif event.key == pygame.K_x: 
                    tela_atual = "derrota" # mudar esses elif's por completo depois
            elif tela_atual == "jogodificil":
                if event.key == pygame.K_w:
                    tela_atual = "vitoria"
                elif event.key == pygame.K_x: 
                    tela_atual = "derrota"
            elif tela_atual in ["vitoria", "derrota"] and event.key == pygame.K_RETURN:
                tela_atual = "inicio"  

    screen.fill((255, 255, 255))

    if tela_atual == "inicio":
        desenhar_texto("Cats War", letra_grande, (0, 0, 0), 30)
        desenhar_texto("Ajude os gatinhos a derrotar", letra_pequena, (0, 0, 0), 65)
        desenhar_texto("os ratinhos do mal!", letra_pequena, (0, 0, 0), 81)
        desenhar_texto("Pressione ENTER para começar", letra_pequena, (0, 0, 0), 400)

        gatinhos_img = pygame.image.load('gatinhos.png').convert_alpha()
        gatinhos_img = pygame.transform.scale(gatinhos_img, (461, 101))

        x_base = (640//2) - (gatinhos_img.get_width()//2)
        y_base = (480//2) - (gatinhos_img.get_height()//2)

        screen.blit(gatinhos_img, (x_base, y_base))

    elif tela_atual == "dificuldade":
        desenhar_texto("Dificuldade do jogo:", letra_grande, (0, 0, 0), 10)
        escolha = desenhar_texto("1 - Fácil | 2 - Difícil", letra_pequena, (0, 0, 0), 240)

    elif tela_atual == "selecao":
        desenhar_texto("Escolha seu gatinho!", letra_grande, (0, 0, 0), 30)
        desenhar_texto("1 - Cinza    |   2 - Siamês   |   3 - Preto   |    4 - Laranja   ", letra_pequena, (0, 0, 0), 155)

        gatinhos_img = pygame.image.load('gatinhos.png').convert_alpha()
        gatinhos_img = pygame.transform.scale(gatinhos_img, (461, 101))

        x_base = (640//2) - (gatinhos_img.get_width()//2)
        y_base = (480//2) - (gatinhos_img.get_height()//2)

        screen.blit(gatinhos_img, (x_base, y_base))

    elif tela_atual == "jogofacil":
        '''hit_list = pygame.sprite.spritecollide(pacman, sprites_cerejas, True)
        todos_sprites.remove(hit_list)
        sprites_cerejas.remove(hit_list)

        todos_sprites.update() # chama a função update de todos os sprites

        screen.fill((255, 255, 255)) # limpa a tela'''

        sprites_ratinhos.draw(screen)

    elif tela_atual == "jogodificil":

        sprites_ratinhos.draw(screen)

    elif tela_atual == "vitoria":
        desenhar_texto("Você venceu!", letra_grande, (0, 0, 0), 30)
        desenhar_texto("Tecle ENTER para jogar novamente", letra_pequena, (0, 0, 0), 430)

        imagens_gatinhos = {
            pygame.K_1: 'gatocinza_vitoria.png',
            pygame.K_2: 'gatomarrom_vitoria.png',
            pygame.K_3: 'gatopreto_vitoria.png',
            pygame.K_4: 'gatolaranja_vitoria.png'
        }
        
        if gatinho_escolhido in imagens_gatinhos:
            gatinho_img = pygame.image.load(imagens_gatinhos[gatinho_escolhido]).convert_alpha()
            gatinho_img = pygame.transform.scale(gatinho_img, (641//2, 541//2))
            x_centro = (640//2)-(gatinho_img.get_width()//2)
            y_centro = (480//2)-(gatinho_img.get_height()//2)
            screen.blit(gatinho_img, (x_centro, y_centro))

        '''gatopretov_img = pygame.image.load('gatopreto_vitoria.png').convert_alpha()
        gatopretov_img = pygame.transform.scale(gatopretov_img, (641//2, 541//2))
        x_centro = (640//2)-(gatopretov_img.get_width()//2)
        y_centro = (480//2)-(gatopretov_img.get_height()//2)
        screen.blit(gatopretov_img, (x_centro, y_centro))'''

    elif tela_atual == "derrota":
        desenhar_texto("Você perdeu!", letra_grande, (0, 0, 0), 30)
        desenhar_texto("Tecle ENTER para jogar novamente", letra_pequena, (0, 0, 0), 430)

        ratinho_derrota_img = pygame.image.load('ratinho_derrota.png').convert_alpha()
        ratinho_derrota_img = pygame.transform.scale(ratinho_derrota_img, (641//2, 541//2))
        x_centro1 = (640//2)-(ratinho_derrota_img.get_width()//2)
        y_centro1 = (480//2)-(ratinho_derrota_img.get_height()//2)
        screen.blit(ratinho_derrota_img, (x_centro1, y_centro1))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()