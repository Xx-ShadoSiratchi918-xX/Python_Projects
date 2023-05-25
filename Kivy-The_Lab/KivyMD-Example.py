from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "A700"
        self. theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="Show",
                                         pos_hint={"center_x": 0.5, "center_y": 0.5})
        icon_btn = MDFloatingActionButton(icon="lenguage-python",
                                          pos_hint={"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(btn_flat)
        return screen


DemoApp().run()
