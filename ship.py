import pygame
import os


class Ship:
    """manage the ship"""

    def __init__(self, ai_game):
        """init the ship and set pos"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting

        self.r_movement = False
        self.l_movement = False

        # load the ship image
        image_path = os.path.join(
            os.path.dirname(__file__), 'images', 'ship.bmp')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        # start at midbottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # ship features
        self.shield_active = False
        self.plasma_bullets = False
        self.bomb_count = 0

    def update(self):
        if self.r_movement and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.l_movement and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """draw the ship"""
        self.screen.blit(self.image, self.rect)

        # draw shield indicator if active
        if self.shield_active:
            pygame.draw.rect(self.screen, (0, 255, 255), self.rect, 3)

    def activate_shield(self):
        """activate shield for one hit"""
        self.shield_active = True

    def deactivate_shield(self):
        """deactivate shield"""
        self.shield_active = False

    def activate_plasma(self):
        """activate plasma bullets"""
        self.plasma_bullets = True

    def add_bomb(self):
        """add bomb to inventory"""
        self.bomb_count += 1
