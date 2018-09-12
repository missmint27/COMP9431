#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:56:09 2018

@author: ella
"""
import speech_recognition as sr

r = sr.Recognizer()
#harvard = sr.AudioFile("jackhammer.wav")
#with harvard as source:
#    r.adjust_for_ambient_noise(source, duration=0.5)
#    audio = r.record(source)
    #audio1 = r.record(source, duration=4) #first four seconds
    #audio2 = r.record(source, duration=4) #always move ahead
    #audio = r.record(source, offset=4, duration=3)
#r.recognize_google(audio, show_all=True)
#r.recognize_google_cloud(audio)
#r.recognize_sphinx(audio)
#r.recognize_sphinx(audio1)
#r.recognize_sphinx(audio2)

mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

r.recognize_google(audio)
