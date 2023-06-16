import sys
import pygame
from bullet import Bullet


def check_events(ss_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ss_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ss_settings, screen, ship, bullets):
    """Respond to keydown events."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to left.
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship to top.
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the ship to bottom.
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ss_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to keyup events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ss_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ss_settings.bg_color)
    ship.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.blitme()

    # Make the most drawn screen visible.
    pygame.display.flip()
