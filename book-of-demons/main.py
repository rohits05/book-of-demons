import pygame
import time


pygame.init()

red = (255, 255, 255)
green = (24, 202, 77)
black = (0, 0 ,0 )
size = width, height = 600, 600
font = pygame.font.Font("/usr/share/fonts/TTF/AkaashNormal.ttf", 33)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello mortal 😵😵😵😵😵😵😵")


sent_list = [
    "wecome to book of demon!",
    "In this game you are trying to save the world",
    "You have to fight and defeat demons",
    "to save everyone",
    "Tell me your name"
]


while 1:
    screen.fill(black)
    for sent in sent_list:
        screen.fill(black)
        text = font.render(sent, True, green)

        text_rect = text.get_rect()

        text_rect.center = (600//2, 600//2)
        screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # print(event)
        pygame.display.flip()
        time.sleep(2)