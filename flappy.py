from KivyGame import *
from kivy.app import App

class Player(GameObject):
    def update(self, dt):
        self.velY -= 10

    def on_key_down(self, key):
        if key == "spacebar":
            self.velY = 300

class Obstacle(GameObject):
    def update(self, dt):
        self.velX = -80

        if self.pos_x() < -100:
            self.set_x(800)

class MyGame(App):
    def build(self):
        screen = GameScreen()

        player = Player()
        player.create((50, 300), (50,50), "flyman.png")

        screen.add_widget(player)

        for i in range(4):
            obstacleDown = Obstacle()
            obstacleDown.create((200 + i * 200, 0), (100,200), "cactus.png")
            obstacleUp = Obstacle()
            obstacleUp.create((200 + i * 200, 400), (100,200), "cactus_up.png")

            screen.add_widget(obstacleDown)
            screen.add_widget(obstacleUp)

        return screen

MyGame().run()
