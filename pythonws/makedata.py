from pytube import YouTube
from pydub import AudioSegment
import subprocess

#https://wikidocs.net/26366

name = "bad_ball_joint"                             #label name
data_path = "C://Users//eom02//Documents//GitHub//Sound-mechanic//pythonws//ML_data//"           #ML data txt file 모아둔 곳
file_name = name + ".txt"
wav_path = data_path + name + "_mp4//"   #save mp4 data and 그냥 잘린 데이터
ml_path = data_path + name +"//"         #complete machine learning training data

time_slice = 5
time_interval = 1

f = open(data_path + file_name, 'r')
i = 0
while True:
    line = f.readline()
    print(line)
    if not line:
        print("download done" + str(i))
        break
    path = line.split('\t')[0]
    times = line.split('\t')[-1]#time에 대한 list
    time = times.split(',')#['0', '58']
    time = list(map(int, time))
    try:
        sound = YouTube(path)
        print(sound.streams.filter(only_audio=True).all())
        for sound_infos in sound.streams.filter(only_audio=True).all():
            sound_infos_str = str(sound_infos)
            sound_info = sound_infos_str.split(' ')
            sound_type = sound_info[2]
            # webm을 wav 파일로 바꾸기 위해서는 mp4를 거쳐서 wav로 바꿈
            if sound_type.find('mp4') != -1:
                #download video file
                sound_infos.download(output_path=wav_path, filename=str(i).zfill(2))
                #convert mp4 to wav
                #ffmpeg -i D://pythonws//ML_data//no_problem_mp4//00.mp4 -ab 128k -ac 2 -ar 48000 D://pythonws//ML_data//no_problem_mp4//00.wav
                command = "ffmpeg -i " + wav_path + str(i).zfill(2) + ".mp4 -ab 128k -ac 2 -ar 48000 " + wav_path + str(i).zfill(2) + ".wav"
                print(command)
                subprocess.call(command, shell=True)
                #edit wav file
                wav = AudioSegment.from_wav(wav_path + str(i).zfill(2) + ".wav")
                number_of_execute = 1
                print(time)
                for sec in time:
                    print("print sec : " + str(sec))
                    if time.index(sec) % 2 == 0:
                        start = sec * 1000
                        print(start)
                    else:
                        finish = sec * 1000
                        if number_of_execute == 1:
                            cut_wav = wav[start:finish]
                            number_of_execute += 1
                        else:
                            cut_wav += wav[start:finish]
                #store wav file
                cut_wav.export(ml_path + "edit"+str(i).zfill(2)+".wav", format="wav", parameters=["-ab", "128k", "-ac", "2", "-ar", "48000"])
                print('download' + str(i).zfill(2) + "is finished")
                i += 1
                break
            else:
                i += 1
                print('fail')

    except Exception as ex:
        i += 1
        print(ex)
        print('download fail')

#sound.streams.filter(only_audio=True).all()[1].download()
#mime_type 확장자로 다운로드됨