from bs4 import BeautifulSoup as bs
import requests
import os
import random
import csv
from itertools import chain

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")

#import candidate names
with open("names.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]

data=list(chain(*data)) #unlist
data = [item.lower() for item in data] 
data = [item.strip() for item in data]
data = [item.replace(" ", "+") for item in data]

sample = random.sample(data,10) 
sample

videolist=[]
keywords=[]
titles=[]

for i in range(len(sample)):
    base = "https://www.youtube.com/results?search_query="
    qstring = sample[i]
    r = requests.get(base+qstring)
    page = r.text
    soup=bs(page,'html.parser')
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    for v in vids:
        tmp = ('https://www.youtube.com' + v['href']).encode('utf-8').strip()
        title= v['title'].encode("utf-8")
        videolist.append(tmp)
        keywords.append(qstring)
        titles.append(title)

results = zip(titles, keywords,videolist)



with open('results.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['title','keywords','url'])
    for row in results:
        try:
            csv_out.writerow(row)
        except UnicodeEncodeError:
            results = False