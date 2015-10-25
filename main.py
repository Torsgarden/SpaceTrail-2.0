import pygame, sys
from pygame.locals import *

class buttons:
    def __init__(self, x, y, w, h, color, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.action = action

def button_action():
    pygame.quit()
    sys.exit()

def input(button_queue):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            for b in button_queue:
                if mousex >= b.x and mousey >= b.y and mousex <= b.x + b.w and mousey <= b.x + b.h:
                    b.action()

def update(window, button_queue):
    # fill screen with white
    window.fill((255, 255, 255))
    for b in button_queue:
        pygame.draw.rect(window, b.color, (b.x, b.y, b.w, b.h))

    pygame.display.update()

def main():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    button_queue = []
    button_queue.append(buttons(100, 100, 100, 100, (0, 0, 0), button_action))
    while True:
        input(button_queue)
        update(window, button_queue)

main()
