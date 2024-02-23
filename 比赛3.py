import pygame

pygame.init()
screen = pygame.display.set_mode((750, 750))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#EE9A49")

    for x in range(15):
        pygame.draw.line(screen, "#000000", [25 + 50 * x, 25], [25 + 50 * x, 725], 2)
    for y in range(15):
        pygame.draw.line(screen, "#000000", [25,25+50 * y,], [725 , 25+50 * y], 2)



    pygame.display.update()

pygame.quit()



