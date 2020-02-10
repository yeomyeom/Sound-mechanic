from fastai.vision import *
import numpy as np
import subprocess
from pydub import AudioSegment
import librosa
import librosa.display
import matplotlib.pyplot as plt
import threading

np.random.seed(42)

# thread setting
threads = []
exe_time = 0

# class(label) setting
# class name must be sorted in alphabet ascend order
classes = ['bad_ball_joint', 'bad_brake_pad', 'engine_seizing_up', 'failing_water_pump',
           'hole_in_muffler', 'no_problem']

# machine learning data setting
# 가능하면 바꾸지 말것!
time_slice = 3  # client 로부터 들어온 wav 파일을 3초 길이로 자름
time_interval = 1  # 이거는 팀원들이랑 이야기하고 정할꺼 semi 앙상블용으로 할 생각임

# audio setting
# 가능하면 바꾸지 말것!
audio_sampling_rate = 44100  # sampling rate 44.1kHz
audio_bit_rate = 128000  # bit rate 128k
audio_channels = 1  # 1 is mono 2 is stereo, mono is default setting in android & IOS

# file path & name setting
# wav_type = '.pcm'
wav_type = '.wav'
# wav_path = '/app/MD_Web/app/upload/'  # 스맛폰에서 보내온 녹음 파일 경로 (pcm->wav)
wav_path = 'D://pythonws//ML_data//data//no_problem//'
wav_name = 'local_test_00007'  # 스맛폰에서 보내온 녹음 파일 이름 (pcm->wav)
img_type = '.png'
# img_path = '/app/MD_Web/app/upload/'  # 녹음 파일을 mel spectrogram 으로 변환하여 저장할 경로
img_path = 'D://pythonws//ML_data//data//no_problem//'
img_name = ''  # 녹음 파일을 mel spectrogram 으로 변환하여 저장할 이름
mod_path = 'D://pythonws//ML_data//data//'  # 트레이닝 완료된 모델 경로

# server to client setting
top_rank = 3  # 예측한 것 중에서 상위 n 순위까지만 전송함
percent_decimal_point = 4  # 예측한 값 퍼센트 소수점 몇 자리까지 전송하는지

# wav to mel spectrogram setting
# 가능하면 바꾸지 말것!
img_size_x = 10
img_size_y = 4


def mapping_label(n):
    return classes[n]


def list_to_dic(label, prediction):
    # list 2개를 합쳐서 dictionary 형태로 만듬
    return {label[i]: prediction[i] for i in range(0, len(label))}


def normalization(some_list):
    maxi = max(some_list)
    mini = min(some_list)
    return [(some_list[i] - mini) / (maxi - mini) for i in range(0, len(some_list))]


def percentage(some_list):
    total_sum = sum(some_list)
    return [round((some_list[i] / total_sum) * 100, percent_decimal_point)
            for i in range(0, len(some_list))]


def pcm_to_wav(name_tmp):
    global wav_name
    global img_name
    wav_name = name_tmp
    img_name = name_tmp
    command = "ffmpeg -y -i " + wav_path + wav_name + wav_type + \
              " -ab " + str(audio_bit_rate) + \
              " -ac " + str(audio_channels) + \
              " -ar " + str(audio_sampling_rate) + \
              " " + wav_path + wav_name + ".wav"
    subprocess.call(command, shell=True)


def cut_wav_only3sec():
    wav = AudioSegment.from_wav(wav_path + wav_name + ".wav")
    if len(wav) > time_slice * 1000:
        return wav[1000:4000]


def cut_wav_multi():
    wav = AudioSegment.from_wav(wav_path + wav_name + ".wav")
    total_wav_long = len(wav) // 1000
    global exe_time
    exe_time = total_wav_long - time_slice + 1
    slice_start = 0
    for i in range(0, exe_time):
        slice_finish = slice_start + time_slice
        try:
            edit_wav = wav[slice_start * 1000:slice_finish * 1000]
            edit_wav.export(wav_path + wav_name + str(i) + ".wav", format="wav",
                            parameters=["-ab", str(audio_bit_rate),
                                        "-ac", str(audio_channels),
                                        "-ar", str(audio_sampling_rate)])
        except IndexError:
            print("client sent wav file less then 5 seconds")
            pass
        slice_start += time_interval


def wav_to_mel():
    global img_name
    img_name = wav_name
    wav, sr = librosa.load(wav_path + wav_name + wav_type)
    mel_spec = librosa.feature.melspectrogram(y=wav, sr=sr)
    plt.figure(figsize=(img_size_x, img_size_y))
    librosa.display.specshow(librosa.power_to_db(mel_spec, ref=np.max), sr=sr)
    plt.axis('off')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
    plt.savefig(img_path + img_name + img_type, bbox_inces='tight', pad_inches=0)
    plt.close('all')


def predict():
    defaults.device = torch.device('cpu')
    # label_test = "no_problem"
    # path_test = "D://pythonws//ML_data//data//"
    learn = load_learner(mod_path)
    # img_path = 서버에서는 검사할 이미지 경로가 이쪽으로 들어간다.
    img = open_image(img_path + '//' + img_name + img_type)
    # img_path_test = path_test + label_test + "//edit00037.png"
    # img = open_image(img_path_test)
    predict_class, predict_idx, output = learn.predict(img)
    result = output.tolist()
    # result = normalization(result)
    result = percentage(result)
    top_rank_index = np.flip(np.argsort(result)[-top_rank:])
    top_rank_value = [result[i] for i in top_rank_index]
    top_rank_names = list(map(mapping_label, top_rank_index))
    print("predict_class list : " + str(predict_class))
    print("top_rank_names : " + top_rank_names[0])
    return list_to_dic(top_rank_names, top_rank_value)


def predict_thread(thread_name):
    defaults.device = torch.device('cpu')
    path_test = "D://pythonws//ML_data//data//"
    learn = load_learner(path_test)
    img = open_image(img_path + thread_name + img_type)
    predict_class, predict_idx, output = learn.predict(img)
    result = output.tolist()
    # result = normalization(result)
    result = percentage(result)
    top_rank_index = np.flip(np.argsort(result)[-top_rank:])
    top_rank_value = [result[i] for i in top_rank_index]
    top_rank_names = list(map(mapping_label, top_rank_index))
    print("predict_class list : " + str(predict_class))
    print("top_rank_names : " + top_rank_names[0])
    return list_to_dic(top_rank_names, top_rank_value)


class predict_thread(threading.Thread):
    def __init__(self, threadID, path):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.path = path

    def run(self):
        return predict_thread(self.path)


def predict_thread_run():
    for i in range(0, exe_time):
        threads.append(predict_thread(i, img_path + img_name + str(i) + img_type))
    for i in range(0, exe_time):
        threads[i].start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    # pcm_to_wav(wav_name)
    cut_wav_only3sec()
    wav_to_mel()
    print(predict())
    # predict()
    # 숑숑숑 뿅뿅뿅
    # pcm_to_wav()
    # cut_wav_multi()
    # predict_thread_run()

