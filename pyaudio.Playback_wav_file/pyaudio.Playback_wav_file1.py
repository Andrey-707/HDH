# pyaudio.Playback_wav_file1. Блокирует поток выполнения.

import pyaudio
import wave
import sys

from path import path


CHUNK = 1024

# path to file_name.wav
wf = wave.open(path, "rb")

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream
while data != "":
    stream.write(data)
    data = wf.readframes(CHUNK)

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
