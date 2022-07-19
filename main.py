# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""

# https://github.com/attreyabhatt/KivyMD-Basics

'''
from kivy.app import App
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        value = TextInput(text="Enter value here")
        return value

MainApp().run()

'''
# LABELS

"""
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoApp(MDApp):
    def build(self):
        # halign = horizontal align

        label = MDLabel(text="Hello world", halign="center", theme_text_color="Error",
                        font_style="Subtitle2")

        # label = MDLabel(text="Hello world", halign="center",theme_text_color="Custom",
        #                 text_color=(0,0,1,1))

        # label = MDIcon(icon="language-python", halign="center")
        return label


DemoApp().run()

"""

# BUTTONS

'''
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.lang import Builder


KV = """
<RectangleFlatButton>:
    ripple_color: 0, 0, 0, .2
    background_color: 0, 0, 0, 0
    color: root.primary_color
    canvas.before:
        Color:
            rgba: root.primary_color
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)
Screen:
    canvas:
        Color:
            rgba: 0.9764705882352941, 0.9764705882352941, 0.9764705882352941, 1
        Rectangle:
            pos: self.pos
            size: self.size
"""


class RectangleFlatButton(TouchRippleBehavior, Button):
    primary_color = [
        0.12941176470588237,
        0.5882352941176471,
        0.9529411764705882,
        1
    ]

    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            self.ripple_show(touch)
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
            return True
        return False


class MainApp(App):
    def build(self):
        screen = Builder.load_string(KV)
        screen.add_widget(
            RectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size_hint=(None, None),
                size=(dp(110), dp(35)),
                ripple_color=(0.8, 0.8, 0.8, 0.5),
            )
        )
        return screen


MainApp().run()

'''

# TEXT FIELD

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

Window.size = (360, 600)


class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        username = MDTextField(text="Enter Weight",
                               helper_text="This will disappear when you click off",
                               helper_text_mode="on_focus",
                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint_x=None, width=200)
        screen.add_widget(username)
        return screen


DemoApp().run()
