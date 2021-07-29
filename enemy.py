import pygame
import math
import settings
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

HPBAR_WIDTH = 50
HPBAR_HEIGHT = 5
HPBAR_X_OFFSET = -10
HPBAR_Y_OFFSET = -30
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        # path index
        self.path_pos = 0
        # how many frames away from path point
        self.move_count = 0
        # distance between two points
        self.stride = 1
        self.x, self.y = self.path[0]

        self.next_x = 0
        self.next_y = 0

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """

        pygame.draw.rect(win, GREEN,
                         [self.x + HPBAR_X_OFFSET, self.y + HPBAR_Y_OFFSET, HPBAR_WIDTH * self.health / self.max_health,
                          HPBAR_HEIGHT])

        pygame.draw.rect(win, RED,
                         [self.x + HPBAR_X_OFFSET + HPBAR_WIDTH * self.health / self.max_health,
                          self.y + HPBAR_Y_OFFSET, HPBAR_WIDTH * (1 - self.health / self.max_health), HPBAR_HEIGHT])

        pass

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """

        # on a path point

        curr_x, curr_y = self.path[self.path_pos]
        # next path point
        next_x, next_y = self.path[self.path_pos + 1]

        # stride is the distance between path points
        distance = int(math.sqrt((curr_x - next_x) ** 2 + (curr_y - next_y) ** 2))
        # move a frame
        max_count = int(distance / self.stride)

        # between path points

        if self.move_count < max_count:

            self.x += (next_x - curr_x) / distance * self.stride

            self.y += (next_y - curr_y) / distance * self.stride

            self.move_count += 1
        else:
            self.move_count = 0
            self.path_pos += 1

        pass

class EnemyGroup:

    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120  # (unit: frame)
        self.reserved_members = []
        self.expedition = [enemy()]  # don't change this line until you do the EX.3
        self.timer = 1

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        timer += 1

        if(self.gen_count < 3) and (self.timer >= 120):
            self.expedition.append(self.reserved_members.pop())
            self.gen_count += 1
            self.timer = 0
        else:
            self.expedition.append(enemy())

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        self.reserved_members.append(enemy())


    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.gen_count -= 1
        self.expedition.remove(enemy)

