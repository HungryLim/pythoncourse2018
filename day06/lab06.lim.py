import re
import os

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/day06")

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	text = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

key=re.compile(r"\b[Tt]he\b")
key=re.compile(r"\bThe|the\b")

keyword = re.compile(r"\sthe\s")
keyword2 = re.compile(r"The\w+")
l=[]
for line in (text):
    if keyword.search(line) or keyword2.search(line):
       the = line
    else:
        nothe = line
        print nothe
        l.append(nothe)

len(l)

# TODO: print lines that contain a word of any length starting with s and ending with e
text2= [x.lower() for x in text]
key= re.compile(r"\bs[a-z]*e\b")

find=[]
for line in text2:
    if key.search(line):
        find.append(line)

find
len(find)



## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY: ")
Month = re.compile(r"\d{1,2}/\d{1,2}")
Day = re.compile(r"\d{1,2}/\d{1,2}")
Year  = re.compile(r"\d{1,2}/\d{1,2}")

date =raw_input("Please enter a date in the format MM.DD.YY: ")