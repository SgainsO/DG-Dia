import os
import requests
import time
import threading
#from TextTo11Lab import *
from TextToVoice import *
from bs4 import BeautifulSoup
class page:
    def __init__(self, n, tag, play):
        self.name = n
        self.tag = tag
        self.am_played = play

def EmptyDirec(folder):
    for file in os.listdir(folder):
        os.remove(f"out/{file}")
class Reader:
    def __init__(self):
        self.Topic_Name = ""
        self.pgS = []                   #This will be used as the stack
        self.LastPlayed = ""

    def StartReading(self, topic_name):    #this topic name is being given by the user and put in the variable
        self.Topic_Name = topic_name
        EmptyDirec("out")
        url = "https://en.wikipedia.org/wiki/" + self.Topic_Name
        response = requests.get(url)

        s = BeautifulSoup(response.text, 'html.parser')

        wiki_text = s.find_all(['p', 'h2'])
        length_of_wiki = len(wiki_text)
        vdT = threading.Thread(target=DownloadAllFromWiki, args=(wiki_text, self.Topic_Name))
        vdT.start()

        # NOTE: This stack is here for future implementation of being able to read through multiple pages

        self.pgS.append(page(self.Topic_Name, len(wiki_text), 0))  # Add another to the stack


    def PlayNextFile(self):
        if self.pgS[-1].am_played < self.pgS[-1].tag:
            self.pgS[-1].am_played += 1
            file_path = "out/" + f"{self.pgS[-1].name}{self.pgS[-1].am_played}.wav"
            print(file_path)
            if os.path.exists(file_path):
                self.LastPlayed = file_path[:-4]
                os.startfile(os.path.normpath(file_path))
            else:
                self.pgS[-1].am_played -= 1             #We undo the change we made previously
                return 0

    def PlayPrevFile(self):
        if self.pgS[-1].am_played > 0:
            self.pgS[-1].am_played -= 1
            file_path = "out/" + f"{self.pgS[-1].name}{self.pgS[-1].am_played}.wav"
            if os.path.exists(file_path):
                self.LastPlayed = file_path[:-4]
                os.startfile(os.path.normpath(file_path))
            else:
                self.pgS[-1].am_played += 1          #We undo the change we made previously
                return 0
