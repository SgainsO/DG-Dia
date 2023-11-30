from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.base import runTouchApp

# Load the kv file
Builder.load_file('main.kv')
class MyBoxLayout(Widget):
    pass
class BuildApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    BuildApp().run()
