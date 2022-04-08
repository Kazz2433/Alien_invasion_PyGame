class Settings():

    def __init__(self):

        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (248, 248, 248)

        # Configuração dos projeteis
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        # Configurações dos alienígenas
        self.fleet_drop_speed = 100
        
        #Vida
        self.ship_limit = 2

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # fleet_direction igual a 1 representa a direita; -1 represent
        #  esquerda
        self.fleet_direction = 1
        #Pontuação
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.speedup_scale