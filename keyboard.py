import arcade
import arcade.gui
from arcade import Window
import keyboard

class Keyboard(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


        self.ui_text_label = arcade.gui.UILabel(text= '', width=200, height=20, align='center')

        # First Line
        self.firstLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        q_button = arcade.gui.UIFlatButton(text="Q", width=30)
        self.firstLineLayout.children.append(q_button)
        q_button.on_click = self.on_click_q

        w_button = arcade.gui.UIFlatButton(text="W", width=30)
        self.firstLineLayout.add(w_button)
        w_button.on_click = self.on_click_w

        e_button = arcade.gui.UIFlatButton(text="E", width=30)
        self.firstLineLayout.add(e_button)

        r_button = arcade.gui.UIFlatButton(text="R", width=30)
        self.firstLineLayout.add(r_button)

        t_button = arcade.gui.UIFlatButton(text="T", width=30)
        self.firstLineLayout.children.append(t_button)

        z_button = arcade.gui.UIFlatButton(text="Z", width=30)
        self.firstLineLayout.add(z_button)

        u_button = arcade.gui.UIFlatButton(text="U", width=30)
        self.firstLineLayout.add(u_button)

        i_button = arcade.gui.UIFlatButton(text="I", width=30)
        self.firstLineLayout.add(i_button)

        o_button = arcade.gui.UIFlatButton(text="O", width=30)
        self.firstLineLayout.add(o_button)

        p_button = arcade.gui.UIFlatButton(text="P", width=30)
        self.firstLineLayout.add(p_button)

        # Second Line
        self.secondLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        a_button = arcade.gui.UIFlatButton(text="A", width=30)
        self.secondLineLayout.children.append(a_button)

        s_button = arcade.gui.UIFlatButton(text="S", width=30)
        self.secondLineLayout.children.append(s_button)

        d_button = arcade.gui.UIFlatButton(text="D", width=30)
        self.secondLineLayout.children.append(d_button)

        f_button = arcade.gui.UIFlatButton(text="F", width=30)
        self.secondLineLayout.children.append(f_button)

        g_button = arcade.gui.UIFlatButton(text="G", width=30)
        self.secondLineLayout.children.append(g_button)

        h_button = arcade.gui.UIFlatButton(text="H", width=30)
        self.secondLineLayout.children.append(h_button)

        j_button = arcade.gui.UIFlatButton(text="J", width=30)
        self.secondLineLayout.children.append(j_button)

        k_button = arcade.gui.UIFlatButton(text="K", width=30)
        self.secondLineLayout.children.append(k_button)

        l_button = arcade.gui.UIFlatButton(text="L", width=30)
        self.secondLineLayout.children.append(l_button)

        # Third Line
        self.thirdLineLayout = arcade.gui.UIBoxLayout(vertical=False)

        y_button = arcade.gui.UIFlatButton(text="Y", width=30)
        self.thirdLineLayout.children.append(y_button)

        x_button = arcade.gui.UIFlatButton(text="X", width=30)
        self.thirdLineLayout.children.append(x_button)

        c_button = arcade.gui.UIFlatButton(text="C", width=30)
        self.thirdLineLayout.children.append(c_button)

        v_button = arcade.gui.UIFlatButton(text="V", width=30)
        self.thirdLineLayout.children.append(v_button)

        b_button = arcade.gui.UIFlatButton(text="B", width=30)
        self.thirdLineLayout.children.append(b_button)

        n_button = arcade.gui.UIFlatButton(text="N", width=30)
        self.thirdLineLayout.children.append(n_button)

        m_button = arcade.gui.UIFlatButton(text="M", width=30)
        self.thirdLineLayout.children.append(m_button)

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
    def on_click_q(self, event):
        if len(self.ui_text_label.text) < 3:
            self.TEXT = "Q"
            self.update_text()

    def on_click_w(self, event):
        if len(self.ui_text_label.text) < 3:
            self.TEXT = "W"
            self.update_text()

    def update_text(self):
        helper = self.ui_text_label.text
        self.ui_text_label.text = helper + self.TEXT
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