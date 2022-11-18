import time, telebot, shutil, os, asyncio
from selenium import webdriver
from bs4 import BeautifulSoup
from cfg import TOKEN
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


async def main():
  browser = webdriver.Chrome("chromedriver.exe") #Подключение веб драйвера
  browser.get('http://192.168.20.21/') #IP сервера atlasCopco
  #browser.get('https://pythonru.com/baza-znanij/razdelit-stroku-split')
  while True:
    time.sleep(30)

    soup = BeautifulSoup(browser.page_source) #Загрузка страницы в BS
    print (soup)
    if 'ESUNIT' in soup:
      ESUNIT = soup.find("div", {"id": "ESUNIT"}) #Поиск давления
      bar =''.join(ESUNIT.split('>')[1]) #Обрезка строки до значения давления
      pressure = ''.join(bar.split()[:1]) #Обрезка после значения
      print(pressure)
      return pressure      
      
    else:
      print('Ошибка "Нет данных по давлению"')
      await asyncio.sleep(10) #Задержка в 3 минуты

async def bot(pressure):
  message = pressure
  bot = telebot.TeleBot(TOKEN)
  bot.send_message(message.from_user.id,'загружаю файл с отчетом...')
  
  #def send_welcome(message):
    #bot.reply_to(message, f'Привет, '+ message.from_user.first_name + '!')

  bot.polling(none_stop=True)
  await asyncio.sleep(1)


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()