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

    # Apply logic
    window.fill((255, 255, 255))
    font = pygame.font.Font('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\Cardo98s.ttf', 100)
    text = font.render("My Awesome Game", True, (50, 50, 50))
    window.blit(text, (350, 300))

    # Update display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)