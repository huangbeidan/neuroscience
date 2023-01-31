import re
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv

HTMLFile = open(
    "C:/Users/Andric Li/Documents/Github/scrapy_tutorial_dse203/scrapy_tutorial_dse203/quotes-as-a-new-study-spotlights-a-growing-role-for-lrrk2-in-parkinsons-denali-clears-an-early-trial-hurdle.html",
    "r")
index = HTMLFile.read()

S = BeautifulSoup(index, 'lxml')

for para in S.find_all("p"):
    goodText = para.get_text().replace("\xad", "")
    goodText = re.sub(r'[$][0-9]+', '', goodText)
    arr = goodText.split()
    #print(goodText.split())
    for i in arr:
        if i[0] == "$":
            print(i)
# extract list of companies on website
# https://www.drugs.com/pharmaceutical-companies.html