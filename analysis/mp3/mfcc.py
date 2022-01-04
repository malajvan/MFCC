from python_speech_features import mfcc
import sys,os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
from unidecode import unidecode


df=pd.read_csv('/Volumes/Samsung_T5/Vietnamese (V-Pop) 2021/csv/Vietnamese (V-Pop) 2021.csv')
tracks=os.listdir(r"/Volumes/Samsung_T5/Vietnamese (V-Pop) 2021/mp3")
dog='/Users/vanpham/Desktop/Dog-barking-sound.mp3'
def extract_features(file_name):
    data, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T,axis=0)


    return mfccs_processed
df['file']=(df['song'].str.lower()+'.mp3')
df['file']=df['file'].apply(unidecode)
df['song']=df['song'].apply(unidecode)
l=[]
for i in tracks:
    l.append(unidecode(i))
tracks=l

feats=[]
for i,r in df.iterrows():
    try:
        coef=extract_features("/Volumes/Samsung_T5/Vietnamese (V-Pop) 2021/mp3/"+r['file'])
    except FileNotFoundError:
        coef='NaN'
    feats.append([r['song'],r['popularity'],coef])

df2=pd.DataFrame(feats,columns=['song','popularity','coef'])
df2.to_json('coeficients.json',indent=4)
