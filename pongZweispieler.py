import random

import arcade
from arcade import Window, Section, View, SpriteList, SpriteSolidColor, SpriteCircle, draw_text, draw_line
from arcade.color import BLACK, BLUE, RED, BEAU_BLUE, GRAY, WHITE
from arcade.key import A, D, LEFT, RIGHT

import pongZweispieler

PLAYER_SECTION_WIDTH = 100
PLAYER_PADDLE_SPEED = 10
SPEED = 0

class Pong(View):

    def __init__(self):
        super().__init__()

        self.paddles: SpriteList = SpriteList()
        self.bot: SpriteSolidColor = SpriteSolidColor(100, 10, BLACK)
        self.right_player: SpriteSolidColor = SpriteSolidColor(100, 10, WHITE)
        self.left_player: SpriteSolidColor = SpriteSolidColor(100, 10, WHITE)

        self.background = arcade.load_texture("PongHintergrund.png")

        self.paddles.append(self.left_player)
        self.paddles.append(self.right_player)
        self.paddles.append(self.bot)

        self.ball: SpriteCircle = SpriteCircle(10, RED)

    def setup(self):
        self.ball.position = self.window.width / 2, self.window.height / 2
        # ball speed
        self.ball.change_x = random.choice([-2, -3, -4, -5, 2, 3, 4, 5])
        self.ball.change_y = random.choice([-SPEED, SPEED])

        # setup player and bot paddles
        self.right_player.position = self.window.width / 2 + 100, self.window.height - 880
        self.left_player.position = self.window.width / 2 - 100, self.window.height - 880
        self.bot.position = self.window.width / 2, self.window.height - 10

        self.counter = 0

    def on_update(self, delta_time: float):
        self.ball.update()
        self.bot.update()
        self.right_player.update()
        self.left_player.update()

        if self.ball.left <= 0:
            self.ball.change_x *= -1
        elif self.ball.right >= self.window.width:
            self.ball.change_x *= -1

        # moving the bot
        if self.bot.position[0] != self.ball.position[0]:
            position_x = self.ball.position[0]
            position_y = self.bot.position[1]
            self.bot.set_position(position_x, position_y)

        # limit bot movement
        if self.bot.right > self.window.width:
            self.bot.right = self.window.width

        if self.bot.left < 0:
            self.bot.left = 0

        # ball collide with paddle
        collided_paddle = self.ball.collides_with_list(self.paddles)
        if collided_paddle:
            if collided_paddle[0] is self.left_player or collided_paddle[0] is self.right_player:
                self.ball.bottom = self.left_player.top
                self.ball.bottom = self.right_player.top
                if pongZweispieler.SPEED < 32:
                    pongZweispieler.SPEED += 2
                    self.ball.change_y = -pongZweispieler.SPEED
                    self.ball.change_x = random.choice([-2, -3, -4, -5, 2, 3, 4, 5])
                    print("Speed:",pongZweispieler.SPEED)
                    x = print("Richtung:", self.ball.change_x)
                self.counter += 1
            else:
                self.ball.top = self.bot.bottom

            # bounce the ball from the paddle
            self.ball.change_y *= -1

        # limit movement right_player
        if self.right_player.right > self.window.width:
            self.right_player.right = self.window.width

        if self.right_player.left < self.window.width / 2:
            self.right_player.left = self.window.width / 2

        # limit movement left_player
        if self.left_player.left < 0:
            self.left_player.left = 0

        if self.left_player.right > self.window.width / 2:
            self.left_player.right = self.window.width / 2

        # check if the ball has exited the screen in either side and
        # end the game
        self.player = self.left_player, self.right_player
        if self.ball.bottom <= 0:
            self.end_game()
        elif self.ball.top >= self.window.height:
            self.end_game()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.right_player.change_x = PLAYER_PADDLE_SPEED
        if symbol == arcade.key.LEFT:
            self.right_player.change_x = -PLAYER_PADDLE_SPEED
        if symbol == arcade.key.D:
            self.left_player.change_x = PLAYER_PADDLE_SPEED
        if symbol == arcade.key.A:
            self.left_player.change_x = -PLAYER_PADDLE_SPEED

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.right_player.stop()
        self.left_player.stop()

    def end_game(self):
        print("Du hast:", self.counter, "erreicht.")
        f = open("scorePong2" , "a")
        f.write(str(self.counter) + "\n")
        f.close()

        self.window.close()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1440, 900, self.background)

        draw_text(f'Score: {self.counter}', self.window.width - 470 ,
                  self.window.height / 2, WHITE, font_size=30)

        self.half_window_x = self.window.width / 2
        draw_line(self.half_window_x, 0, self.half_window_x, self.window.height, GRAY, 2)

        self.ball.draw()
        self.bot.draw()
        self.right_player.draw()
        self.left_player.draw()

def main():
    window = Window(title='Arcane Arcade', fullscreen=True)
    game = Pong()
    game.setup()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()

