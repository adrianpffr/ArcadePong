import random

import arcade
from arcade import Window, Section, View, SpriteList, SpriteSolidColor, \
    SpriteCircle, draw_text, draw_line
from arcade.color import BLACK, BLUE, RED, BEAU_BLUE, GRAY, WHITE
from arcade.key import W, S, UP, DOWN

import pongEinspieler

PLAYER_SECTION_WIDTH = 100
PLAYER_PADDLE_SPEED = 10
SPEED = 5

class Pong(View):

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("PongHintergrund.png")

        self.paddles: SpriteList = SpriteList()
        self.bot: SpriteSolidColor = SpriteSolidColor(10, 100, BLACK)
        self.right_player: SpriteSolidColor = SpriteSolidColor(10, 100, WHITE)

        self.paddles.append(self.bot)
        self.paddles.append(self.right_player)

        self.ball: SpriteCircle = SpriteCircle(10, RED)

    def setup(self):
        self.ball.position = self.window.width / 2, self.window.height / 2
        self.bot.position = 0 + 20, self.window.height / 2
        self.right_player.position = self.window.width - 20, self.window.height / 2

        # ball speed/direction
        self.ball.change_x = random.choice([SPEED, -SPEED])
        self.ball.change_y = random.choice([-2, -3, -4, -5, -6, -7, -8, 2, 3, 4, 5, 6, 7, 8 ])


        self.counter = 0

    def on_update(self, delta_time: float):
        self.ball.update()
        self.bot.update()
        self.right_player.update()

        # bounce ball
        if self.ball.bottom <= 0:
            self.ball.change_y *= -1
        elif self.ball.top >= self.window.height:
            self.ball.change_y *= -1

        # moving the bot
        if self.bot.position[0] != self.ball.position[0]:
            position_y = self.ball.position[1]
            position_x = self.bot.position[0]
            self.bot.set_position(position_x, position_y)

        # limit bot movement
        if self.bot.top > self.window.height:
            self.bot.top = self.window.height

        if self.bot.bottom < 0:
            self.bot.bottom = 0

        # limit Player movement
        if self.right_player.top > self.window.height:
            self.right_player.top = self.window.height

        if self.right_player.bottom < 0:
            self.right_player.bottom = 0

        # collide with paddle
        collided_paddle = self.ball.collides_with_list(self.paddles)
        if collided_paddle:
            if collided_paddle[0] is self.bot:
                self.ball.left = self.bot.right
                pongEinspieler.SPEED += .5
                self.ball.change_x = -pongEinspieler.SPEED
                print(pongEinspieler.SPEED)
            else:
                self.ball.right = self.right_player.left
                pongEinspieler.SPEED += .5
                self.ball.change_x = pongEinspieler.SPEED
                self.counter += 1
                print(pongEinspieler.SPEED)

            # bounce ball from paddle
            self.ball.change_x *= -1

        if self.ball.right <= 0:
            self.end_game(self.right_player)
        elif self.ball.left >= self.window.width:
            self.end_game(self.bot)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.right_player.change_y = PLAYER_PADDLE_SPEED
        if symbol == arcade.key.DOWN:
            self.right_player.change_y = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.right_player.stop()

    def end_game(self):
        print("Du hast:", self.counter, "erreicht.")
        self.window.close()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1440, 900, self.background)

        draw_text(f'Score: {self.counter}', self.window.width - 470 ,
                  self.window.height / 2, BLUE, font_size=30)

        half_window_x = self.window.width / 2
        draw_line(half_window_x, 0, half_window_x, self.window.height, GRAY, 2)

        self.ball.draw()
        self.bot.draw()
        self.right_player.draw()

def main():
    window = Window(title='Arcane Arcade', fullscreen=True)
    game = Pong()
    game.setup()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()