# Technical_Problem

## 1. Collecting data
### 1.1. using pytube library
pytube is a library in python. pytube offers user to download video or audio file in youtube which is the most popular video stream site in the world. Youtube changes video download query but pytube maker didn't update library so that you can see "url_encoded_fmt_stream_map" error message. 
To solve this problem
  #### 1. Find pytube library install folder
    In pycham File -> setting -> project -> project Interpreter -> put your mouse cursor on pytube then you can see path of pytube library
  #### 2. Find minxins.py
    
  #### 3. change code 
    fallow this [**instructions**](https://github.com/nficano/pytube/pull/534/commits/e5f1a9e2476b096ed2012939d50851d3499016e1)
  #### 4. restart pycharm
