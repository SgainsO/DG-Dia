import sys
import os
import io
import contextlib
from contextlib import contextmanager
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

#https://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto


console_out = sys.stdout
console_err = sys.stderr
class item:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount

    name: str
    amount: int


def RemoveErrorBrackets(paragraph):
     newPar = ""
     for c in range(len(paragraph)):
          if paragraph[c] == '[':
               while paragraph[c] != ']':
                    c += 1
          else:
               newPar += paragraph[c]
     return newPar


# This will need to be changed on local installs        .....\\Lib\\site-packages\\TTS\\.models.json
path = "C:\\Users\\sudar\\anaconda3\\envs\\yolo\\Lib\\site-packages\\TTS\\.models.json"

store_pages = []

@contextmanager
def suppress_stdout():
    with open(os.devnull, 'w') as fnull:
        save_stdout = sys.stdout
        sys.stdout = io.StringIO()
        yield
        sys.stdout = save_stdout



def TTSVoice(text, Name):
     nMp3 = 0  # this long string is an example
     present = False

     text = RemoveErrorBrackets(text)   #Remakes the text

     for i in store_pages:
          if Name == i.name:
               nMp3 = i.amount
               i.amount += 1
               present = True  # of a voice id

     if present == False:
          newItem = item(name=Name, amount=0)
          store_pages.append(newItem)

     mm = ModelManager(path)

     m_path, con_path, m_item = mm.download_model("tts_models/en/ljspeech/speedy-speech")

     v_path, v_conf_path , _ = mm.download_model("vocoder_models/en/ljspeech/hifigan_v2")

     syn = Synthesizer(
          tts_checkpoint=m_path,
          tts_config_path=con_path,
          vocoder_checkpoint=v_path,
          vocoder_config= v_conf_path
     )
     original_stdout = sys.stdout
     sys.stdout = open(os.devnull, 'w')
     try:
        with suppress_stdout():
            outputs = syn.tts(text)
     except:
        with suppress_stdout():
            outputs = syn.tts("There is a character that I had trouble understanding ")
        print(f"THE FOLLOWING RESULTED IN AN ERROR: {text}")

     sys.stdout = original_stdout

     syn.save_wav(outputs, f"out/{Name}{nMp3}.wav")

def DownloadAllFromWiki(wiki, name):
     print(f"reading through {name}")
     for tag in wiki:
          if tag.text != "\n":
               TTSVoice(tag.text, name)