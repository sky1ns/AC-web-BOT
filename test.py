import time, telebot, shutil, os, asyncio
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options) #Подключение веб драйвера
browser.delete_all_cookies()
browser.get('http://192.168.20.21/') #IP сервера atlasCopco

time.sleep(30)

with open("page_source.html", "w",encoding='utf-8') as f:
 f.write(browser.page_source)
 html =  open('page_source.html','r')

soup = BeautifulSoup(browser.page_source, 'lxml')#.decode('utf-8') #Загрузка страницы в BS

print (soup)
time.sleep(3)

if 'ESUNIT' in html:
    ESUNIT = soup.find("div", {"id": "ESUNIT"}) #Поиск давления
    bar =''.join(ESUNIT.split('>')[1]) #Обрезка строки до значения давления
    pressure = ''.join(bar.split()[:1]) #Обрезка после значения
    print(pressure)
else: print('error')

'''
soup = '<div id="ESUNIT" style="position:relative;top:5px;font-size:14px">7.766 Bar</div>'
if 'ESUNIT' in soup:
    ESUNIT = soup
    bar =''.join(ESUNIT.split('>')[1])
    pressure = ''.join(bar.split()[:1])
    print(pressure)'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service '''