import pyttsx3

engine = pyttsx3.init()

text = "hello, 我是王高杰"

engine.setProperty('rate', 250)
engine.setProperty("volume", 0.7)

engine.say(text)

engine.runAndWait()