import arcade
import arcade.gui
from arcade import Window, SpriteSolidColor, Sprite
from arcade.color import PURPLE_PIZZAZZ, WHITE

max_length_input = 4

class Keyboard(arcade.View):
    def __init__(self):
        super().__init__()

        self.window.set_update_rate(0.02)
        self.maus = arcade.SpriteCircle(color=PURPLE_PIZZAZZ, radius=10)
        joysticks = arcade.get_joysticks()

        if joysticks:
            # Grab the first one in  the list
            self.joystick = joysticks[0]
            self.joystick2 = joysticks[1]
            self.joystick.open()
            self.joystick2.open()
            # Push this object as a handler for joystick events.
            # Required for the on_joy* events to be called.
            self.joystick.push_handlers(self)
            self.joystick2.push_handlers(self)

        main.lastView = "GameOver"
        width_button = 70
        height_button = 50
        self.press = False

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.ui_text_label = arcade.gui.UILabel(text='', width=200, height=30, align='center', font_size=20)

        # First Line
        self.firstLineList = arcade.SpriteList()

        self.q_button = Sprite("keyboard_keys/q_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.q_button)
        self.q_button.set_position(70, 400)

        self.w_button = Sprite("keyboard_keys/w_button.png",image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.w_button)
        self.w_button.set_position(150, 400)

        self.e_button = Sprite("keyboard_keys/e_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.e_button)
        self.e_button.set_position(230, 400)

        self.r_button = Sprite("keyboard_keys/r_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.r_button)
        self.r_button.set_position(310, 400)

        self.t_button = Sprite("keyboard_keys/t_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.t_button)
        self.t_button.set_position(390, 400)

        self.z_button = Sprite("keyboard_keys/z_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.z_button)
        self.z_button.set_position(470, 400)

        self.u_button = Sprite("keyboard_keys/u_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.u_button)
        self.u_button.set_position(550, 400)

        self.i_button = Sprite("keyboard_keys/i_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.i_button)
        self.i_button.set_position(630, 400)

        self.o_button = Sprite("keyboard_keys/o_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.o_button)
        self.o_button.set_position(710, 400)

        self.p_button = Sprite("keyboard_keys/p_button.png", image_width=width_button, image_height=height_button)
        self.firstLineList.append(self.p_button)
        self.p_button.set_position(790, 400)

        # Second Line
        self.secondLineList = arcade.SpriteList()

        self.a_button = Sprite("keyboard_keys/a_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.a_button)
        self.a_button.set_position(90, 340)

        self.s_button = Sprite("keyboard_keys/s_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.s_button)
        self.s_button.set_position(170, 340)

        self.d_button = Sprite("keyboard_keys/d_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.d_button)
        self.d_button.set_position(250, 340)

        self.f_button = Sprite("keyboard_keys/f_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.f_button)
        self.f_button.set_position(330, 340)

        self.g_button = Sprite("keyboard_keys/g_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.g_button)
        self.g_button.set_position(410, 340)

        self.h_button = Sprite("keyboard_keys/h_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.h_button)
        self.h_button.set_position(490, 340)

        self.j_button = Sprite("keyboard_keys/j_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.j_button)
        self.j_button.set_position(570, 340)

        self.k_button = Sprite("keyboard_keys/k_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.k_button)
        self.k_button.set_position(670, 340)

        self.l_button = Sprite("keyboard_keys/l_button.png", image_width=width_button, image_height=height_button)
        self.secondLineList.append(self.l_button)
        self.l_button.set_position(750, 340)

        # Third Line
        self.thirdLineList = arcade.SpriteList()

        self.y_button = Sprite("keyboard_keys/y_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.y_button)
        self.y_button.set_position(230, 280)

        self.x_button = Sprite("keyboard_keys/x_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.x_button)
        self.x_button.set_position(310, 280)

        self.c_button = Sprite("keyboard_keys/c_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.c_button)
        self.c_button.set_position(390, 280)

        self.v_button = Sprite("keyboard_keys/v_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.v_button)
        self.v_button.set_position(470, 280)

        self.b_button = Sprite("keyboard_keys/b_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.b_button)
        self.b_button.set_position(550, 280)

        self.n_button = Sprite("keyboard_keys/n_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.n_button)
        self.n_button.set_position(630, 280)

        self.m_button = Sprite("keyboard_keys/m_button.png", image_width=width_button, image_height=height_button)
        self.thirdLineList.append(self.m_button)
        self.m_button.set_position(710, 280)

        # Keyboard Layout
        self.keyboardLayout = arcade.gui.UIBoxLayout()
        self.keyboardLayout.add(self.ui_text_label)

        self.main_button = Sprite("keyboard_keys/main_button.png", image_width=200, image_height=50)
        self.main_button.set_position(800, 600)

        self.replay_button = Sprite("keyboard_keys/newgame_button.png", image_width=200, image_height=50)
        self.replay_button.set_position(800, 550)

        self.save_button = Sprite("keyboard_keys/save_button.png", image_width=200, image_height=50)
        self.save_button.set_position(800, 500)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.keyboardLayout)
        )

    def on_joybutton_press(self, _joystick, button):
        if button == 2:
            self.press = True

    def on_update(self, delta_time: float):
        self.center_x = 0
        self.center_y = 0

        if self.joystick:
            # x-axis
            self.change_x = self.joystick.x
            # y-axis
            self.change_y = -self.joystick.y

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x == 1.0:
            print(self.center_x)

        if self.center_x == 1.0:
            self.on_key_press(self, 1)
        if self.center_x == -1.0:
            self.on_key_press(self, 1)
        if self.center_y == 1.0:
            self.on_key_press(self, 1)
        if self.center_y == -1.0:
            self.on_key_press(self, 1)
        if self.center_y != 1.0 and self.center_y != -1.0 and self.center_x != 1.0 and self.center_x != -1.0:
            self.on_key_release(self, 1)
        self.on_keyboard_key()
        self.maus.update()

    def on_keyboard_key(self):
        if self.maus.collides_with_sprite(self.q_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "Q"
                self.update_text()

        if self.maus.collides_with_sprite(self.w_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "W"
                self.update_text()

        if self.maus.collides_with_sprite(self.e_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "E"
                self.update_text()

        if self.maus.collides_with_sprite(self.r_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "R"
                self.update_text()

        if self.maus.collides_with_sprite(self.r_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "R"
                self.update_text()

        if self.maus.collides_with_sprite(self.t_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "T"
                self.update_text()

        if self.maus.collides_with_sprite(self.z_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "Z"
                self.update_text()

        if self.maus.collides_with_sprite(self.u_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "U"
                self.update_text()

        if self.maus.collides_with_sprite(self.i_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "I"
                self.update_text()

        if self.maus.collides_with_sprite(self.o_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "O"
                self.update_text()

        if self.maus.collides_with_sprite(self.p_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "P"
                self.update_text()

        if self.maus.collides_with_sprite(self.a_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "A"
                self.update_text()

        if self.maus.collides_with_sprite(self.s_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "S"
                self.update_text()

        if self.maus.collides_with_sprite(self.d_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "D"
                self.update_text()

        if self.maus.collides_with_sprite(self.f_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "F"
                self.update_text()

        if self.maus.collides_with_sprite(self.g_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "G"
                self.update_text()

        if self.maus.collides_with_sprite(self.h_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "H"
                self.update_text()

        if self.maus.collides_with_sprite(self.j_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "J"
                self.update_text()

        if self.maus.collides_with_sprite(self.k_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "K"
                self.update_text()

        if self.maus.collides_with_sprite(self.l_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "L"
                self.update_text()

        if self.maus.collides_with_sprite(self.y_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "Y"
                self.update_text()

        if self.maus.collides_with_sprite(self.x_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "X"
                self.update_text()

        if self.maus.collides_with_sprite(self.c_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "C"
                self.update_text()

        if self.maus.collides_with_sprite(self.v_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "V"
                self.update_text()

        if self.maus.collides_with_sprite(self.b_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "B"
                self.update_text()

        if self.maus.collides_with_sprite(self.n_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "N"
                self.update_text()

        if self.maus.collides_with_sprite(self.m_button) and self.press == True:
            if len(self.ui_text_label.text) < max_length_input:
                self.pressed_key = "M"
                self.update_text()

        if self.maus.collides_with_sprite(self.save_button) and self.press == True:
            self.save_button_pressed()

        if self.maus.collides_with_sprite(self.replay_button) and self.press == True:
            self.replay_button_pressed()

        if self.maus.collides_with_sprite(self.main_button) and self.press == True:
            self.main_button_pressed()


    def on_key_press(self, symbol: int, modifiers: int):

        if self.center_y == -1.0:
            self.maus.change_y = 5
        if self.center_y == 1.0:
            self.maus.change_y = -5
        if self.center_x == -1.0:
            self.maus.change_x = 5
        if self.center_x == 1.0:
            self.maus.change_x = -5

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.maus.stop()

    def update_text(self):
        label_text = self.ui_text_label.text
        self.ui_text_label.text = label_text + self.pressed_key
        print("Name: ", self.ui_text_label.text)
        self.press = False

    def on_show_view(self):
        arcade.set_background_color(arcade.color.RED)
        self.background = arcade.load_texture("Pictures/GameOverView.jpg")

    def replay_button_pressed(self, event):
        if main.lastGame == 2:
            game = SnakeViewZweispieler()
        if main.lastGame == 3:
            game = PongView()
            game.setup()
        if main.lastGame == 1:
            game = SnakeViewEinspieler()

        self.window.show_view(game)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1536, 864, self.background)
        self.manager.draw()
        self.firstLineList.draw()
        self.secondLineList.draw()
        self.thirdLineList.draw()
        self.main_button.draw()
        self.save_button.draw()
        self.replay_button.draw()
        self.maus.draw()

    def main_button_pressed(self, event):
        game = MenuView()
        self.window.show_view(game)

    def save_button_pressed(self, event):
        print("HALLO")
        if main.lastGame == 1:
            f = open("Scores/ScoreSnakeEinspieler.txt", "a")
        if main.lastGame == 2:
            f = open("Scores/ScoreSnakeZweispieler.txt", "a")
        if main.lastGame == 3:
            f = open("Scores/ScorePongEinspieler.txt", "a")
        if main.lastGame == 4:
            f = open("Scores/ScorePongZweispieler.txt", "a")

        f.write(str(self.ui_text_label.text) + " " + str(main.SCORE) + "\n")
        f.close()

def main():
        window = Window(title='Arcane Arcade', fullscreen=True)
        game = Keyboard()
        window.show_view(game)
        window.run()

if __name__ == '__main__':
    main()
