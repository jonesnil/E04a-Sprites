#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)
        self.character_list = arcade.SpriteList()

    def setup(self):
        for i in range(20):
            x = random.randint(0,800)
            y = random.randint(0,600)
            self.zombie_sprite = arcade.Sprite("assets/zombie.png", 1.5)
            self.zombie_sprite.center_x = x
            self.zombie_sprite.center_y = y
            self.character_list.append(self.zombie_sprite)  
        self.hero_sprite = arcade.Sprite("assets/head.png", 1.5)
        self.hero_sprite.center_x = 400
        self.hero_sprite.center_y = 300
        self.character_list.append(self.hero_sprite) 


    def on_draw(self):
        arcade.start_render()
        self.character_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.hero_sprite.center_x = x
        self.hero_sprite.center_y = y
        for zombie in self.character_list:
            if(zombie.center_x >= 50):
                if(x - zombie.center_x <= 50 and (x - zombie.center_x) > 0 and abs(y - zombie.center_y) <= 100 ):
                    zombie.center_x -= 5
            if(zombie.center_x <= 750):
                if(zombie.center_x - x <= 50 and (zombie.center_x - x) > 0 and abs(zombie.center_y - y) <= 100 ):
                    zombie.center_x += 5
            if(zombie.center_y >= 45):
                if(y - zombie.center_y <= 50 and (y - zombie.center_y) > 0 and abs(x - zombie.center_x) <= 100 ):
                    zombie.center_y -= 5
            if(zombie.center_y <= 555):
                if(zombie.center_y - y <= 50 and (zombie.center_y - y) > 0 and abs(zombie.center_x - x) <= 100 ):
                    zombie.center_y += 5



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()