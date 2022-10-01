import os
import io
from time import time_ns

from flask import Flask, request
from flask import jsonify, send_from_directory
from flask_cors import CORS, cross_origin

# all tts, stt, audio modules
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition

app = Flask(__name__)
CORS(app, support_credentials=True)

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
    

# the endpoint forspeech to text
@app.route('/api/speech-to-text',methods=['POST','GET'])
def stt_api_endpoint ():
    data = request.get_data()
    uid_fname = f"{time_ns()}.wav"
    byte_file = io.BytesIO(data)
    os.lis()
    AudioSegment.from_file(byte_file).export(f'./static/wav/{uid_fname}')

    stt(f'./static/wav/{uid_fname}')
    
    return "ok"

def stt (absolute_fname):
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(absolute_fname) as source:
        audio_data = recognizer.record(source)
        text = r.recognize_google(audio_data)

        print(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
