from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.lang import Builder
from kivy.clock import Clock
from landing import *
from gpt import *
import os

Builder.load_file("MCan.kv")

r = Reader()                  #This is the class that will navigate through the website

s : GPT


class SummarButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Summarize(self):
        contents = ""
        with open(r.LastPlayed + ".txt", 'r') as file:
            contents = file.read()
        return s.Summarize(contents)         #lastPlayed is saved so the text can be
                                                                           #accesed and past in


class SendGPTButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def SendKey(self, key : str):
        print("BUTTON PRESSED")
        global s
        if key != "":
            s = GPT(key)          #sets api key
        else:
            with open("KeyStore.txt", "r") as file:
                s = GPT(file.read())

    def TurnOff(self):
        sendKey_button = self.ids.sendKey
        print(sendKey_button.text)




class StartReadingButton(Button):        #Define a new type of button
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def StartVoiceToText(self, topic :str):       #Access What is in a text input and send to function
        print(topic)
        r.StartReading(topic)

class ForewardAudioButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def NextSong(self):
        worked = r.PlayNextFile()          ##Returns if file does not exist, Still waiting for load
        print(f"WORKED WORKED--------------------------------------------------- {worked}")
        if worked == 0:
            content = Label(text="File does not exist. Still waiting for load.")   ##creates a popup to update user
            popup = Popup(title="Alert", content=content, size_hint=(.4, .3))
            Clock.schedule_once(popup.dismiss, 1)
            popup.open()
class PrevAudioButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def PrevSong(self):
        r.PlayPrevFile()

class TwoCanvasLayout(BoxLayout):
    pass

class TwoCanvasApp(App):
    def build(self):
        return TwoCanvasLayout()






if __name__ == '__main__':
    TwoCanvasApp().run()
