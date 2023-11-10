import os
import requests
from bs4 import BeautifulSoup

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


url = "https://en.wikipedia.org/wiki/%C3%85bo_Bloodbath"

response = requests.get(url)


s = BeautifulSoup(response.text, 'html.parser')

wiki_text = s.find_all(['p', 'h2'])

print(wiki_text)
print(len(wiki_text[1]))



if len(wiki_text[1]) < 10:
    print("this page a kinda short, is their anything else on the previous section ")

for tag in wiki_text:
    print(tag.text)