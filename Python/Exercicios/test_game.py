import pygame, random

pygame.init()

screen = pygame.display.set_mode([500, 500])
timer = pygame.time.Clock()

x = 240
y = 240
a = 240
b = 240
red = 255 
green = 255
blue = 255
run = True

while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        x += -10

    if key[pygame.K_d]:
        x += 10

    if key[pygame.K_w]:
        y += -10

    if key[pygame.K_s]:
        y += 10
    if key[pygame.K_ESCAPE]:
        run = False

    screen.fill([0, 0, 0])
    player = pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))

    food = pygame.draw.rect(screen, (red, green, blue), (a, b, 20, 20))

    if player.colliderect(food):
        a = random.randint(20, 480)
        b = random.randint(20, 480)
        red = random.randint(0, 255)
        gren = random.randint(0, 255)
        blue = random.randint(0, 255)

    pygame.display.flip()
pygame.quit()