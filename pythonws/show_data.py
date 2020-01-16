import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

name_list = ["bad_ball_joint", "bad_brake_pad", "engine_seizing_up", "failing_water_pump", "hole_in_muffler", "no_problem"]
name = "engine_seizing_up"  # label name
data_path = "D://pythonws//ML_data//"
ml_path = data_path + name + "//"

def wav_to_melspec():
    i = 0
    for exe_num in range(0, 100):
        try:
            data_number = str(i).zfill(2)
            path = ml_path + "edit" + data_number + ".wav"
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
            i += 1
        except FileNotFoundError:
            print("done")
            break
        except Exception as error:
            print("Error : " + error)
            break


if __name__ == "__main__":
    wav_to_melspec()