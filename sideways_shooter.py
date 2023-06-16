import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():

    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Set the background color
    # bg_color = (255, 255, 255)

    # Make the ship.
    ship = Ship(screen, settings)

    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)


if __name__ == "__main__":
    run_game()
