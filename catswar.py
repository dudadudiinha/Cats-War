import pygame

def imagens():
    gatinhos_img = pygame.image.load('gatinhos.png').convert_alpha()
    gatinhos_img = pygame.transform.scale(gatinhos_img, (100, 100))
    gatolaranja_img = pygame.image.load('gatolaranja.png').convert_alpha()
    gatolaranja_img = pygame.transform.scale(gatolaranja_img, (100, 100))
    gatopreto_img = pygame.image.load('gatopreto.png').convert_alpha()
    gatopreto_img = pygame.transform.scale(gatopreto_img, (100, 100))
    gatocinza_img = pygame.image.load('gatocinza.png').convert_alpha()
    gatocinza_img = pygame.transform.scale(gatocinza_img, (100, 100))
    gatomarrom_img = pygame.image.load('gatomarrom.png').convert_alpha()
    gatomarrom_img = pygame.transform.scale(gatomarrom_img, (100, 100))

while True:
    