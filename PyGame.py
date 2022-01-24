import pygame

pygame.init()

w, h = 1280, 720
window = pygame.display.set_mode((w, h))

pygame.display.set_caption('My Game')

fps = 30
clock = pygame.time.Clock()

start = True

while start:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    window.fill((255, 255, 255))

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)