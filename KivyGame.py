from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import Builder


Builder.load_string('''
<GameObject>
    size: 50, 50
    pos: 50,100
    source: ''
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: self.source


''')


class GameObject(Widget):

    velX = 0
    velY = 0

    def set_x(self, value):
        self.pos[0] = value

    def set_y(self, value):
        self.pos[1] = value

    def set_vel_x(self, value):
        self.velX = value
        
    def set_vel_y(self, value):
        self.velY = value

    def pos_x(self):
        return self.pos[0]
    
    def pos_y(self):
        return self.pos[1]
    

    def create(self, pos, size, source):
        self.pos = pos
        self.size = size
        self.source = source
        

        self.init()

    def init(self):
        pass

    def physics_update(self,dt):
        self.pos[0] += self.velX * dt
        self.pos[1] += self.velY * dt

    def update(self, dt):
        pass

    def on_key_down(self, key):
        pass

    def on_collision(self, other):
        pass
        

class GameScreen(Widget):
    width = 800
    height = 600

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (800, 600)

        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        for c in self.children:
            c.on_key_down(keycode[1])

    def window_size(self, width, height):
        self.width = width
        self.height = height
        Window.size = (width, height)

    def update(self, dt):
        for c in self.children:
            c.update(dt)
            c.physics_update(dt)
            for other in self.children:
                if other != c and self.collision(c,other):
                    c.on_collision(other)
            


    def collision(self, r1, r2):

        if r1.pos_x() + r1.width >= r2.pos_x() and r1.pos_x() <= r2.pos_x() + r2.width and r1.pos_y() + r1.height >= r2.pos_y() and r1.pos_y()<=r2.pos_y()+r2.height:
            return True
        return False