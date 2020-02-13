# Technical Problems

## 1. Collecting data
### 1.1. using pytube library
Our project need broken car engine sounds. But it's hard to get the sound of a broken car engine even a car repair shop. So we found an alternative. Download sound file through youtube. pytube is a library in python. pytube offers user to download video or audio file in youtube which is the most popular video stream site in the world. But youtube changes video download query but pytube maker didn't update library so that you can see "url_encoded_fmt_stream_map" error message. 

To solve this problem
  #### 1. Find pytube library install folder
  In pycham File -> setting -> project -> project Interpreter -> put your mouse cursor on pytube then you can see path of pytube library
  
  #### 2. Find minxins.py
    
  #### 3. change code 
  Fallow this [**instructions**](https://github.com/nficano/pytube/pull/534/commits/e5f1a9e2476b096ed2012939d50851d3499016e1)
  
  #### 4. restart pycharm


### 1.2. convert mp4 format to wav
We decided collecting data through youtube. youtube offers mp4 format or mp3 format. But mp4 is video file and mp3 changes record file that only human can hear. We need raw and uncompressed record file. So that we choose wav foramt. It is the main format used on Microsoft Windows systems for raw and typically uncompressed audio. FFMPEG is free open source program that convert some audio file format to another format.

  #### 1. Download FFMPEG
  [**Download FFMPEG in windows**](http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/)
  
  #### 2. Decide audio file setting
  
  
