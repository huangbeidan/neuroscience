import re
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

def extracter(link):
    index = urlopen(link)
    S = BeautifulSoup(index, 'lxml')

    counter = 0
    sentences = S.find_all('p')
    for sentence in sentences:
        sentenceToString = sentence.get_text()
        sentenceToString = sentenceToString.replace("\xad", "")
        sentenceToString = sentenceToString.replace("-", "")
        res = re.findall(r"([^.]*?Parkinson[^.]*\.)", sentenceToString)
        if len(res) > 0:
            # data cleaning here
            #print(res)
            counter += len(res)


    title = S.title.get_text().replace("â€™", "\'")
    print(title)
    date = S.find_all(class_='epn_time')[0].get_text()
    print(date)
    url = S.find("link",{"rel":"canonical"})['href']
    print(url)
    print(counter)

    with open('indicator.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'title': title, 'date': date, 'link': url, '# of occurence': counter})

#HTMLFile = "https://endpts.com/as-a-new-study-spotlights-a-growing-role-for-lrrk2-in-parkinsons-denali-clears-an-early-trial-hurdle/"

with open('indicator.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'date', 'link', '# of indications']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

HTMLFile = "https://endpts.com/page/1/?s=Parkinson%E2%80%99s"

print(HTMLFile)

bindex = urlopen(HTMLFile)

soup = BeautifulSoup(bindex, 'lxml')


while(soup):
    try:
        nexturl = soup.find('a',attrs={'class':'epn_navigation epn_navigation_next'})['href']
    except:
        nexturl = "no"
    #nexturl.replace("’", "%E2%80%99")
    nexturl = nexturl[:-2]
    nexturl += "%E2%80%99s"
    print(nexturl)
    counta = 0
    data = soup.findAll('div',attrs={'class':'epn_white_box epn_item'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            if('channel' in a['href']):
                continue
            extracter(a['href'])
            counta += 1
    print(counta)
    if(nexturl == "%E2%80%99s"):
        break
    cindex = urlopen(nexturl)
    soup = BeautifulSoup(cindex, 'lxml')