import re
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s=Service('Chromedriver PATH')
driver = webdriver.Chrome(service=s)


driver.get("https://endpts.com/")
sleep(0.5)

"""
<div class="epn_search_bar">
        <form action="https://endpts.com/">
            <input type="text" name="s" placeholder="Search">
            <button class="epn_ux_button epn_white epn_search_submit_button"></button>
        </form>
        <button class="epn_ux_button epn_white epn_search_button"></button>
    </div>
"""
search_bar = driver.find_element(By.CLASS_NAME, 'epn_search_bar')
search_bar.click()

search_box = driver.find_element(By.NAME, 's')
search_box.send_keys('PINK1')
sleep(0.5)
search_box.send_keys(Keys.RETURN)
sleep(0.5)

"""
<div class="epn_search_bar epn_active">
        <form action="https://endpts.com/">
            <input type="text" name="s" placeholder="Search">
            <button class="epn_ux_button epn_white epn_search_submit_button"></button>
        </form>
        <button class="epn_ux_button epn_white epn_search_button"></button>
    </div>
"""
#open file to record search result
file_result = open("assignment_result.txt", "w")


search_result = driver.find_element(By.CLASS_NAME, 'epn_result_list')
# h3_elem = search_result.find_elements(By.TAG_NAME, "h3")

for i in search_result.find_elements(By.TAG_NAME,'h3'):
    article_link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
    article_title = i.find_element(By.TAG_NAME, 'a').get_attribute('title')

    article = article_title + ": " + article_link + "\n"

    file_result.write(article)

# check next page
"""
<div class="epn_ux_pagination">
    
    <span class="epn_navigation epn_navigation_number epn_navigation_active">1</span><a a="" href="https://endpts.com/page/2/?s=LRRK2" title="Page #2" class="epn_navigation epn_navigation_number">2</a>
    <a href="https://endpts.com/page/2/?s=LRRK2" title="Next page" class="epn_navigation epn_navigation_next">Next page</a>
<a href="https://endpts.com/page/2/?s=LRRK2" title="Last page" class="epn_navigation epn_navigation_last">Last page</a>
</div>
"""
page_checker = driver.find_elements(By.CLASS_NAME, 'epn_ux_pagination')
if(len(page_checker)> 0):
    #list out all options of naviagting pages
    page_option = page_checker[0].find_elements(By.TAG_NAME, 'a')
    #choose to go to next page
    for p in page_option:
        if(p.get_attribute('title') == "Next page"):
            p.click()
            break

    #search result on next page
    search_result = driver.find_element(By.CLASS_NAME, 'epn_result_list')
    # h3_elem = search_result.find_elements(By.TAG_NAME, "h3")
    for i in search_result.find_elements(By.TAG_NAME,'h3'):
        article_link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        article_title = i.find_element(By.TAG_NAME, 'a').get_attribute('title')

        article = article_title + ": " + article_link + "\n"

        file_result.write(article)
            

else:
    driver.quit()

file_result.close()
