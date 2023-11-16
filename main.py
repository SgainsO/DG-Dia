import os
import requests 
import threading
from TextTo11Lab import *
from TextToVoice import *
from bs4 import BeautifulSoup
class page:
    def __init__(self, n, tag, play):
        self.name = n
        self.tag = tag
        self.amPlayed = play

    name : str
    amOfTag: int
    amPlayed: int




Topic_Name = "Destiny_(streamer)"
EmptyDirec("out")
url = "https://en.wikipedia.org/wiki/" + Topic_Name

response = requests.get(url)



s = BeautifulSoup(response.text, 'html.parser')

wiki_text = s.find_all(['p', 'h2'])
lengthOfWiki = len(wiki_text)
vdT = threading.Thread(target = DownloadAllFromWiki, args=(wiki_text, Topic_Name))

vdT.start()

pgS = []                    #this will be treated as a stack to
pgS.append(page(Topic_Name, len(wiki_text), 0))
while True:
    file_path = "out/" + f"{pgS[-1].name}{pgS[-1].amPlayed}.wav"
    if os.path.exists(file_path):
        os.startfile(file_path)
        pgS[-1].amPlayed+=1
        input("-----------Press Any Button To Load the next text ")
    else:
        print("Voice is loading...")