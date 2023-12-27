from openai import OpenAI
import os


def StoreKey(key):
  with open("KeyStore.txt", "w") as file:
    file.write(key)
    file.close()


class GPT:
  def __init__(self, apiKey):
    os.environ["OPENAI_API_KEY"] = apiKey
    self.client = OpenAI()
    self.AllSummaries = []
    StoreKey(apiKey)


  def Summarize(self, toSummarize : str):
    this_message = [{"role": "system",
                     "content": 'Briefly summarize the paragraph you were given. Summarize in bulletpoints. '
                                'After every bullet put an endline character'},
                    {"role": "user", "content": toSummarize}]
    self.AllSummaries.append([{"role": "user", "content": toSummarize}])
    chat_completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages= this_message
    )
    return chat_completion.choices[0].message.content

