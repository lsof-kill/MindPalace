import pyaudio
import wave
import pyAesCrypt
import io
import socket
from threading import Thread

port = 7777
slaves=[]

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",port))
    s.listen()
    print('listening')
    slave, slave_address = s.accept()
    slaves.append(slave)

ListenerThread = Thread(target=listen,args=(port,), daemon=True)
ListenerThread.start()


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5


key = "hello we are secure"
bufferSize = 1024 * 5


p = pyaudio.PyAudio()  # Create an interface to PortAudio

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

while(len(slaves)==0):
    continue

print('Recording')

# Store data in chunks for n seconds
for i in range(0, int(fs / chunk * seconds)):
# for i in range(0, 1):

    data = stream.read(chunk)
    fCiph = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(data), fCiph, key, bufferSize)
    slaves[0].sendall(fCiph.getvalue())
    print(len(fCiph.getvalue()))


stream.stop_stream()
stream.close()
p.terminate()

print('Finished recording')



# audio = b''.join(frames)
# fIn = io.BytesIO(audio)

# pyAesCrypt.encryptStream(fIn, fCiph, key, bufferSize)
# encrypted_audio = fCiph.getvalue()

