import sys
import pygame


def check_events(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """Respond to keydown events."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to left.
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship to top:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


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


def update_screen(settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the most drawn screen visible.
    pygame.display.flip()
