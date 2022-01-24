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
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    pygame.draw.polygon(window, red, ((491, 100), (788, 100), (937, 357),
                        (788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window, green, (640, 360), 200) # surface, color, center, radius
    pygame.draw.line(window, blue, (468, 392), (812, 392), 10)


    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)