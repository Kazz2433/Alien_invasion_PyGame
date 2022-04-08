import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # Cria um retângulo para o projétil em (0, 0) e, em seguida,
        # define a posição correta
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx 
        self.rect.top = ship.rect.top

        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move o projétil para cima na tela."""
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)