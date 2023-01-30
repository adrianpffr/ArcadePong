import random

from arcade import Window, Section, View, SpriteList, SpriteSolidColor, SpriteCircle, draw_text, draw_line
from arcade.color import BLACK, BLUE, RED, BEAU_BLUE, GRAY, WHITE
from arcade.key import A, D, LEFT, RIGHT

import pongZweispieler

PLAYER_SECTION_WIDTH = 100
PLAYER_PADDLE_SPEED = 10
SPEED = 4

class Bot(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         **kwargs)

        self.paddle: SpriteSolidColor = SpriteSolidColor(100, 10, GRAY)

    def setup(self):
        self.paddle.position = self.left + 400, self.top - 10

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        self.paddle.draw()

class Player1(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        self.paddle: SpriteSolidColor = SpriteSolidColor(100, 10, BLACK)

    def setup(self):
        self.paddle.position = self.left + 100, self.bottom + 10

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == self.key_up:
            self.paddle.change_x = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_x = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.paddle.stop()

class Player2(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        self.paddle: SpriteSolidColor = SpriteSolidColor(100, 10, WHITE)

    def setup(self):
        self.paddle.position = self.left + 10, self.bottom + 10

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == self.key_up:
            self.paddle.change_x = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_x = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.paddle.stop()


class Pong(View):

    def __init__(self):
        super().__init__()

        self.paddles: SpriteList = SpriteList()

        self.left_player: Player1 = Player1(
            0, 0, PLAYER_SECTION_WIDTH, self.window.height, key_up=D,
            key_down=A, name='Left')

        self.right_player: Player2 = Player2(
            self.window.width - PLAYER_SECTION_WIDTH, 0, PLAYER_SECTION_WIDTH,
            self.window.height, key_up=RIGHT, key_down=LEFT, name='right')

        self.bot: Bot = Bot(
            0, 0, PLAYER_SECTION_WIDTH,
            self.window.height, key_up=RIGHT, key_down=LEFT, name='bot')

        self.add_section(self.left_player)
        self.add_section(self.right_player)
        self.add_section(self.bot)

        self.paddles.append(self.left_player.paddle)
        self.paddles.append(self.right_player.paddle)
        self.paddles.append(self.bot.paddle)

        self.ball: SpriteCircle = SpriteCircle(10, RED)

    def setup(self):
        self.ball.position = self.window.width / 2, self.window.height / 2


        # ball speed
        self.ball.change_x = random.choice([-2, -3, -4, -5, -6, -7, 2, 3, 4, 5, 6, 7])
        self.ball.change_y = random.choice([SPEED, -SPEED])

        # setup player and bot paddles
        self.left_player.setup()
        self.right_player.setup()
        self.bot.setup()

        self.counter = 0


    def on_update(self, delta_time: float):
        self.ball.update()

        if self.ball.left <= 0:
            self.ball.change_x *= -1
        elif self.ball.right >= self.window.width:
            self.ball.change_x *= -1

        # moving the bot
        if self.bot.paddle.position[0] != self.ball.position[0]:
            position_x = self.ball.position[0]
            position_y = self.bot.paddle.position[1]
            self.bot.paddle.set_position(position_x, position_y)

        # limit bot movement
        if self.bot.paddle.right > self.window.width:
            self.bot.paddle.right = self.window.width

        if self.bot.paddle.left < 0:
            self.bot.paddle.left = 0

        # ball collide with paddle
        collided_paddle = self.ball.collides_with_list(self.paddles)
        if collided_paddle:
            if collided_paddle[0] is self.left_player.paddle or collided_paddle[0] is self.right_player.paddle:
                self.ball.bottom = self.left_player.paddle.top
                self.ball.bottom = self.right_player.paddle.top
                pongZweispieler.SPEED += .5
                self.ball.change_x = pongZweispieler.SPEED
                print(pongZweispieler.SPEED)
                self.counter += 1
                print(self.counter)
            else:
                self.ball.top = self.bot.paddle.bottom

            # bounce the ball from the paddle
            self.ball.change_y *= -1

        # limit movement right_player

        if self.right_player.paddle.right > self.window.width:
            self.right_player.paddle.right = self.window.width

        if self.right_player.paddle.left < self.window.width / 2:
            self.right_player.paddle.left = self.window.width / 2

        # limit movement left_player

        if self.left_player.paddle.left < 0:
            self.left_player.paddle.left = 0

        if self.left_player.paddle.right > self.window.width / 2:
            self.left_player.paddle.right = self.window.width / 2

        # check if the ball has exited the screen in either side and
        # end the game
        self.player = self.left_player, self.right_player
        if self.ball.bottom <= 0:
            self.end_game()
        elif self.ball.top >= self.window.height:
            self.end_game()

    def end_game(self):
        print("Du hast:", self.counter, "erreicht.")
        self.window.close()

    def on_draw(self):
        self.clear(BEAU_BLUE)

        draw_text(f'Score: {self.counter}', self.window.width - 470 ,
                  self.window.height / 2, BLUE, font_size=30)

        self.half_window_x = self.window.width / 2
        draw_line(self.half_window_x, 0, self.half_window_x, self.window.height, GRAY, 2)

        self.ball.draw()

def main():
    window = Window(title='Arcane Arcade', fullscreen=False)
    game = Pong()
    game.setup()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()

