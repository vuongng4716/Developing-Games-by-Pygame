import pygame

pygame.init()

w, h = 1280, 720
window = pygame.display.set_mode((w, h))

pygame.display.set_caption('GUI')

fps = 30
clock = pygame.time.Clock()

# Colors
c = {"LightGreen": (189, 209, 197),
     "LightOrange": (238, 204, 140),
     "LightPink": (232, 178, 152),
     "darkPink": (211, 162, 157),
     "darkGreen": (158, 171, 162),
     "darkGray": (128, 126, 126),
     "LightGray": (204, 204, 204),
     "darkBrown": (89, 61, 61),
     "white": (255, 255, 255),
     "black": (0, 0, 0)
     }

# Images
imgBackground = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\background.png').convert()
imgDesign = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\design.png').convert_alpha()
imgIcon1 = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\icon1.png').convert_alpha()
imgIcon2 = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\icon2.png').convert_alpha()
imgIcon3 = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\icon3.png').convert_alpha()
imgIcon4 = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\icon4.png').convert_alpha()
imgIcon5 = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\icon5.png').convert_alpha()
imgShadow = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\shadow.png').convert_alpha()
imgToggleOn = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\toggleOn.png').convert_alpha()
imgToggleOff = pygame.image.load('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Project - GUI\\toggleOff.png').convert_alpha()

# List of WindowPads

pads = [{"no": 1, "color": c['LightGreen'], "text": "Original", "icon":imgIcon2},
        {"no": 2, "color": c['LightOrange'], "text": "Gray Scale", "icon":imgIcon3},
        {"no": 3, "color": c['LightPink'], "text": "Edges", "icon":imgIcon4},
        {"no": 4, "color": c['darkPink'], "text": "Colors", "icon":imgIcon5}]

def drawWindowPad(pos, color, text, icon):
    xo, yo, w, h = pos
    window.blit(imgShadow, (xo, yo+h-66))

    # Header rectangle
    pygame.draw.rect(window, color, (xo, yo, w, 64),
                     border_top_left_radius=10, border_top_right_radius=10)

    # Image area White
    pygame.draw.rect(window, c['white'], (xo, yo+64, w, h-87),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)

    # Icon
    window.blit(icon, (xo + 20, yo + 12))
    # Text
    font = pygame.font.Font('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\Cardo98s.ttf', 20)
    text = font.render(text, True, c['darkBrown'])
    window.blit(text, (xo+82, yo+20))

def drawFilterPad():
    drawWindowPad((75, 57, 312, 602), c["darkGreen"], "Filter", imgIcon1)

    # Toggles
    font = pygame.font.Font('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\Cardo98s.ttf', 20)

    # 1
    textDisp1 = font.render("Gray Scale", True, c["darkBrown"])
    window.blit(textDisp1, (106, 165))
    window.blit(imgToggleOn, (283, 164))

    # 2
    textDisp2 = font.render("Edges", True, c["darkBrown"])
    window.blit(textDisp2, (106, 165 + 60))
    window.blit(imgToggleOn, (283, 164 + 60))

    # 3
    textDisp3 = font.render("Contours", True, c["darkBrown"])
    window.blit(textDisp3, (106, 165+120))
    window.blit(imgToggleOff, (283, 164+120))

    # 4
    textDisp4 = font.render("Blur", True, c["darkBrown"])
    window.blit(textDisp4, (106, 165+180))
    window.blit(imgToggleOff, (283, 164+180))

    # Sliders
    font = pygame.font.Font('C:\\Users\\ThinkPad\\PycharmProjects\\Game-Dev\\Resources\\Cardo98s.ttf', 20)
    for y in range(0, 3):
        h = 447 + y * 55
        sliderPos = 105 + 50 * y + 30
        pygame.draw.line(window, c["LightGray"], (105, h), (105+155, h), 5)
        pygame.draw.line(window, c["darkGray"], (105, h), (sliderPos, h), 5)
        pygame.draw.rect(window, c["darkGray"], (sliderPos, h-15, 12, 30))
        textDisp = font.render(str(y*50+30), True, c['darkBrown'])
        window.blit(textDisp, (286, h - 18))

def drawAll():
    w, h = 312, 301
    gapW, gapH = 72, 25
    drawWindowPad((484, 57, w, h), pads[0]['color'], pads[0]['text'], pads[0]['icon'])
    drawWindowPad((484+gapW+w, 57, w, h), pads[1]['color'], pads[1]['text'], pads[1]['icon'])
    drawWindowPad((484, 57+gapH+h, w, h), pads[2]['color'], pads[2]['text'], pads[2]['icon'])
    drawWindowPad((484 + gapW + w, 57+gapH+h, w, h), pads[3]['color'], pads[3]['text'], pads[3]['icon'])

    drawFilterPad()


start = True
while start:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic

    window.blit(imgBackground, (0, 0))
    imgDesign.set_alpha(50)
    window.blit(imgDesign, (0, 0))

    drawAll()

    # update display
    pygame.display.update()

    # set FPS
    clock.tick(fps)