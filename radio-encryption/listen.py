import pyaudio
import wave
import pyAesCrypt
import io
import socket

ip = '192.168.1.10'

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,7777))

frames=[]
p = pyaudio.PyAudio()

key = "hello we are secure"
bufferSize = 1024 * 5

stream = p.open(format = sample_format,
                channels = channels,
                rate = fs,
                output = True)

# Read data in chunks

data=s.recv(8192)
while True:
    fDec = io.BytesIO()
    print(data)
    pyAesCrypt.decryptStream(io.BytesIO(data), fDec, key, bufferSize, 4391)
    stream.write(fDec.getvalue())
    data=s.recv(8192)

stream.close()
p.terminate()



# initialize decrypted binary stream
audio = b''.join(frames)
fIn = io.BytesIO(audio)
fDec = io.BytesIO()
ctlen = len(fIn.getvalue())


pyAesCrypt.decryptStream(fIn, fDec, key, bufferSize, ctlen)
decrypted_audio = fDec.getvalue()

