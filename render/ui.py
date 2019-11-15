import pygame
import random
from pprint import pprint

pygame.init()
WINDOW_WIDTH = 1252
WINDOW_HEIGHT = 834
pandaSize = 100
appleSize = 70
background = pygame.image.load('./resources/images/background.jpg')
background = pygame.transform.scale2x(background)
pandaImg = pygame.image.load('./resources/images/BabyPanda.png')
pandaImg = pygame.transform.scale(pandaImg, (pandaSize, pandaSize))
appleImg = pygame.image.load('./resources/images/apple.png')
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
                self.width = random.randint(WINDOW_WIDTH // 5, WINDOW_WIDTH // 2)
                self.height = random.randint(WINDOW_WIDTH // 40, WINDOW_WIDTH // 10)
            else:
                self.height = random.randint(WINDOW_WIDTH // 5, WINDOW_WIDTH // 2)
                self.width = random.randint(WINDOW_WIDTH // 40, WINDOW_WIDTH // 10)
            self.x = random.randint(32, WINDOW_WIDTH - self.width)
            self.y = random.randint(32, WINDOW_HEIGHT - self.height)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
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


def generateMap(walls):
    map = [['.' for i in range(WINDOW_WIDTH)] for j in range(WINDOW_HEIGHT)]
    for wall in walls:
        for x in range(wall.x - pandaImg.get_rect().size[0], wall.x + wall.width):
            for y in range(wall.y - pandaImg.get_rect().size[1], wall.y + wall.height):
                map[y][x] = '#'
    return map


def renderPath(path):
    for point in path:
        pygame.draw.circle(win, (0, 0, 255), (point[0] + pandaSize // 2, point[1] + pandaSize // 2), 5)


def changeMap(objects):
    walls = []
    for x in range(random.randint(4, 7)):
        walls.append(Wall(objects))
    return walls


def renderPanda(pos):
    adultPanda = Character(pandaImg, pos[0], pos[1])
    adultPanda.draw(win)
    return adultPanda


def renderApple(pos):
    apple = Character(appleImg, WINDOW_WIDTH - appleImg.get_rect().size[0] - 20,
                      WINDOW_HEIGHT - appleImg.get_rect().size[1] - 20)
    apple.draw(win)
    return apple


def renderWalls(walls):
    for wall in walls:
        wall.draw(win)


def renderBackground():
    win.blit(background, (0, 0))


def renderComplete():
    font = pygame.font.SysFont("comicsansms", 100)
    text = font.render("Panda Got the Apple!!", True, (255, 165, 0))
    win.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))


def setFramerate(rate):
    clock.tick(rate)

def updateScreen():
    pygame.display.update()

'''
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                changeMap()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    renderBackground()
    panda = renderPanda((0, 0))
    apple = renderApple((WINDOW_WIDTH - appleSize//2, WINDOW_HEIGHT - appleSize//2))
    walls = changeMap([apple, panda])
    renderWalls(walls)
    renderComplete()
    pygame.display.update()

pygame.quit()
'''
