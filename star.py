import pygame
from pygame import sprite
from pygame.sprite import Sprite
""""
class Star(Sprite):

    def __init__(self,ai_settings, screen):
        super(Star,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image,self.rect)
"""