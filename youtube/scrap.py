#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import build
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import youtube

import os

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")


import csv
with open("names.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]



    

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyBYl6LkkHOIfBCSzRpMcptBiEArCDKwq7g'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
  q="obama",
  part='id,snippet',
  maxResults=2).execute()

name=["obama"]
search_response = youtube.search().list(
  q=data[0][0],
  part='id,snippet',
  maxResults=2).execute()

