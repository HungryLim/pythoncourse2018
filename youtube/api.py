import argparse
import build
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import youtube
import csv
import os
import re
import random
from itertools import chain

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")

#import candidate names
with open("names.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]

data=list(chain(*data)) #unlist
data = [item.lower() for item in data] #make all lower case
data = [item.strip() for item in data]
sample = random.sample(data,10) 

DEVELOPER_KEY = 'AIzaSyBYl6LkkHOIfBCSzRpMcptBiEArCDKwq7g'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)


out=[]
for i in range(len(sample)):
    search_response = youtube.search().list(
        q=sample[i],
        part='id',
        maxResults=2).execute()
    search_response
    search_response["search_key"]=sample[i]
    out.append(search_response)
print out[0].keys()
out[0].keys()


out[0]['items'][0]
out[9]['items'][0]['id']['videoId']

ids=[]
keywords=[]
for i in range(len(out)):
    for j in range(len(out[i]['items'])):
        id = out[i]['items'][j]['id']['videoId'].encode("utf-8")
        keyword = out[i]["search_key"]
        print i
        print j
        ids.append(id)
        keywords.append(keyword)
