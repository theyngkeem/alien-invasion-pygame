import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """manage the game assets"""

    def __init__(self):
        """manage game behavior"""
        pygame.init()

        self.setting = Setting()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_w, self.setting.screen_h))
        pygame.display.set_caption("AlienInvasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def run_game(self):
        """main game loop"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        """check pressin key"""
        if event.key == pygame.K_RIGHT:
            self.ship.r_movement = True
        elif event.key == pygame.K_LEFT:
            self.ship.l_movement = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.r_movement = False
        elif event.key == pygame.K_LEFT:
            self.ship.l_movement = False

    def _update_screen(self):
        """update the screen"""

        self.screen.fill(self.setting.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # show recent screen visible
        pygame.display.flip()

    def _fire_bullet(self):
        """creat new bullet and add it to the group"""
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """update bullet and delet who passed the screen"""
        self.bullets.update()

        # delete the bullets who disaapear
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
