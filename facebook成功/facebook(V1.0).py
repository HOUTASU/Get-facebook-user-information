from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
import multiprocessing
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import win32api,win32gui,win32con
from ctypes import *
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains

# class Facebook_Spider(object):
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#鼠标的移动
def moveCurPos(x, y):
    windll.user32.SetCursorPos(x, y)
#获得当前鼠标的位置
def getCurPos():
    return win32gui.GetCursorPos()
def scroll(driver):
    driver.execute_script("""   
        (function () {   
            var y = document.body.scrollTop;   
            var step = 100;   
            window.scroll(0, y);   


            function f() {   
                if (y < document.body.scrollHeight) {   
                    y += step;   
                    window.scroll(0, y);   
                    setTimeout(f, 50);   
                }  
                else {   
                    window.scroll(0, y);   
                    document.title += "scroll-done";   
                }   
            }   


            setTimeout(f, 1000);   
        })();   
        """)
def net():
    number=0
    s = requests.Session()
    s.headers.clear()  # 清除requests头部中的Python机器人信息，否则登录失败
    # browser = webdriver.Chrome('D:\软件位置\chromedriver.exe')
    # browser = webdriver.Chrome('C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    browser = webdriver.Chrome()
    a=getCurPos()
    emails=input("输入搜索个数")
    emails=int(emails)
    input_name=input("请输入用户名")
    input_password=input("请输入密码")
    # browser.set_page_load_timeout(30)
    browser.get('https://www.facebook.com')
    name = browser.find_element_by_id('email')
    name.send_keys(input_name)
    passworld = browser.find_element_by_id('pass')
    passworld.send_keys(input_password)
    sleep(2)
    passworld.send_keys(Keys.ENTER)
    clickLeftCur()

    while(1):
        key_word = input("请输入搜索词")
        html="https://www.facebook.com/search/pages/?q="+key_word
        i=0
        browser.get(html)
        while i<=1000:
            i += 1
            scroll(browser)
            js = "var q=document.documentElement.scrollTop=10000"
            browser.execute_script(js)
        a=browser.find_elements_by_class_name("_32mo")
        # print(a)
        html=[]
        for x in a:
            # try:
            # print(x.get_attribute("href"))
            c=x.get_attribute('href')
            # print(c)
            c=re.match(r'(.*)/?ref=br_rs',c)
            # print(c.group(1))
            c=c.group(1)
            c=list(c)
            c.remove('?')
            c="".join(str(m) for m in c)
            c=c+'about/?ref=page_internal'
            print(c)
            html.append(c)
        time.sleep(3)
        for x in html:
            browser.get(x)
            try:
                f=browser.find_elements_by_class_name("_50f4")
                for x in f:
                    v=x.text
                    for n in v:
                        if n=='@':
                            print(v)
                            with open('email.txt','a+') as  file:
                                file.writelines(v)
                                file.writelines('\n')
                                number += 1
                            break
            except:
                pass
            if number >= emails:
                break
        sleep(2)
        if number >= emails:
            print("收集成功！")
            break
# if __name__ == '__main__':
#     faceboospoder = Facebook_Spider()
#     faceboospoder.net()
net()