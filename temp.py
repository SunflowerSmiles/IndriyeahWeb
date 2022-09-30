from gtts import gTTS
import os

txt = 'Hey whats up riya'
lang = 'en'

tts = gTTS(text=txt,lang=lang,slow=True)
tts.save('./temp.mp3')
