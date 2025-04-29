import wave

# from pydub import AudioSegment

# Notes: 
# Number of channels: 1 = mono, 2 = stereo
# Sample width: 1 = 8-bit, 2 = 16-bit, 4 = 32-bit float
# Frame rate: number of samples per second
# Number of frames: number of samples in the file
# Value of a frame: 0 = silence, 1 = max volume, -1 = min volume
# The value of a frame is the amplitude of the sound wave at that point in time.

# Code to convert stereo to mono
# audio = AudioSegment.from_wav('wav_files/file_example_WAV_1MG.wav')
# audio = audio.set_channels(1)
# audio.export('wav_files/file_example_WAV_1MG_mono.wav', format="wav")

file = 'wav_filestest.wav'

obj = wave.open(file, 'rb')
print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())
print("Length of the file in seconds: ", obj.getnframes()/obj.getframerate())

frames = obj.readframes(-1)
print(type(frames), type(frames[0]), len(frames), (len(frames)/obj.getsampwidth()/obj.getnchannels()))
obj.close()
obj_new = wave.open(file, 'wb')

obj_new.setnchannels(1)

obj_new.setsampwidth(2)
obj_new.setframerate(44100)
obj_new.writeframes(frames)


obj_new.close()