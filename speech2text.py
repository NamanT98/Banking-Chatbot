import json
import wave
import recorder
from vosk import Model, SetLogLevel,KaldiRecognizer

SetLogLevel(0)
speech2text_model = Model(lang="en-us")
sample_rate=44100

running = None
rec=recorder.Recorder(channels=1,rate=sample_rate)
text_extracter=KaldiRecognizer(speech2text_model,sample_rate)

def start():
    global running
    if running is not None:
        print('already running')
    else:
        running = rec.open("audio.wav", 'wb')
        running.start_recording()
        print("Started recording")

def stop():
    global running
    if running is not None:
        running.stop_recording()
        running.close()
        running = None
        print('Stopped recording')
        text=speech2text(text_extracter)
        print("text extracted")
        return text
    else:
        print('not running')

def speech2text(ext):
    wf = wave.open('audio.wav', 'rb')
    while True:
        data=wf.readframes(4000)
        if len(data)==0: 
            break
        ext.AcceptWaveform(data)
    return json.loads(ext.FinalResult())['text']

