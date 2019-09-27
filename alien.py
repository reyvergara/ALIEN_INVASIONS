import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        # Initialize the alien and set its starting position.
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = settings

        # Load alien image and set its hitbox
        self.image = pygame.image.load('images/ufo_.png')
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the alien at its current location.
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # RETURN TRUE IF ALIENS ARE AT THE EDGE OF SCREEN
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def update(self):
        # MOVE ALIEN TO RIGHT
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
