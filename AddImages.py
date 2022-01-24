import pygame

pygame.init()

w, h = 1280, 720
window = pygame.display.set_mode((w, h))

pygame.display.set_caption('My Game')

fps = 30
clock = pygame.time.Clock()

# Load Images
imgBackground = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\BackgroundBlue.jpg').convert()
imgBalloonRed = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\BalloonRed.png').convert_alpha()

start = True

while start:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    window.fill((255, 255, 255))
    window.blit(imgBalloonRed, (500, 500))
    window.blit(imgBackground, (0, 0))


    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)