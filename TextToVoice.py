from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

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

   #  text = " "
     try:
          outputs = syn.tts(text)
     except:
          outputs = syn.tts("There is a character herer that I had trouble understanding ")
          print(f"the following resulted in an error: {text}")


     syn.save_wav(outputs, f"out/{Name}{nMp3}.wav")

def DownloadAllFromWiki(wiki, name):
     print(f"reading through {name}")
     for tag in wiki:
          if tag.text != "\n":
               TTSVoice(tag.text, name)