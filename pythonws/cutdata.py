import numpy as np
from pydub import AudioSegment

path1 = "D://pythonws//ML_data//bad_ball_joint//00.wav"
path2 = "D://pythonws//ML_data//bad_ball_joint//01.wav"
test_path = "D://pythonws2//makeMLdata//test"

wav1 = AudioSegment.from_wav(path1)
wav2 = AudioSegment.from_wav(path2)

wav1_10sec = wav1[10000:20000]
wav2_5sec = wav2[5000:10000]



print(wav1_10sec)

print(type(wav1_10sec))
print(len(wav1_10sec))

new_wav = wav1_10sec
new_wav += wav2_5sec

print(type(new_wav))
print(len(new_wav))

#new_wav.export("new_wav.wav", format="wav")
tests = [1, 3, 5, 7]
for time in tests:
    if(tests.index(time)%2==0):
        start = time
    else:
        finish = time
        print("start : "+str(start))
        print("finish : "+str(finish))
