# pyaudio.Playback_wav_file2. НЕ блокирует поток выполнения.

import pyaudio
import wave
import sys
import time

from path import path


# path to file_name.wav
wf = wave.open(path, "rb")

# instantiate PyAudio
p = pyaudio.PyAudio()

# define callback
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open stream using callback
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

# start the stream
stream.start_stream()

# wait for stream to finish
while stream.is_active():
    time.sleep(0.1)

# stop stream
stream.stop_stream()
stream.close()
wf.close()

# close PyAudio
p.terminate()
