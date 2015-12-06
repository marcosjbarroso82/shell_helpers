#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# https://pypi.python.org/pypi/SpeechRecognition/
import speech_recognition as sr
from time import sleep, time
from keys.keyboard import KeyBoard


import sys
import pyaudio

from apps.app_pycharm import PyCharm


# linux only!
assert("linux" in sys.platform)

r = sr.Recognizer()
m = sr.Microphone()



def log2(buffer, done, callback, keyb, sleep_interval=.005):
    apps = []
    apps.append(PyCharm())

    print ("log2 !!!!!")
    while not done():
        sleep(sleep_interval)
        changed, modifiers, keys = keyb.fetch_keys()
        if changed: callback(buffer, time(), modifiers, keys, apps, keyb)


class Buffer():
    buffer = ""

    def __str__(self):
        return self.buffer






def get_menu_or_exec(buffer, t, modifiers, keys, apps, keyb, *args, **kwargs):
    global r, m
    try:
        if modifiers['right alt']:
            try:
                with m as source:
                    print("Say something!")
                    audio = r.listen(source)
                    print("Got it! Now to recognize it...")
                    try:
                        # recognize speech using Google Speech Recognition
                        print("processing...")
                        value = r.recognize_google(audio)

                        # we need some special handling here to correctly print unicode characters to standard output
                        if str is bytes: # this version of Python uses bytes for strings (Python 2)
                            print(u"P2 You said: {}".format(value).encode("utf-8"))

                            for app in apps:
                                if app.is_focused():
                                    app.command(format(value).encode("utf-8"))
                        else: # this version of Python uses unicode for strings (Python 3+)
                            print("P3 You said: {}".format(value))
                            for app in apps:
                                if app.is_active():
                                    app.command(format(value))


                    except sr.UnknownValueError:
                        print("Oops! Didn't catch that")
                    except sr.RequestError as e:
                        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            except:
                print("ERROR at listening...")

    except:
        print("eror en get_menu_or_exec")



try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))

except KeyboardInterrupt:
    pass


import datetime
print (datetime.datetime.now().strftime("%M:%S"))

if __name__ == "__main__":

    keyb = KeyBoard()

    now = time()
    buffer = Buffer()
    # done = lambda: time() > now + 60
    done = lambda: False
    log2(buffer, done, get_menu_or_exec, keyb)

    print (datetime.datetime.now().strftime("%M:%S"))