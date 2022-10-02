import os
import io
from subprocess import call
from time import time_ns

from flask import Flask, request, Response
from flask import jsonify, send_from_directory
from flask_cors import CORS, cross_origin

# all tts, stt, audio modules
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = 'Pranjal-Is-A-Sexy-Man' 

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
    absolute_fname = f"./flaskr/static/wav/{time_ns()}.wav"
    byte_file = io.BytesIO(data)
    AudioSegment.from_file(byte_file).export(absolute_fname, format="wav")
 
    return stt(absolute_fname)
    

def stt (absolute_fname):
    text = ""
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(absolute_fname) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return format_stt_data(text)

def format_stt_data (text):
    DATA = {
                "status" : "OK",
                "src" : text,
            }


# endpoint for registering
@app.route('/api/register', methods=['POST'])
def register ():
    UID = create_user_data_storage(time_ns())

    resp = Response('REGISTERED')
    resp.set_cookie("indriyeah",value=str(UID),domain='0.0.0.0')

    return resp

def create_user_data_storage (UID):
    execute_bash(f'sh ./create_user_data_storage.sh {UID}')
    print(f"[\033[0;32mok\033[0;0m] created user : {UID}")

    return UID

def execute_bash (command):
    call (command.split(' '))

@app.route('/api/append_history/<history_item>',methods=['GET'])
def append_history (history_item):
    UID = request.cookies.get("indriyeah-regd")

    append_to_history(UID,history_item)

    return "APPENDED "+history_item

def append_to_history (UID, history_item):
    execute_bash(f"sh ./append_to_history.sh {UID} {history_item[::-1]}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
