import pygame
import time

def desenhar_texto(texto, fonte, y):
    render = fonte.render(texto, True, 'black')
    x = (640//2) - (render.get_width()//2)
    screen.blit(render, (x, y))

class RatinhosSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, dificuldade):
        pygame.sprite.Sprite.__init__(self)
        ratinho_img  = pygame.image.load('ratinho.png').convert_alpha()
        ratinho_img = pygame.transform.scale(ratinho_img, (153//2, 66//2))
        if dificuldade == 'facil':
            self.velocidade_x = 4
        else:
            self.velocidade_x = 7
        self.image = ratinho_img
        self.rect = ratinho_img.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.x += self.velocidade_x
        if self.rect.left <= 0 or self.rect.right >= 640:
            self.velocidade_x = -self.velocidade_x
            self.image = pygame.transform.flip(self.image, True, False)

class Bolas_de_peloSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, gatinho_escolhido):
        pygame.sprite.Sprite.__init__(self)
        bolinhas_images = {
                pygame.K_1: 'bola_cinza.png',
                pygame.K_2: 'bola_marrom.png',
                pygame.K_3: 'bola_preta.png',
                pygame.K_4: 'bola_laranja.png'
            }
        if gatinho_escolhido in bolinhas_images:
            bolinhas_image = pygame.image.load(bolinhas_images[gatinho_escolhido]).convert_alpha()
            bolinhas_image = pygame.transform.scale(bolinhas_image, (701//35, 648//35))
            x_centrob = ((640//2)-(bolinhas_image.get_width()//2))-5.5
            screen.blit(bolinhas_image, (x_centrob, 360))
        self.image = bolinhas_image
        self.rect = bolinhas_image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = -9.5
        self.atirando = False

    def update(self):
        if self.atirando:
            self.rect.y += self.velocidade
            if self.rect.bottom < 0:
                self.atirando = False

pygame.init()
pygame.display.set_caption("Cats War")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

letra_grande = pygame.font.Font(None, 50)
letra_media = pygame.font.Font(None, 40)
letra_pequena = pygame.font.Font(None, 25)

tempo_limite = None

tela_atual = "inicio"

if tela_atual == "jogofacil":
    dificuldade_atual = "facil"
else:
    dificuldade_atual = "dificil"

gatinhos_images = {
    pygame.K_1: 'gatinhocinza.png',
    pygame.K_2: 'gatinhomarrom.png',
    pygame.K_3: 'gatinhopreto.png',
    pygame.K_4: 'gatinholaranja.png'
}

texto2 = letra_pequena.render("Mais um segundo!", True, 'black')
tempo_texto2 = 0

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
                    sprite_bola = Bolas_de_peloSprite(-8, -8, gatinho_escolhido)
            elif tela_atual == "dificuldade":
                if event.key in [pygame.K_1, pygame.K_2]:
                    if event.key == pygame.K_1:
                        tela_atual = "jogofacil"
                        dificuldade_atual = "facil"
                        tempo_limite = 8
                    elif event.key == pygame.K_2:
                        tela_atual = "jogodificil"
                        dificuldade_atual = "dificil"
                        tempo_limite = 4

                    tempo_inicial = pygame.time.get_ticks()    

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

                    if gatinho_escolhido in gatinhos_images:
                        gatinho_image = pygame.image.load(gatinhos_images[gatinho_escolhido]).convert_alpha()
                        gatinho_image = pygame.transform.scale(gatinho_image, (641//11, 541//11))
                        x_centro = (640//2)-(gatinho_image.get_width()//2)

            elif tela_atual in ["jogofacil", "jogodificil"]:
                if event.key == pygame.K_SPACE and sprite_bola.atirando == False:
                    sprite_bola.rect.topleft = (x_centro, 380)
                    sprite_bola.atirando = True

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

    elif tela_atual in ["jogofacil", "jogodificil"]:
        tempo_passado = (pygame.time.get_ticks()-tempo_inicial)//1000

        desenhar_texto("Tecle ESPAÇO para atirar", pygame.font.Font(None, 20), 445)
        texto = letra_pequena.render(f"Tempo: {tempo_passado}s", True, 'black')
        screen.blit(texto, (10, 440))

        sprites_ratinhos.update()
        sprites_ratinhos.draw(screen)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_centro > 0:
            x_centro -= 4
        if teclas[pygame.K_RIGHT] and x_centro < 640 - gatinho_image.get_width():
            x_centro += 4

        if sprite_bola.atirando:
            sprite_bola.update()
            screen.blit(sprite_bola.image, sprite_bola.rect.topleft)

            ratinhos_acertados = pygame.sprite.spritecollide(sprite_bola, sprites_ratinhos, True)
            if ratinhos_acertados:
                sprite_bola.atirando = False
                sprite_bola.rect.topleft = (-0, -0)
                tempo_limite += 1
                tempo_texto2 = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - tempo_texto2)//1000 < 0.04:
            screen.blit(texto2, (10, 420))

        screen.blit(gatinho_image, (x_centro, 380))

        if len(sprites_ratinhos) == 0 and tempo_passado <= tempo_limite:
            tela_atual = "vitoria"

        if len(sprites_ratinhos) > 0 and tempo_passado >= tempo_limite:
            tela_atual = "derrota"

    elif tela_atual == "vitoria":
        desenhar_texto("Parabéns! Você conseguiu", letra_media, 30)
        desenhar_texto("derrotar todos os ratos", letra_media, 55)
        desenhar_texto("inimigos!", letra_media, 80)
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
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                tela_atual = "inicio"  

    elif tela_atual == "derrota":
        desenhar_texto("O tempo acabou!", letra_media, 30)
        desenhar_texto("Os ratinhos conseguiram", letra_media, 56)
        desenhar_texto("dominar a casa dos gatinhos :(", letra_media, 80)
        desenhar_texto("Tecle ENTER para jogar novamente", letra_pequena,430)

        ratinho_derrota_img = pygame.image.load('ratinho_derrota.png').convert_alpha()
        ratinho_derrota_img = pygame.transform.scale(ratinho_derrota_img, (641//2, 541//2))
        x_centro1 = (640//2)-(ratinho_derrota_img.get_width()//2)
        y_centro1 = (480//2)-(ratinho_derrota_img.get_height()//2)
        screen.blit(ratinho_derrota_img, (x_centro1, y_centro1))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                tela_atual = "inicio"  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()