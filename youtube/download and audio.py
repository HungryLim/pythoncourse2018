from pytube import YouTube
from bs4 import BeautifulSoup as bs
import requests
import os
import random
import csv
from itertools import chain
import pandas
import pytube
import time

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")

#import candidate names
import pandas
colnames = ['title', 'keywords', 'url', 'Chosen']
data = pandas.read_csv('winner_sample_sample.csv', names=colnames)
l=data["url"].tolist()
l.pop(0)
item=l[1]



for item in l:
    yt = YouTube(item)
    stream = yt.streams.first()
    stream.download("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube/video")
    time.sleep(5)


#import subprocess

#command = "ffmpeg -i C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube/Kennedy-Clinton Dinner New Hampshire  John K Delaney.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

#subprocess.call(command, shell=True)

import moviepy.editor as mp
import os
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube/video")
clip = mp.VideoFileClip("Kennedy-Clinton Dinner New Hampshire  John K Delaney.mp4").subclip(0,20)
clip.audio.write_audiofile("theaudio.mp3")