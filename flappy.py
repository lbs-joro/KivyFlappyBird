from KivyGame import *
from kivy.app import App

class Ball(GameObject):
    def on_key_down(self, key):
        if key == "w":
            self.velX = 0
            self.velY = 50
        if key == 's':
            self.velX = 0
            self.velY = -50
        if key == 'd':
            self.velX = 50
            self.velY = 0
        if key == 'a':
            self.velX = -50
            self.velY = 0

class MyGame(App):
    def build(self):
        screen = GameScreen()

        ball = Ball()
        ball.create((400,500), (50,50), "ball.png")

        screen.add_widget(ball)

        player = Ball()
        player.create((50,300), (75,75), "flyman.png")

        screen.add_widget(player)
        return screen

MyGame().run()
