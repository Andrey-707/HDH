# Test_Speach.
from colorama import init, Fore, Back, Style
import pyttsx3

init()

print(Fore.WHITE)
print("Program start")

print(Fore.YELLOW)

speak_engine = pyttsx3.init()

# если установлен голосовой пакет для синеза речи RHVoice
voices = speak_engine.getProperty("voices")
speak_engine.setProperty("voice", voices[1].id)

what = input() # Вводим текст с клавиауры, программа говорит через колонки.

speak_engine.say(what)
speak_engine.runAndWait()

print(Fore.WHITE)
print("Program finish")
