import pygame

def menu(screen):
    bc = "MENU"
    screen.fill([0, 0, 0])
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
               bc = "GAME"
    pygame.display.flip()
    return bc
