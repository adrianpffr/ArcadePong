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


class Bot(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        self.paddle: SpriteSolidColor = SpriteSolidColor(10, 100, BLACK)

    def setup(self):
        self.paddle.position = self.left + 20, self.height / 2

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == self.key_up:
            self.paddle.change_y = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_y = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.paddle.stop()

class Player2(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        self.paddle: SpriteSolidColor = SpriteSolidColor(10, 100, WHITE)


    def setup(self):
        self.paddle.position = self.left + 80, self.height / 2

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == self.key_up:
            self.paddle.change_y = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_y = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.paddle.stop()


class Pong(View):

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("PongHintergrund.png")

        self.paddles: SpriteList = SpriteList()

        self.bot: Bot = Bot(
            0, 0, PLAYER_SECTION_WIDTH, self.window.height, key_up=W,
            key_down=S, name='Left')

        self.right_player: Player2 = Player2(
            self.window.width - PLAYER_SECTION_WIDTH, 0, PLAYER_SECTION_WIDTH,
            self.window.height, key_up=UP, key_down=DOWN, name='Right')

        self.add_section(self.bot)
        self.add_section(self.right_player)

        self.paddles.append(self.bot.paddle)
        self.paddles.append(self.right_player.paddle)

        self.ball: SpriteCircle = SpriteCircle(10, RED)

    def setup(self):
        self.ball.position = self.window.width / 2, self.window.height / 2

        # ball speed/direction
        self.ball.change_x = random.choice([SPEED, -SPEED])
        self.ball.change_y = random.choice([-2, -3, -4, -5, -6, -7, -8, 2, 3, 4, 5, 6, 7, 8 ])

        self.bot.setup()
        self.right_player.setup()

        self.counter = 0

    def on_update(self, delta_time: float):
        self.ball.update()

        # bounce ball
        if self.ball.bottom <= 0:
            self.ball.change_y *= -1
        elif self.ball.top >= self.window.height:
            self.ball.change_y *= -1

        # moving the bot
        if self.bot.paddle.position[0] != self.ball.position[0]:
            position_y = self.ball.position[1]
            position_x = self.bot.paddle.position[0]
            self.bot.paddle.set_position(position_x, position_y)

        # limit bot movement
        if self.bot.paddle.top > self.window.height:
            self.bot.paddle.top = self.window.height

        if self.bot.paddle.bottom < 0:
            self.bot.paddle.bottom = 0

        # limit Player movement
        if self.right_player.paddle.top > self.window.height:
            self.right_player.paddle.top = self.window.height

        if self.right_player.paddle.bottom < 0:
            self.right_player.paddle.bottom = 0

        # collide with paddle
        collided_paddle = self.ball.collides_with_list(self.paddles)
        if collided_paddle:
            if collided_paddle[0] is self.bot.paddle:
                self.ball.left = self.bot.paddle.right
                pongEinspieler.SPEED += .5
                self.ball.change_x = -pongEinspieler.SPEED
                print(pongEinspieler.SPEED)
            else:
                self.ball.right = self.right_player.paddle.left
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

def main():
    window = Window(title='Arcane Arcade', fullscreen=True)
    game = Pong()
    game.setup()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()