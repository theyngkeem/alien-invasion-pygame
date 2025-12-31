import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """manage the bullet"""
    def __init__(self, ai_game):
        """match the ship pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # set bullet to ship rect
        self.rect = pygame.Rect(0, 0, self.setting.bullet_w,
                                self.setting.bullet_h)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store it as float
        self.y = float(self.rect.y)

    def update(self):
        """update bullet pos"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet from scratch"""
        pygame.draw.rect(self.screen, self.color, self.rect)
