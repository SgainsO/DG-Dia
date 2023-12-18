from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("MCan.kv")


class TwoCanvasLayout(BoxLayout):
    pass


class TwoCanvasApp(App):
    def build(self):
        return TwoCanvasLayout()


if __name__ == '__main__':
    TwoCanvasApp().run()
