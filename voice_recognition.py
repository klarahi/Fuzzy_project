"""
Created on Thu Mar 17 16:34:46 2022
​
@author: svein
"""
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import os
import ffmpeg
from scipy.io import wavfile
import numpy as np

def Speech_to_text():
    myfile="output.wav"

    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:    ## Show an error ##
        print("Error: %s file not found" % myfile)
 ##
    print("recording start")
    fs = 44100  # Sample rate
    seconds = 4  # Duration of recording

    sd.default.dtype='int32', 'int32'

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print("recording ended")
    wavfile.write("output.wav", fs, myrecording)  # Save as WAV file

    def SpeechToText():
        r = sr.Recognizer()   #Speech recognition
        audio = sr.AudioFile("output.wav")
        with audio as source:
            print("Wait. Program Starting")
            audio = r.record(source)
            message = r.recognize_google(audio)
            print("Check: "+message)
        return message
    Ord=SpeechToText()
    return Ord

if __name__ == "__main__":
    print(Speech_to_text())