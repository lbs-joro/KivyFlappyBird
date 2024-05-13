from KivyGame import *
from kivy.app import App
import random

class Player(GameObject):
    def update(self, dt):
        self.velY -= 10

        if self.pos_y() < 0:
            App.get_running_app().reset_game()

    def on_key_down(self, key):
        if key == "spacebar":
            self.velY = 300

    def on_collision(self, other):
        App.get_running_app().reset_game()

class Obstacle(GameObject):
    def update(self, dt):
        self.velX = -80

        if self.pos_x() < -100:
            randomheight = random.randint(100,500)
            self.size = (100, randomheight)

            if self.source == "cactus_up.png": 
                self.set_y(600-randomheight)
            
            self.set_x(800)

class MyGame(App):
    def build(self):
        self.screen = GameScreen()
        self.reset_game()
        return self.screen
    
    def reset_game(self):
        self.screen.clear_widgets()

        player = Player()
        player.create((50, 300), (50,50), "flyman.png")

        self.screen.add_widget(player)

        for i in range(4):
            obstacleDown = Obstacle()
            randomheightDown = random.randint(100,280)
            obstacleDown.create((200 + i * 200, 0), (100,randomheightDown), "cactus.png")
            
            obstacleUp = Obstacle()
            randomheightUp = random.randint(100,280)
            obstacleUp.create((200 + i * 200, 600-randomheightUp), (100,randomheightUp), "cactus_up.png")
            
            
            self.screen.add_widget(obstacleDown)
            self.screen.add_widget(obstacleUp)

MyGame().run()
