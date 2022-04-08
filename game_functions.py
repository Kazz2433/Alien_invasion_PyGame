import sys
from time import sleep
import pygame
from pygame.constants import KEYDOWN
from pygame.event import get
from bullet import Bullet
from alien import Alien
# from star import Star



def check_keydown_events(event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        fire_bullet(ai_settings,screen, ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen,stats,sb, ship,aliens, bullets,
play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #stars.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Verifica se algum projétil atingiu os alienígena
    # Em caso afirmativo, livra-se do projétil e do alienígena
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,
bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens) 
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas que cabem na tela."""
    available_space_y = (ai_settings.screen_height - 
                            (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    # Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    aliens.add(alien)
""""
def create_star(ai_settings, screen, stars, star_number,row_number):
    # Cria um alienígena e o posiciona na linha
    star = Star(ai_settings,screen)
    star_width = star.rect.width
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    star.rect.x = star_width + 3 * star_width * star_number
    stars.add(star)
"""

def create_fleet(ai_settings, screen,ship, aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # Cria frota de alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
""" 
for star_number in range(10):
create_star(ai_settings,screen,stars,star_number,row_number)
"""

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,
bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a 
        #espaçonave é atingida
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """"
    Verifica se a frota está em uma das bordas
    e então atualiza as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    if stats.ship_left > 0:
        # Decrementa ship left
        stats.ship_left -= 1

        # Atualiza o painel de pontuações
        sb.prep_ships()

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()