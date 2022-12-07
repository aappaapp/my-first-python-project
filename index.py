import sys
import pygame


# Parker Odinson - Hello To A World
print("HI WORLD!!!")


# Classes
class Object:
    objectList = []

    @staticmethod
    def updateAll():
        for object in Object.objectList:
            object.update()

    def __init__(self):
        self.object = pygame.image.load(self.fileName)
        self.rect = self.object.get_rect()
        Object.objectList.append(self)

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.object, self.rect)


class Ball(Object):
    def __init__(self, startX, startY):
        self.fileName = "ball.png"
        self.speed = [1, 1]
        super().__init__()
        self.rect.topleft = (startX, startY)

    def update(self):
        self.move()
        super().update()

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > size[0]:
            self.speed[0] = -self.speed[0]
            if self.rect.right > size[0]:
                self.rect = self.rect.move(-1, 0)
            else:
                self.rect = self.rect.move(1, 0)
        if self.rect.top < 0 or self.rect.bottom > size[1]:
            self.speed[1] = -self.speed[1]
            if self.rect.bottom > size[1]:
                self.rect = self.rect.move(-1, 0)
            else:
                self.rect = self.rect.move(1, 0)


# Variables
size = [400, 400]


# Long Mode Detection
longDefined = False

while not longDefined:
    long = input("Long Mode:(y/n) ")
    if long == "y":
        long = True
        longDefined = True
    elif long == "n":
        long = False
        longDefined = True

if not long:
    Ball(0, 0)
    Ball(50, 50)


# Pygame Init
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load("ball.png"))
pygame.display.set_caption("HI BALLS!!")


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if long:
        Ball(0, 0)
    screen.fill((0, 0, 0))
    Object.updateAll()
    pygame.display.flip()
    pygame.display.set_mode(size)

    if size[0] > 100:
        size[0] -= 0.1
