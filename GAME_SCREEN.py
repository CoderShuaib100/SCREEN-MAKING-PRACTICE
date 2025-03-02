# Welcome!
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("First Game Screen (FGS)")
background = pygame.transform.scale(pygame.image.load('BACKGROUND.jpg').convert(),(SCREEN_WIDTH + 100,SCREEN_HEIGHT + 20))
codingal_logo = pygame.transform.scale(pygame.image.load('LOGO.png').convert(),(280,152.8))
C_logo_rect = codingal_logo.get_rect()
login_in_ui = pygame.transform.scale(pygame.image.load('login_ui.png').convert(),(307,200))
LUI_rect = login_in_ui.get_rect()

# FPS runner
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(background,(0,0))
    display_surface.blit(codingal_logo,(260,100))
    display_surface.blit(login_in_ui,(246.5,300))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
