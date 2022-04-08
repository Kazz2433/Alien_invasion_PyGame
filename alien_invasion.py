import pygame
import sys
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen, "Play")

    # Cria instância para armazenar estatísticas do jogo e cria painel
    # de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    ship = Ship(ai_settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # Cria um alienígena
    aliens = Group()
    stars = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update() 
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats,sb, ship, aliens,
                             bullets)
            gf.update_screen(ai_settings, screen,stats,sb, ship, aliens, 
                            bullets,play_button)

run_game()
