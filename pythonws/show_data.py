import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

name = "bad_ball_joint"
data_number = "00"
data_path = "D://pythonws//ML_data//"
ml_path = data_path + name + "//"
path = ml_path + data_number + ".wav"


def wav_to_melspec():
    print(path)
    wav, sr = librosa.load(path)
    wav_mel = librosa.feature.melspectrogram(y=wav, sr=sr)
    '''
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(wav_mel, y_axis='mel')
    plt.title(path)
    plt.show() #power_to_db를 안했을 때는 데이터에 frequency(y축)가 들쭉날쭉함
    '''
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(wav_mel, ref=np.max), y_axis='mel', sr=sr, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-Spectrogram')
    #plt.tight_layout()
    plt.savefig(ml_path + data_number + ".png")
    #plt.show()


if __name__ == "__main__":
    wav_to_melspec()