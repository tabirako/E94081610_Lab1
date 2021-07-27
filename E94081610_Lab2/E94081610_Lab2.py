from typing import Union

import pygame
import time
import math

from pygame.font import Font
from pygame.surface import SurfaceType, Surface

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

# load image (background, enemy, buttons)
# background
base_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
# enemy
enemy = pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))
# hp
img_hp = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
# hp_gray
img_hp_gray = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
# buttons
img_mute = pygame.transform.scale(pygame.image.load("images/mute.png"), (BTN_WIDTH, BTN_WIDTH))
img_sound = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_WIDTH))
img_continue = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_WIDTH))
img_pause = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_WIDTH))

# create window surface

pygame.display.set_caption("My first game")

# clock
clock = pygame.time.Clock()


class Game:

    def __init__(self):
        # windows

        self.font1 = pygame.font.SysFont('timesnewroman', 25)
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10

        # time
        self.init_time = time.time()
        self.curr_time = time.time() - self.init_time

    def game_run(self):
        # game loop
        run = True
        while run:

            clock.tick(FPS)
            # event loop (user action)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            self.win.fill(WHITE)
            self.win.blit(base_image, (0, 0))

            # draw enemy and health bar

            pygame.draw.rect(self.win, RED, [50, 250, 50, 10])
            self.win.blit(enemy, (30, 260))

            # draw menu (and buttons)
            pygame.draw.rect(self.win, BLACK, [0, 0, WIN_WIDTH, BTN_HEIGHT * 1 + 10])
            self.win.blit(enemy, (30, 260))

            # display hp
            for i in range(2):
                for j in range(5):

                    if (i * 5 + j) + 1 > self.hp:
                        self.win.blit(img_hp, ((j * HP_WIDTH + 430), (10 + i * HP_HEIGHT)))
                    else:
                        self.win.blit(img_hp_gray, [(j * HP_WIDTH + 430), (10 + i * HP_HEIGHT)])

            # display button
            self.win.blit(img_pause, (WIN_WIDTH - BTN_WIDTH * 1 - 10, 10))
            self.win.blit(img_continue, (WIN_WIDTH - BTN_WIDTH * 2 - 10, 10))
            self.win.blit(img_sound, (WIN_WIDTH - BTN_WIDTH * 3 - 10, 10))
            self.win.blit(img_mute, (WIN_WIDTH - BTN_WIDTH * 4 - 10, 10))

            # draw time
            self.curr_time = time.time() - self.init_time
            curr_sec = math.floor(self.curr_time)
            curr_min = math.floor(curr_sec / 60)

            text_time = self.font1.render(str(curr_min) + " : " + str(curr_sec), False, WHITE, BLACK)
            self.win.blit(text_time, (10, WIN_HEIGHT - 30))

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
