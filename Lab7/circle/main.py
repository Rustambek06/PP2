import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
done = False
clock = pygame.time.Clock()
w, h = screen.get_size()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and h / 2 - 20 > 0:
                h -= 40
            elif event.key == pygame.K_DOWN and h / 2 + 20 < 800:
                h += 40
            elif event.key == pygame.K_RIGHT and w / 2 + 20 < 800:
                w += 40
            elif event.key == pygame.K_LEFT and w / 2 - 20 > 0:
                w -= 40



    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (w/2, h/2), 25)

    pygame.display.flip()
    clock.tick(60)