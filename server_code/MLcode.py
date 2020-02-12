from fastai.vision import *
import numpy as np
import subprocess
from pydub import AudioSegment
import librosa
import librosa.display
import matplotlib.pyplot as plt

np.random.seed(42)

# class(label) setting
# class name must be sorted in alphabet ascend order
classes = ['bad_ball_joint', 'bad_brake_pad', 'engine_seizing_up', 'failing_water_pump',
           'hole_in_muffler', 'no_problem']

# machine learning data setting

time_slice = 3 

# audio setting

audio_sampling_rate = 44100  # sampling rate 44.1kHz
audio_bit_rate = 128000  # bit rate 128k
audio_channels = 1  # 1 is mono 2 is stereo, mono is default setting in android & IOS

# file path & name setting
wav_type = '.wav'
wav_path = '/app/MD_Web/app/upload/'
wav_name = ''  
img_type = '.png'
img_path = '/app/MD_Web/app/upload/' 
img_name = ''
mod_path = '/app/MD_Web/app/model/'

# server to client setting
top_rank = 3 
percent_decimal_point = 4 

# wav to mel spectrogram setting
img_size_x = 10
img_size_y = 4


def mapping_label(n):
    return classes[n]


def list_to_dic(label, prediction):
    return {label[i]: prediction[i] for i in range(0, len(label))}


def percentage(some_list):
    total_sum = sum(some_list)
    return [round((some_list[i] / total_sum) * 100, percent_decimal_point)
            for i in range(0, len(some_list))]


def sound_to_wav(name_tmp):
    global wav_name
    global img_name
    wav_name = name_tmp
    img_name = name_tmp
    command = "ffmpeg -y -i " + wav_path + wav_name + \
              " -ab " + str(audio_bit_rate) + \
              " -ac " + str(audio_channels) + \
              " -ar " + str(audio_sampling_rate) + \
              " " + wav_path + wav_name
    subprocess.call(command, shell=True)


def cut_wav_only3sec():
    wav = AudioSegment.from_wav(wav_path + wav_name)
    if len(wav) > time_slice * 1000:
        return wav[1000:1000+time_slice*1000]


def wav_to_mel():
    global img_name
    img_name = wav_name.split(".")[0]
    wav, sr = librosa.load(wav_path + wav_name)
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
    learn = load_learner(mod_path)
    img = open_image(img_path + img_name + img_type)
    predict_class, predict_idx, output = learn.predict(img)
    result = output.tolist()
    result = percentage(result)
    top_rank_index = np.flip(np.argsort(result)[-top_rank:])
    top_rank_value = [result[i] for i in top_rank_index]
    top_rank_names = list(map(mapping_label, top_rank_index))
    return list_to_dic(top_rank_names, top_rank_value)


if __name__ == "__main__":
    sound_to_wav(name)
    cut_wav_only3sec()
    wav_to_mel()
    print(predict())
