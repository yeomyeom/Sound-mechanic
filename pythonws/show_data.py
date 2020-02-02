import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

name_list = ["bad_ball_joint", "bad_brake_pad", "engine_seizing_up", "failing_water_pump", "hole_in_muffler",
             "no_problem"]
name = "no_problem"  # label name
data_path = "D://pythonws//ML_data//"
save_path = "D://pythonws//ML_data//data//"
ml_path = data_path + name + "//"
sa_path = save_path + name + "//"

img_sizex = 10
img_sizey = 4


def wav_to_melspec():
    file_list = os.listdir(ml_path)
    for file_name in file_list:
        try:
            file_type = file_name.split(".")[-1]
            file_title = file_name.split(".")[0]
            if file_type.find("wav") is not -1:
                path = ml_path + file_name
                wav, sr = librosa.load(path)
                wav_mel = librosa.feature.melspectrogram(y=wav, sr=sr)
                plt.figure(figsize=(img_sizex, img_sizey))
                librosa.display.specshow(librosa.power_to_db(wav_mel, ref=np.max),
                                         y_axis='mel', sr=sr, x_axis='time')
                # plt.colorbar(format='%+2.0f dB')
                plt.title('Mel-Spectrogram')
                plt.axis('off')
                plt.xticks([]), plt.yticks([])
                plt.tight_layout()
                plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
                plt.savefig(sa_path + file_title + ".png",
                            bbox_inces='tight',
                            pad_inches=0)
                print(str(file_name) + "is made")
                plt.close('all')
                # plt.show() # print
            else:
                print("not wav file")
                pass
        except Exception as e:
            print(str(e))
            pass


if __name__ == "__main__":
    wav_to_melspec()
