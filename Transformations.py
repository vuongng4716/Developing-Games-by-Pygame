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
pygame.transform.flip(imgBalloonRed, True, False)
start = True

while start:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic

    imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 90, 0.3)

    window.blit(imgBackground, (0, 0))
    window.blit(imgBalloonRed, (500, 500))

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)