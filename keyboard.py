import arcade
import arcade.gui
from arcade import Window

max_length_input = 4

class Keyboard(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        self.ui_text_label = arcade.gui.UILabel(text= '', width=200, height=30, align='center', font_size=20)

        # First Line
        self.firstLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        q_button = arcade.gui.UIFlatButton(text="Q", width=width_button, height= height_button)
        self.firstLineLayout.children.append(q_button)
        q_button.on_click = self.on_click_q

        w_button = arcade.gui.UIFlatButton(text="W", width=width_button, height= height_button)
        self.firstLineLayout.add(w_button)
        w_button.on_click = self.on_click_w

        e_button = arcade.gui.UIFlatButton(text="E", width=width_button, height= height_button)
        self.firstLineLayout.add(e_button)
        e_button.on_click = self.on_click_e

        r_button = arcade.gui.UIFlatButton(text="R", width=width_button, height= height_button)
        self.firstLineLayout.add(r_button)
        r_button.on_click = self.on_click_r

        t_button = arcade.gui.UIFlatButton(text="T", width=width_button, height= height_button)
        self.firstLineLayout.children.append(t_button)
        t_button.on_click = self.on_click_t

        z_button = arcade.gui.UIFlatButton(text="Z", width=width_button, height= height_button)
        self.firstLineLayout.add(z_button)
        z_button.on_click = self.on_click_z

        u_button = arcade.gui.UIFlatButton(text="U", width=width_button, height= height_button)
        self.firstLineLayout.add(u_button)
        u_button.on_click = self.on_click_u

        i_button = arcade.gui.UIFlatButton(text="I", width=width_button, height= height_button)
        self.firstLineLayout.add(i_button)
        i_button.on_click = self.on_click_i

        o_button = arcade.gui.UIFlatButton(text="O", width=width_button, height= height_button)
        self.firstLineLayout.add(o_button)
        o_button.on_click = self.on_click_o

        p_button = arcade.gui.UIFlatButton(text="P", width=width_button, height= height_button)
        self.firstLineLayout.add(p_button)
        p_button.on_click = self.on_click_p

        # Second Line
        self.secondLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        a_button = arcade.gui.UIFlatButton(text="A", width=width_button, height= height_button)
        self.secondLineLayout.children.append(a_button)
        a_button.on_click = self.on_click_a

        s_button = arcade.gui.UIFlatButton(text="S", width=width_button, height= height_button)
        self.secondLineLayout.children.append(s_button)
        s_button.on_click = self.on_click_s

        d_button = arcade.gui.UIFlatButton(text="D", width=width_button, height= height_button)
        self.secondLineLayout.children.append(d_button)
        d_button.on_click = self.on_click_d

        f_button = arcade.gui.UIFlatButton(text="F", width=width_button, height= height_button)
        self.secondLineLayout.children.append(f_button)
        f_button.on_click = self.on_click_f

        g_button = arcade.gui.UIFlatButton(text="G", width=width_button, height= height_button)
        self.secondLineLayout.children.append(g_button)
        g_button.on_click = self.on_click_g

        h_button = arcade.gui.UIFlatButton(text="H", width=width_button, height= height_button)
        self.secondLineLayout.children.append(h_button)
        h_button.on_click = self.on_click_h

        j_button = arcade.gui.UIFlatButton(text="J", width=width_button, height= height_button)
        self.secondLineLayout.children.append(j_button)
        j_button.on_click = self.on_click_j

        k_button = arcade.gui.UIFlatButton(text="K", width=width_button, height= height_button)
        self.secondLineLayout.children.append(k_button)
        k_button.on_click = self.on_click_k

        l_button = arcade.gui.UIFlatButton(text="L", width=width_button, height= height_button)
        self.secondLineLayout.children.append(l_button)
        l_button.on_click = self.on_click_l

        # Third Line
        self.thirdLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        y_button = arcade.gui.UIFlatButton(text="Y", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(y_button)
        y_button.on_click = self.on_click_y

        x_button = arcade.gui.UIFlatButton(text="X", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(x_button)
        x_button.on_click = self.on_click_x

        c_button = arcade.gui.UIFlatButton(text="C", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(c_button)
        c_button.on_click = self.on_click_c

        v_button = arcade.gui.UIFlatButton(text="V", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(v_button)
        v_button.on_click = self.on_click_v

        b_button = arcade.gui.UIFlatButton(text="B", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(b_button)
        b_button.on_click = self.on_click_b

        n_button = arcade.gui.UIFlatButton(text="N", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(n_button)
        n_button.on_click = self.on_click_n

        m_button = arcade.gui.UIFlatButton(text="M", width=width_button, height= height_button)
        self.thirdLineLayout.children.append(m_button)
        m_button.on_click = self.on_click_m

        # Keyboard Layout
        self.keyboardLayout = arcade.gui.UIBoxLayout()
        self.keyboardLayout.add(self.ui_text_label)
        self.keyboardLayout.add(self.firstLineLayout)
        self.keyboardLayout.add(self.secondLineLayout)
        self.keyboardLayout.add(self.thirdLineLayout)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
            child=self.keyboardLayout)
        )

    # Click Events Buttons
    def on_click_q(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "Q"
            self.update_text()

    def on_click_w(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "W"
            self.update_text()

    def on_click_e(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "E"
            self.update_text()

    def on_click_r(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "R"
            self.update_text()

    def on_click_t(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "T"
            self.update_text()

    def on_click_z(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "Z"
            self.update_text()

    def on_click_u(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "U"
            self.update_text()

    def on_click_i(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "I"
            self.update_text()

    def on_click_o(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "O"
            self.update_text()

    def on_click_p(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "P"
            self.update_text()

    def on_click_a(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "A"
            self.update_text()

    def on_click_s(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "S"
            self.update_text()

    def on_click_d(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "D"
            self.update_text()

    def on_click_f(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "F"
            self.update_text()

    def on_click_g(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "G"
            self.update_text()

    def on_click_h(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "H"
            self.update_text()

    def on_click_j(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "J"
            self.update_text()

    def on_click_k(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "K"
            self.update_text()

    def on_click_l(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "L"
            self.update_text()

    def on_click_y(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "Y"
            self.update_text()

    def on_click_x(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "X"
            self.update_text()

    def on_click_c(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "C"
            self.update_text()

    def on_click_v(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "V"
            self.update_text()

    def on_click_b(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "B"
            self.update_text()

    def on_click_n(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "N"
            self.update_text()

    def on_click_m(self, event):
        if len(self.ui_text_label.text) < max_length_input:
            self.pressed_key = "M"
            self.update_text()

    def update_text(self):
        label_text = self.ui_text_label.text
        self.ui_text_label.text = label_text + self.pressed_key
        print("Name: ", self.ui_text_label.text)

    def on_draw(self):
        self.clear()
        self.manager.draw()


def main():
    window = Window(title='Arcane Arcade', fullscreen=False)
    game = Keyboard()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()