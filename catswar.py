import pygame

def desenhar_texto(texto, fonte, y):
    render = fonte.render(texto, True, 'black')
    x = (640//2) - (render.get_width()//2)
    screen.blit(render, (x, y))

class RatinhosSprite(pygame.sprite.Sprite):
  def __init__(self, x, y, dificuldade):
    pygame.sprite.Sprite.__init__(self)
    ratinho_img  = pygame.image.load('ratinho.png').convert_alpha()
    ratinho_img = pygame.transform.scale(ratinho_img, (153//2, 66//2))
    print(dificuldade)
    if dificuldade == 'facil':
        self.velocidade_x = 3
    else:
        self.velocidade_x = 6
    self.image = ratinho_img
    self.rect = ratinho_img.get_rect()
    self.rect.topleft = (x, y)

  def update(self):
    self.rect.x += self.velocidade_x
    if self.rect.left <= 0 or self.rect.right >= 640:
        self.velocidade_x = -self.velocidade_x

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

letra_grande = pygame.font.Font(None, 50)
letra_pequena = pygame.font.Font(None, 25)

tela_atual = "inicio"

if tela_atual == "jogofacil":
    dificuldade_atual = "facil"
else:
    dificuldade_atual = "dificil"

gatinho_escolhido = None

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
                        dificuldade_atual = "facil"
                    elif event.key == pygame.K_2:
                        tela_atual = "jogodificil"
                        dificuldade_atual = "dificil"

                    lista_ratinhos = [
                        RatinhosSprite(250, 5, dificuldade_atual),
                        RatinhosSprite(10, 100, dificuldade_atual),
                        RatinhosSprite(500, 50, dificuldade_atual),
                        RatinhosSprite(190, 150, dificuldade_atual),
                        RatinhosSprite(400, 200, dificuldade_atual),
                        RatinhosSprite(80, 250, dificuldade_atual),
                        RatinhosSprite(300, 300, dificuldade_atual)
                    ]
                    sprites_ratinhos = pygame.sprite.Group(lista_ratinhos)

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
        desenhar_texto("Cats War", letra_grande, 30)
        desenhar_texto("Ajude os gatinhos a derrotar", letra_pequena, 65)
        desenhar_texto("os ratinhos do mal!", letra_pequena, 81)
        desenhar_texto("Pressione ENTER para começar", letra_pequena, 400)

        gatinhos_img = pygame.image.load('gatinhos.png').convert_alpha()
        gatinhos_img = pygame.transform.scale(gatinhos_img, (461, 101))

        x_base = (640//2) - (gatinhos_img.get_width()//2)
        y_base = (480//2) - (gatinhos_img.get_height()//2)

        screen.blit(gatinhos_img, (x_base, y_base))

    elif tela_atual == "dificuldade":
        desenhar_texto("Dificuldade do jogo:", letra_grande, 10)
        escolha = desenhar_texto("1 - Fácil | 2 - Difícil", letra_pequena, 240)

    elif tela_atual == "selecao":
        desenhar_texto("Escolha seu gatinho!", letra_grande, 30)
        desenhar_texto("1 - Cinza    |   2 - Siamês   |   3 - Preto   |    4 - Laranja   ", letra_pequena, 155)

        gatinhos_img = pygame.image.load('gatinhos.png').convert_alpha()
        gatinhos_img = pygame.transform.scale(gatinhos_img, (461, 101))

        x_base = (640//2) - (gatinhos_img.get_width()//2)
        y_base = (480//2) - (gatinhos_img.get_height()//2)

        screen.blit(gatinhos_img, (x_base, y_base))

    elif tela_atual == "jogofacil":
        desenhar_texto("Tecle ESPAÇO para atirar", pygame.font.Font(None, 20), 445)

        sprites_ratinhos.update()
        sprites_ratinhos.draw(screen)

        gatinhos_images = {
            pygame.K_1: 'gatinhocinza.png',
            pygame.K_2: 'gatinhomarrom.png',
            pygame.K_3: 'gatinhopreto.png',
            pygame.K_4: 'gatinholaranja.png'
        }
       
        if gatinho_escolhido in gatinhos_images:
            gatinho_image = pygame.image.load(gatinhos_images[gatinho_escolhido]).convert_alpha()
            gatinho_image = pygame.transform.scale(gatinho_image, (641//11, 541//11))
            x_centro = (640//2)-(gatinho_image.get_width()//2)
            screen.blit(gatinho_image, (x_centro, 380))

        bolinhas_images = {
            pygame.K_1: 'bola_cinza.png',
            pygame.K_2: 'bola_marrom.png',
            pygame.K_3: 'bola_preta.png',
            pygame.K_4: 'bola_laranja.png'
        }
       
        if gatinho_escolhido in gatinhos_images:
            bolinhas_image = pygame.image.load(bolinhas_images[gatinho_escolhido]).convert_alpha()
            bolinhas_image = pygame.transform.scale(bolinhas_image, (701//35, 648//35))
            x_centrob = ((640//2)-(bolinhas_image.get_width()//2))-5.5
            screen.blit(bolinhas_image, (x_centrob, 360))

    elif tela_atual == "jogodificil":
        desenhar_texto("Tecle ESPAÇO para atirar", pygame.font.Font(None, 20), 445)

        sprites_ratinhos.update()
        sprites_ratinhos.draw(screen)

        gatinhos_images = {
            pygame.K_1: 'gatinhocinza.png',
            pygame.K_2: 'gatinhomarrom.png',
            pygame.K_3: 'gatinhopreto.png',
            pygame.K_4: 'gatinholaranja.png'
        }
       
        if gatinho_escolhido in gatinhos_images:
            gatinho_image = pygame.image.load(gatinhos_images[gatinho_escolhido]).convert_alpha()
            gatinho_image = pygame.transform.scale(gatinho_image, (641//11, 541//11))
            x_centro = (640//2)-(gatinho_image.get_width()//2)
            screen.blit(gatinho_image, (x_centro, 380))

        bolinhas_images = {
            pygame.K_1: 'bola_cinza.png',
            pygame.K_2: 'bola_marrom.png',
            pygame.K_3: 'bola_preta.png',
            pygame.K_4: 'bola_laranja.png'
        }
       
        if gatinho_escolhido in gatinhos_images:
            bolinhas_image = pygame.image.load(bolinhas_images[gatinho_escolhido]).convert_alpha()
            bolinhas_image = pygame.transform.scale(bolinhas_image, (701//35, 648//35))
            x_centrob = ((640//2)-(bolinhas_image.get_width()//2))-5.5
            screen.blit(bolinhas_image, (x_centrob, 360))

    elif tela_atual == "vitoria":
        desenhar_texto("Você venceu!", letra_grande, 30)
        desenhar_texto("Tecle ENTER para jogar novamente", letra_pequena, 430)

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

    elif tela_atual == "derrota":
        desenhar_texto("Você perdeu!", letra_grande, 30)
        desenhar_texto("Tecle ENTER para jogar novamente", letra_pequena,430)

        ratinho_derrota_img = pygame.image.load('ratinho_derrota.png').convert_alpha()
        ratinho_derrota_img = pygame.transform.scale(ratinho_derrota_img, (641//2, 541//2))
        x_centro1 = (640//2)-(ratinho_derrota_img.get_width()//2)
        y_centro1 = (480//2)-(ratinho_derrota_img.get_height()//2)
        screen.blit(ratinho_derrota_img, (x_centro1, y_centro1))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()