'''
Created on Jul 5, 2019

@author: sipika
'''
import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print('speak anything:')
    audio = r.listen(source)

    try:
        text =r.recognize_google(audio,language='hi', show_all=False)
        print('you said: {}'.format(text))
    except:
        print('sorry i cant understand')