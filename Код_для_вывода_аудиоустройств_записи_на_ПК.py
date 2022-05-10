# Код для вывода аудиоустройств записи

# # 1. Способ
# import speech_recognition as sr

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     # print(f"{index}. Microphone with name \"{name}\" found for 'Microphone device'")
#     print(f"{index+1}. {name}")

# 2. Способ
import pyaudio

p = pyaudio.PyAudio()
for index, name in enumerate(range(p.get_device_count())):
    print(f"{index+1}. {p.get_device_info_by_index(name)['name']}")