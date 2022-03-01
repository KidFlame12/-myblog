#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:17:53 2022

@author: Bradley
"""

from tkinter import *
import speech__recoginition as sr
import pyttsx3
from datetime import datetime

root = Tk()
root.geometry("500x500")

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait
    
def r_audio():
    speech_recognisor= sr.Recognisor
    with sr.Michrophone() as source:
        audio=  speech_recognisor.listen(source)
    voice_data=''
    try:
        voice_data= speech_recognisor.recognize_google(audio, language='en-in')
    except sr.UnkownValueError:
        print('Please repeat i did not get that')
    print(voice_data)

def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is James")
        print('my name is James')
        
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    r_audio()
    root.mainloop
