import pygame
import time


pygame.init()

red = (255, 255, 255)
black = (0, 0 ,0 )
size = width, height = 600, 600
font = pygame.font.Font("/usr/share/fonts/TTF/AkaashNormal.ttf", 33)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello mortal 😵😵😵😵😵😵😵")


sent_list = [
    "hello bro, welcome",
    "How are you hope youre fine ok bro",
    "Experiment 1"
]


while 1:
    screen.fill(black)
    for sent in sent_list:
        screen.fill(black)
        text = font.render(sent, True, red)

        text_rect = text.get_rect()

        text_rect.center = (600//2, 600//2)
        screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        time.sleep(2)