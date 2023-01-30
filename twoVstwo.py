import random

from arcade import Window, Section, View, SpriteList, SpriteSolidColor, \
    SpriteCircle, draw_text, draw_line
from arcade.color import BLACK, BLUE, RED, BEAU_BLUE, GRAY, WHITE
from arcade.key import W, S, UP, DOWN

import twoVstwo

PLAYER_SECTION_WIDTH = 100
PLAYER_PADDLE_SPEED = 10
SPEED = 5


class Player1(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        self.paddle: SpriteSolidColor = SpriteSolidColor(10, 100, BLACK)

        self.score: int = 0

    def setup(self):
        self.paddle.position = self.left + 20, self.height / 2

    def on_update(self, delta_time: float):
        self.paddle.update()

    def on_draw(self):
        draw_text(f'Score: {self.score}', self.left + 20 ,
                  self.bottom + 550, BLUE)

        # draw the paddle
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # set the paddle direction and movement speed
        if symbol == self.key_up:
            self.paddle.change_y = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_y = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        # stop moving the paddle
        self.paddle.stop()

class Player2(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 key_up: int, key_down: int, **kwargs):
        super().__init__(left, bottom, width, height,
                         accept_keyboard_events={key_up, key_down}, **kwargs)

        self.key_up: int = key_up
        self.key_down: int = key_down

        # the player paddle
        self.paddle: SpriteSolidColor = SpriteSolidColor(10, 100, WHITE)

        # player score
        self.score: int = 0

    def setup(self):
        # reset the player paddle position to the middle of the screen
        self.paddle.position = self.left + 80, self.height / 2

    def on_update(self, delta_time: float):
        # update the paddle position
        self.paddle.update()

    def on_draw(self):
        draw_text(f'Score: {self.score}', self.left - 20 ,
                  self.bottom + 550, BLUE)

        # draw the paddle
        self.paddle.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # set the paddle direction and movement speed
        if symbol == self.key_up:
            self.paddle.change_y = PLAYER_PADDLE_SPEED
        else:
            self.paddle.change_y = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        # stop moving the paddle
        self.paddle.stop()


class Pong(View):

    def __init__(self):
        super().__init__()

        # a sprite list that will hold each player paddle to
        # check for collisions
        self.paddles: SpriteList = SpriteList()

        # we store each Section
        self.left_player: Player1 = Player1(
            0, 0, PLAYER_SECTION_WIDTH, self.window.height, key_up=W,
            key_down=S, name='Left')

        self.right_player: Player2 = Player2(
            self.window.width - PLAYER_SECTION_WIDTH, 0, PLAYER_SECTION_WIDTH,
            self.window.height, key_up=UP, key_down=DOWN, name='Right')

        # add the sections to the SectionManager so Sections start to work
        self.add_section(self.left_player)
        self.add_section(self.right_player)

        # add each paddle to the sprite list
        self.paddles.append(self.left_player.paddle)
        self.paddles.append(self.right_player.paddle)

        # create the ball
        self.ball: SpriteCircle = SpriteCircle(10, RED)

    def setup(self):
        # set up a new game

        # set ball position in the middle
        self.ball.position = self.window.width / 2, self.window.height / 2

        # randomize ball direction and speed
        self.ball.change_x = random.choice([SPEED, -SPEED])
        self.ball.change_y = random.choice([-2, -3, -4, -5, -6, -7, -8, 2, 3, 4, 5, 6, 7, 8 ])

        # setup player paddles
        self.left_player.setup()
        self.right_player.setup()

    def on_update(self, delta_time: float):
        self.ball.update()  # update the ball

        # bounce the ball either at the top or at the bottom
        if self.ball.bottom <= 0:
            self.ball.change_y *= -1
        elif self.ball.top >= self.window.height:
            self.ball.change_y *= -1


        # check if the ball has collided with a paddle
        collided_paddle = self.ball.collides_with_list(self.paddles)
        if collided_paddle:
            # adjust ball coordinates to simplify the game
            if collided_paddle[0] is self.left_player.paddle:
                self.ball.left = self.left_player.paddle.right
                twoVstwo.SPEED += .5
                self.ball.change_x = -twoVstwo.SPEED
                print(twoVstwo.SPEED)
            else:
                self.ball.right = self.right_player.paddle.left
                twoVstwo.SPEED += .5
                self.ball.change_x = twoVstwo.SPEED
                print(twoVstwo.SPEED)

            # bounce the ball from the paddle
            self.ball.change_x *= -1

        # check if the ball has exited the screen in either side and
        # end the game
        if self.ball.right <= 0:
            self.end_game(self.right_player)
        elif self.ball.left >= self.window.width:
            self.end_game(self.left_player)

    def end_game(self, winner: Player1):
        """ Called when one player wins """
        winner.score += 1  # increment the winner score
        twoVstwo.SPEED = 4
        self.setup()
        if winner.score == 10:
              self.window.close()

    def on_draw(self):
        self.clear(BEAU_BLUE)  # clear the screen

        half_window_x = self.window.width / 2  # middle x
        draw_line(half_window_x, 0, half_window_x, self.window.height, GRAY, 2)

        self.ball.draw()  # draw the ball



def main():
    # create the window
    window = Window(title='Arcane Arcade', fullscreen=True)

    # create the custom View
    game = Pong()

    # set up the game (start a game)
    game.setup()

    # show the view
    window.show_view(game)

    # run arcade loop
    window.run()


if __name__ == '__main__':
    main()