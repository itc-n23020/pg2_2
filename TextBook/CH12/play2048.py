from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Selenium で 2048を開く
browser = webdriver.Chrome()
browser.get('https://rugugu.jp/2048/')

html = browser.find_element(By.TAG_NAME, 'html')

print('停止するにはCTRL-Cを押してください。')

try:
    i = 1
    while True:
        #  上、右、上、右、上、右、上、右、上、左を繰り返す。
        if i % 2 == 1:
            html.send_keys(Keys.UP)
        elif i % 10 == 0:
            html.send_keys(Keys.LEFT)
        else:
            html.send_keys(Keys.RIGHT)
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print('終了')
