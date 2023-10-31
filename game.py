import pygame
import os

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
sSCREEN = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

RUNNING = [pygame.image.load(os.path.join('mario/', "mario_run1")), pygame.image.load(os.path.join('mario/', "mario_run2"))]

JUMPING = [pygame.image.load(os.path.join('mario/', "mario_jump"))]

MUSHROOM = [pygame.image.load(os.path.join('mush/', "mush1")), pygame.image.load(os.path.join('mush/', "mush2")), pygame.image.load(os.path.join('mush/', "mush3")), pygame.image.load(os.path.join('mush/', "mush4")), pygame.image.load(os.path.join('mush/', "mush5"))]

CLOUD = pygame.image.load(os.path.join("other/", "cloud.png"))

BG = pygame.image.load(os.path.join("other/", "background.png"))


