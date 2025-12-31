import pygame


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
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # start at midbottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        if self.r_movement and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.l_movement and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """draw the ship"""
        self.screen.blit(self.image, self.rect)
