import pygame 
import random

pygame.init()

display = pygame.display.set_mode([500, 500])
timer = pygame.time.Clock()

X = 240
Y = 240
A = 240
B = 240
# COLOR
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            run = False

#player
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        X += 10 
        
    if tecla[pygame.K_a]:    
        X += -10
    
    if tecla[pygame.K_w]:
        Y += -10
            
    if tecla[pygame.K_s]:
        Y += 10
    display.fill([255, 255, 255])
    H = 20
    L = 20

    player = pygame.draw.rect(display, (0, 0, 0), [X , Y, H, L])

    rect = pygame.draw.rect(display, (0, 0, 0), [A, B, 20, 20])
    
    if X > 480:
        X = 480

    if X < 0:
        X = 0

    if Y > 480:
        Y = 480

    if Y < 0:
        Y = 0
    
    if player.colliderect(rect):
        A = random.randint(0, 480)
        B = random.randint(0, 480)
    pygame.display.flip()

pygame.quit()
