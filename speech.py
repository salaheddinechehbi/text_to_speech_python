from gtts import gTTS
import os

my_text1 = "Hello salah you have done a great job. you are in"
language = "en"
output1 = gTTS(text=my_text1, lang=language, slow=False)
output1.save("output1.mp3")

fh = open("text.txt","r")

my_text = fh.read().replace("\n", " ")

language = "en"
output = gTTS(text=my_text, lang=language, slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")