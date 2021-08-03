import pygame
import os

SELL_IMG = pygame.image.load(os.path.join("images", "sell.png"))
UPGRADE_IMG = pygame.image.load(os.path.join("images", "upgrade.png"))
UPGRADE_MENU_IMG = pygame.image.load(os.path.join("images", "upgrade_menu.png"))

MENU_IMG_WIDTH = 150
MENU_IMG_HEIGHT = 150

SELL_IMG_WIDTH = 60
SELL_IMG_HEIGHT = 60

UPGRADE_IMG_WIDTH = 100
UPGRADE_IMG_HEIGHT = 60

BTN_OFFSET = 70


class UpgradeMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.upgrade_menu_img = pygame.transform.scale(UPGRADE_MENU_IMG, (MENU_IMG_WIDTH, MENU_IMG_HEIGHT))
        self.sell_img = pygame.transform.scale(SELL_IMG, (SELL_IMG_WIDTH, SELL_IMG_HEIGHT))
        self.upgrade_img = pygame.transform.scale(UPGRADE_IMG, (UPGRADE_IMG_WIDTH, UPGRADE_IMG_HEIGHT))
        self.rect = self.upgrade_menu_img.get_rect()

        self.rect.centerx = self.x - MENU_IMG_WIDTH / 2
        self.rect.centery = self.y - MENU_IMG_HEIGHT / 2

        # print(self.rect)

        # print(self.rect)
        self.__buttons = [Button(self.upgrade_img, "upgrade", self.x, self.y - BTN_OFFSET),
                          Button(self.sell_img, "sell", self.x, self.y + BTN_OFFSET)]

    def draw(self, win):
        """
        self.__buttons = []  # (Q2) Add buttons here
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # pygame.draw.rect(win, (255, 0, 0), [250, 310, 100, 60])
        # draw menu
        win.blit(self.upgrade_menu_img, (self.rect.center))
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.sell_img, (self.x - SELL_IMG_WIDTH / 2, self.y - SELL_IMG_HEIGHT / 2 + MENU_IMG_WIDTH / 2))
        win.blit(self.upgrade_img,
                 (self.x - UPGRADE_IMG_WIDTH / 2, self.y - UPGRADE_IMG_HEIGHT / 2 - MENU_IMG_WIDTH / 2))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """

        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.rect.width = image.get_width()
        self.rect.height = image.get_height()
        # print(self.rect)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """

        if self.rect.collidepoint(x, y):
            # print('true')
            return True
        else:
            # print('false')
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
