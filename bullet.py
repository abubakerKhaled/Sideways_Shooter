import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manage bullet fired from the ship."""

    def __init__(self, setting, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Load the bullet image and get its rect.
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()

        # Set the bullet's initial position at the ship's centerx and top attributes.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.speed_factor

        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the bullet at its current position."""
        self.screen.blit(self.image, self.rect)
