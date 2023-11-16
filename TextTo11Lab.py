import os
import shutil
import requests
import elevenlabs
from bs4 import BeautifulSoup

class item:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount

    name: str
    amount: int

store_pages = []


def EmptyDirec(folder):
    for file in os.listdir(folder):
        os.remove(f"out/{file}")

def GetVoice(TextInput, Name):
    url = "https://api.elevenlabs.io/v1/text-to-speech/zrHiDhphv9ZnVXBqCLjz/stream"
    nMp3 = 0                     #this long string is an example
    present = False
    for i in store_pages:
        if Name == i.name:
            nMp3 = i.amount
            i.amount += 1
            present = True                                           #of a voice id

    if present == False:
        newItem = item(name = Name, amount = 0)
        store_pages.append(newItem)


    CHUNK_SIZE = 1024
    headers ={
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "PUT KEY HERE"           #Put your API key here
    }

    data ={
        "text": TextInput,                 #Text input will contain the wikipedia Paragraph
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
            }
        }
    response = requests.post(url, json=data, headers=headers, stream=True)
    with open(f"making/{Name}{nMp3}.mp3", 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
        shutil.move(f"making/{Name}{nMp3}.mp3", 'out', copy_function = shutil.copytree)



def DownloadAllFromWiki_11Lab(wiki, name):
    for tag in wiki:
        GetVoice(tag.text, name)
