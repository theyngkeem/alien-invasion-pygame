import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.game_active = True
        self.score = 0
        self.aliens_killed = 0
        self._create_fleet()

    def run_game(self):
        """main game loop"""
        while True:
            self._check_event()
            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
                self._check_alien_bottom()
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
        elif event.key == pygame.K_b:
            self._use_bomb()
        elif event.key == pygame.K_1:
            self._buy_feature('shield')
        elif event.key == pygame.K_2:
            self._buy_feature('plasma')
        elif event.key == pygame.K_3:
            self._buy_feature('bomb')

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
        self.aliens.draw(self.screen)

        # draw score
        self._draw_score()

        # draw available features
        if self.score >= self.setting.points_for_feature:
            self._draw_features()

        # show recent screen visible
        pygame.display.flip()

    def _draw_score(self):
        """display the score"""
        score_surf = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        score_rect = score_surf.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_surf, score_rect)

    def _draw_features(self):
        """display available features for purchase"""
        feature_text = "Features: 1=Shield  2=Plasma  3=Bomb"
        feature_surf = self.font.render(feature_text, True, (0, 0, 255))
        feature_rect = feature_surf.get_rect()
        feature_rect.topleft = (10, 50)
        self.screen.blit(feature_surf, feature_rect)

        # show bomb count if any
        if self.ship.bomb_count > 0:
            bomb_text = f"Bombs: {self.ship.bomb_count}"
            bomb_surf = self.font.render(bomb_text, True, (255, 0, 0))
            bomb_rect = bomb_surf.get_rect()
            bomb_rect.topleft = (10, 90)
            self.screen.blit(bomb_surf, bomb_rect)

    def _fire_bullet(self):
        """creat new bullet and add it to the group"""
        if len(self.bullets) < self.setting.bullet_allowed:
            plasma = self.ship.plasma_bullets
            new_bullet = Bullet(self, plasma=plasma)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """update bullet and delet who passed the screen"""
        self.bullets.update()

        # delete the bullets who disaapear
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # check for collisions
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """check for collisions between bullets and aliens"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, False)

        for bullet, aliens in collisions.items():
            # plasma bullets destroy on collision
            if bullet.plasma:
                self.bullets.remove(bullet)

            for alien in aliens:
                self.aliens.remove(alien)
                self.score += 100
                self.aliens_killed += 1

                # increase difficulty every 3 aliens
                if self.aliens_killed % 5 == 0:
                    self.setting.difficulty_scale += 0.1

                # regular bullets stop after hit
                if not bullet.plasma:
                    self.bullets.remove(bullet)
                    break

    def _update_aliens(self):
        """update alien positions and check edges"""
        self.aliens.update()

        # check if any alien hit edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.change_direction()

    def _check_alien_bottom(self):
        """check if aliens reached bottom or hit ship"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

        # check ship-alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """handle ship being hit"""
        if self.ship.shield_active:
            self.ship.deactivate_shield()
        else:
            self.game_active = False
            game_over_surf = self.font.render(
                "GAME OVER! Press Q to quit", True, (255, 0, 0))
            game_over_rect = game_over_surf.get_rect()
            game_over_rect.center = self.screen.get_rect().center
            self.screen.blit(game_over_surf, game_over_rect)
            pygame.display.flip()

    def _use_bomb(self):
        """use bomb to destroy all aliens"""
        if self.ship.bomb_count > 0:
            for alien in self.aliens.sprites():
                self.aliens.remove(alien)
                self.score += 50
            self.ship.bomb_count -= 1
            self._create_fleet()

    def _buy_feature(self, feature_type):
        """buy a feature with points"""
        if self.score >= self.setting.feature_cost:
            self.score -= self.setting.feature_cost

            if feature_type == 'shield':
                self.ship.activate_shield()
            elif feature_type == 'plasma':
                self.ship.activate_plasma()
            elif feature_type == 'bomb':
                self.ship.add_bomb()

    def _create_fleet(self):
        """create aliens in formation"""
        # create a temporary alien to get dimensions
        temp_alien = Alien(self)
        alien_width = temp_alien.rect.width
        alien_height = temp_alien.rect.height
        available_space_x = self.setting.screen_w - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine number of rows
        ship_height = self.ship.rect.height
        available_space_y = (
            self.setting.screen_h - 3 * alien_height - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # clear existing aliens first
        self.aliens.empty()

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """create single alien and place it in grid"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.rect.x = alien_width + 2 * alien_width * alien_number
        alien.x = float(alien.rect.x)
        alien.rect.y = alien_height + 2 * alien_height * row_number
        alien.y = float(alien.rect.y)
        self.aliens.add(alien)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
