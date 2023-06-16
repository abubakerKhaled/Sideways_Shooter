import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():

    pygame.init()

    ss_settings = Settings()

    screen = pygame.display.set_mode(
        (ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Set the background color
    # bg_color = (255, 255, 255)

    # Make the ship.
    ship = Ship(screen, ss_settings)

    # Make a group to store the bullets in.
    bullets = Group()

    while True:

        gf.check_events(ss_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ss_settings, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
