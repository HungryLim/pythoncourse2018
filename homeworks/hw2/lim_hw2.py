from bs4 import BeautifulSoup
import urllib2
import csv 
import random
import time
import os

## setting working directory ------------------------------------------------
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/homeworks/hw2")

with open('hw2_lim.csv', 'wb') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues", "Number of signatures"))
	w.writeheader()
    
    still_petitions = True
    i=0
    while still_petitions:
        web_address='https://petitions.whitehouse.gov/?page=%i' %i
        i += 1
        web_page = urllib2.urlopen(web_address)
        all_html = BeautifulSoup(web_page.read())
        try:
            page= all_html.find('div', {'class':"page-load-next"})
        except AttributeError:
            still_petitions = False

        #if page == "Load More":

            all_petition = all_html.find_all("h3")
            for p in all_petition :
                petition = {} ## empty dictionary to fill in
		        petition["Title"] = p.get_text()
           # getting in each webpage
           #page = p.find_previous("h3")
            address = p.find('a')
            extension=address["href"]

        #date
        pet_page = urllib2.urlopen('https://petitions.whitehouse.gov%s' % extension)
        petition_html = BeautifulSoup(pet_page.read())
	    fordate= petition_html.find('h4', {'class': "petition-attribution"})
        pre= fordate.text.strip()
        petition["Published date"] =pre.split("on")[1]

        #issue
        #pet_page = urllib2.urlopen('https://petitions.whitehouse.gov%s' % extension)
        #petition_html = BeautifulSoup(pet_page.read())
        issue= petition_html.find('div', {'class': "field-item even"})
        petition["Issues"] =issue.text.strip()

        #Number of signatures
        pet_page = urllib2.urlopen('https://petitions.whitehouse.gov%s' % extension)
        petition_html = BeautifulSoup(pet_page.read())
	    num_sig= petition_html.find("span", {'class':"signatures-number"})
        petition["Number of signatures"] =num_sig.text.strip()

        ## write observation to csv
        w.writerow(prof)
        
        else:
            break