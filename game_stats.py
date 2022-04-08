class GameStats():

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.game_active = True
        self.high_score = 0
        self.reset_stats()

        #Inicia o jogo em um estado inativo
        #self.game_active = False

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    