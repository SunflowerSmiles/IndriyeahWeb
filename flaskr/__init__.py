import os
from time import time_ns

from flask import Flask, request
from flask import jsonify, send_from_directory

# text to speech module
from gtts import gTTS

app = Flask(__name__)

# this is the api endpoint for the tts function
@app.route('/api/text-to-speech',methods=['POST'])
def tts_api_endpoint ():
    data = request.get_json()

    DATA = tts(
            text=data.pop("src",None),
            lang=data.pop("lang",None),
            slow=data.pop("slow",None)
        )

    return jsonify(DATA)

# where the actual tts happens
def tts (text, lang='en', slow=False):
    lang = lang  if lang  else 'en'
    slow = False if slow else True

    uid = time_ns()
    gtts_object = gTTS(text=text,lang=lang,slow=slow)

    print(os.getcwd())
    gtts_object.save(f'./flaskr/static/tts/{uid}.mp3')

    DATA = {'filename' : uid}

    return DATA

# static fetching of the .mp3 file
@app.route('/mp3/<path:filename>',methods=['GET'])
def fetch_tts_mp3 (filename):
    return send_from_directory('./static/tts/.',filename)
    
