import os
from time import time_ns

from flask import Flask, request

# text to speech module
from gtts import gTTS

app = Flask(__name__)

# this is the api endpoint for the tts function
@app.route('/api/text-to-speech',methods=['POST','GET'])
def tts_api_endpoint ():
#    data = request.get_json()
#    print(data)
    return '<h1>Hello World</h1>'

def tts (text, lang='en', slow='False'):
    uid = time_ns()
    gtts_object = gTTS(text=text,lang=lang,slow=slow)
    gtts.save(f'./static/tts/{uid}.mp3')
