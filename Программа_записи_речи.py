# Программа записи речи. Опционально на английском.
import speech_recognition as sr

from rich import print


print("[bold magenta]Program start[/]")

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
	print("Say what ...")
	audio = r.listen(source)

query = r.recognize_google(audio, language="eng=ENG")
print("You say: " + query.lower())


print("[bold magenta]Program finish[/]")
input()
