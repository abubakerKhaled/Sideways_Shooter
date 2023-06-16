import pygame


class Ship():

    def __init__(self, screen, ss_settings):

        self.screen = screen

        self.ss_settings = ss_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            'images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start a new ship on the left side of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.y)

        # Movements flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect value.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ss_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ss_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:  # changed up to top
            self.y -= self.ss_settings.ship_speed_factor  # changed sign
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ss_settings.ship_speed_factor  # changed sign

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
