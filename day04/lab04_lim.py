## Go to https://polisci.wustl.edu/faculty/specialization
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv 

web_address = 'https://polisci.wustl.edu/faculty/specialization'
download_page('https://polisci.wustl.edu/faculty/specialization', "polisci_ppl.html")

with open('polisci_ppl.html') as f:
  myfile = f.read()
  
soup = BeautifulSoup(myfile)
soup.prettify()

soup.find_all('a')
all_a_tags = soup.find_all('a')


all_a_tags[22]
all_a_tags[22].attrs ## a dictionary with the attributes
all_a_tags[22].attrs['href']

all_a_tags[22].attrs.keys()
all_a_tags[22]['href']
all_a_tags[22]['class']

l=[]
for i in range(14, len(all_a_tags)):
    all_a_tags[i].attrs
    all_a_tags[i].attrs.keys()
    all_a_tags[i]['href']
    #urls=("https://polisci.wustl.edu/"%all_a_tags[i]['href']) 
    #l.append(urls)
    l.append(all_a_tags[i]['href'])

fields = soup.find_all('h3') ## list of html entries
[i.text for i in fields]

def make_address(value):
    add="https://polisci.wustl.edu%s" %value
    return add

url=[]

for i in range(1,len(l)):
    a=make_address(l[i])
    url.append(a)

#addresses
url

def check_pages(address, filename, wait = 3):
	time.sleep(random.uniform(0,wait))
	page = urllib2.urlopen(address)
	page_content = page.read()

	if os.path.exists(filename) == False:
		with open(filename, 'w') as p_html:
			p_html.write(page_content)
	else:
		print "Can't overwrite file" + filename

check_pages('https://polisci.wustl.edu/faculty/specialization', "polisci_ppl.html")

for i in range(1,len(url)):
    page = urllib2.urlopen(url[1])
    soup = BeautifulSoup(page.read())
    soup.prettify()
    all_h1_tags = soup.find_all('h1')
    name=all_h1_tags[1].text

    all_div_tags= soup.find_all('div', {'class':"field field-name-field-person-email field-type-email field-label-inline clearfix"})
    email= all_div_tags[0].text

    all_div_tags2= soup.find_all('div',{ 'class':"field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
    webpage=all_div_tags2[0].text










