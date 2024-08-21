import pygame

pygame.init()

# Jokuaren pantaila hasieratu
screen = pygame.display.set_mode([500, 500])

# Jokua etengabe egikaritzeko begizta
running = True
while running:

    # Erabiltzaileak ixteko botoia sakatzen duenean
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pantaila zuri kolorez bete
    screen.fill((255, 255, 255))

    # Zirkulu bat marraztu
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Pantailari buelta eman
    pygame.display.flip()

# Amaiera
pygame.quit()
