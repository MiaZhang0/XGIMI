import pygame

pygame.init()
windowSurface = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
myString = "Hello World!"
font = pygame.font.SysFont("Times New Roman", 48)
text = font.render(myString, True, WHITE)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    windowSurface.blit(text, (200, 250))
    pygame.display.update()
pygame.quit()
