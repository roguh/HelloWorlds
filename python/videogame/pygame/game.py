import random
import sys

import pygame
from pygame import KEYDOWN, QUIT, display, event, time
from pygame.image import load


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0


screen = display.set_mode((640, 480))
player = load('player.bmp').convert()
background = load('player.bmp').convert()
screen.blit(background, (0, 0))
objects = [
    GameObject(player, random.randint(0, 300), random.randint(1, 5))
    for x in range(10)
]
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    display.update()
    time.delay(100)
