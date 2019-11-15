import pygame
import random
from pprint import pprint

pygame.init()
WINDOW_WIDTH = 1252;
WINDOW_HEIGHT = 834;
pandaSize = 100;
appleSize = 70;
background = pygame.image.load('../resources/images/background.jpg')
background = pygame.transform.scale2x(background)
pandaImg = pygame.image.load('../resources/images/BabyPanda.png')
pandaImg = pygame.transform.scale(pandaImg, (pandaSize, pandaSize))
appleImg = pygame.image.load('../resources/images/apple.png')
appleImg = pygame.transform.scale(appleImg, (appleSize, appleSize))



win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Panda Game")
clock = pygame.time.Clock()
run = True

class Wall():
    def __init__(self, objects):
        isWide = random.getrandbits(1)
        while True:
            collided = False
            if isWide:
                width = random.randint(WINDOW_WIDTH//5, WINDOW_WIDTH//2)
                height = random.randint(WINDOW_WIDTH//40, WINDOW_WIDTH//10)
            else:
                height = random.randint(WINDOW_WIDTH//5, WINDOW_WIDTH//2)
                width = random.randint(WINDOW_WIDTH//40, WINDOW_WIDTH//10)
            x = random.randint(32, WINDOW_WIDTH - width)
            y = random.randint(32, WINDOW_HEIGHT - height)
            self.rect = pygame.Rect(x, y, width, height)
            for object in objects:
                if self.rect.colliderect(object.rect):
                    collided = True
                    break
            if collided is False:
                break

    def draw(self, win):
        pygame.draw.rect(win, (203, 65, 84), self.rect)

class Character():
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.rect = pygame.Rect(x, y, image.get_rect().size[0], image.get_rect().size[1])
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

def generateMap():
    map = [['.' for i in range(WINDOW_WIDTH)] for j in range(WINDOW_HEIGHT)]
    for wall in walls:
        for x in range(wall.x - pandaImg.get_rect().size[0], wall.x + wall.width):
            for y in range(wall.y - pandaImg.get_rect().size[0], wall.y + wall.height):
                map[y][x] = '#'
    return map;

def drawPath():
    path = getPath()
    for y, row in enumerate(path):
        for x, col in enumerate(row):
            if path[y][x] == '*'
            pygame.draw.circle(win, (0, 0, 255), (x + pandaSize/2, y + pandaSize/2), 5)

def mainDraw():
    win.blit(background, (0,0))
    for wall in walls:
        wall.draw(win)
    drawPath()
    adultPanda.draw(win)
    apple.draw(win)
    pygame.display.update()

adultPanda = Character(pandaImg, 0, 0)
apple = Character(appleImg, WINDOW_WIDTH - appleImg.get_rect().size[0] - 20, WINDOW_HEIGHT - appleImg.get_rect().size[1] - 20)
objects = [adultPanda, apple]
walls = []
for x in range(random.randint(4, 7)):
    walls.append(Wall(objects))
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                walls.clear()
                for x in range(random.randint(4, 7)):
                    walls.append(Wall(objects))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    mainDraw()


pygame.quit()
