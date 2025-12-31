import pygame
import os
from pygame.sprite import Sprite


class Alien(Sprite):
    """manage the aliens"""
    def __init__(self, ai_game):
        """assigne atts"""
        super().__init__()

        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        # load image
        image_path = os.path.join(
            os.path.dirname(__file__), 'images', 'alien.bmp')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # float for precise movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement direction (1 = right, -1 = left)
        self.direction = 1

    def update(self):
        """move the alien"""
        speed = self.setting.alien_speed * self.direction
        speed *= self.setting.difficulty_scale
        self.x += speed
        self.rect.x = self.x

    def check_edges(self):
        """return True if alien is at edge of screen"""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def change_direction(self):
        """change direction and drop down"""
        self.direction *= -1
        self.y += self.setting.fleet_drop_speed
        self.rect.y = self.y
