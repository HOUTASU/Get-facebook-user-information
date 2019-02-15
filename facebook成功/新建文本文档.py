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
# 引入模块
import threading


# class Facebook_Spider(object):
#鼠标左键按下或者放开
def clickLeftCur():
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#鼠标的移动
def moveCurPos(x, y):
    windll.user32.SetCursorPos(x, y)
#获得当前鼠标的位置
def getCurPos():
    return win32gui.GetCursorPos()
#搜索出来的内容往下滚动显示

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
# def run(arg):
def run():
    number=0  #判断获取的邮箱的数量
    # s = requests.Session()
    # s.headers.clear()  # 清除requests头部中的Python机器人信息，否则登录失败
    # 1. 获取session对象, 方法和使用与requests是一样的
    session = requests.session()
    # 2. 设置请求头, 设置该ession每次发送请求, 都会携带该请求头
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    session.headers.clear()
    # browser = webdriver.Chrome('D:\软件位置\chromedriver.exe')
    # browser = webdriver.Chrome('C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    browser = webdriver.Chrome()
    a=getCurPos()
    emails=input("输入搜索个数") # 方便控制获取的邮箱个数
    emails=int(emails)
    input_name_1=input("请输入用户名1")
    input_password_1=input("请输入密码1")

    # browser.set_page_load_timeout(30)  # 控制延时时间让输入完全执行
    browser.get('https://www.facebook.com')
    name_1 = browser.find_element_by_id('email')
    name_1.send_keys(input_name_1)
    passworld_1 = browser.find_element_by_id('pass')
    passworld_1.send_keys(input_password_1)
    sleep(2)
    passworld_1.send_keys(Keys.ENTER)  # 键盘输入enter
    clickLeftCur()

    # input_name_2=input("请输入用户名2")
    # input_password_2=input("请输入密码2")
    # browser.get('https://www.facebook.com')
    # name_2 = browser.find_element_by_id('email')
    # name_2.send_keys(input_name_2)
    # passworld_2 = browser.find_element_by_id('pass')
    # passworld_2.send_keys(input_password_2)
    # sleep(2)
    # passworld_2.send_keys(Keys.ENTER)  # 键盘输入enter
    # clickLeftCur()

    while(1):
        key_word = input("请输入搜索词")
        # "http": 'http://{}:{}@{}'.format('squid_user', 'Urun2017', '137.175.62.130:65432')
        # https://www.facebook.com/search/pages/?q=sun  公共主页
        html="https://www.facebook.com/search/pages/?q="+key_word
        i=0
        browser.get(html)   # 返回解析
        # print(browser.get(html))   # 内容

        # 找到多少个详情页面
        while i<=1000:
            i += 1
            # print("{}_{}".format(arg, i))
            # time.sleep(0.1)
            scroll(browser)
            # 怕有时候js代码执行无效做了个双重保险
            js = "var q=document.documentElement.scrollTop=10000"
            browser.execute_script(js)
        a=browser.find_elements_by_class_name("_32mo")  #？
        print("a:",a)
        # print(a.content.decode())

        html=[]
        #
        for x in a:
            # try:
            # print(x.get_attribute("href"))
            c=x.get_attribute('href')   # 每一个搜索出来的结果的链接
            print("c:",c) # https://www.facebook.com/Sun-188531505398605/?ref=br_rs
            # https://www.facebook.com/heraldsun/?ref=br_rs
            c=re.match(r'(.*)/?ref=br_rs',c)
            print("c.group(1):",c.group(1)) # https://www.facebook.com/Sun-188531505398605/?
            c=c.group(1)
            c=list(c)
            # ['h', 't', 't', 'p', 's', ':', '/', '/', 'w', 'w', 'w', '.', 'f', 'a', 'c', 'e', 'b', 'o', 'o', 'k', '.', 'c', 'o', 'm', '/', 'S', 'u', 'n', '-', '1', '8', '8', '5', '3', '1', '5', '0', '5', '3', '9', '8', '6', '0', '5', '/', '?']
            print("list(c):",c)
            c.remove('?') # https://www.facebook.com/Sun-188531505398605
            c="".join(str(m) for m in c)  #遍历每一个元素
            print("join:",c) # https://www.facebook.com/Sun-188531505398605/
            c=c+'about/?ref=page_internal'
            print("last c:",c) # https://www.facebook.com/Sun-188531505398605/about/?ref=page_internal
            html.append(c)
            print("详情页url列表：",html)
            # ['https://www.facebook.com/Sun-188531505398605/about/?ref=page_internal', 'https://www.facebook.com/Sun-363675764376150/about/?ref=page_internal', 'https://www.facebook.com/thesun/about/?ref=page_internal', 'https://www.facebook.com/Sun.BitterSwig/about/?ref=page_internal', 'https://www.facebook.com/Sunshine-262629954442370/about/?ref=page_internal', 'https://www.facebook.com/sungazing1/about/?ref=page_internal', 'https://www.facebook.com/sunpower/about/?ref=page_internal', 'https://www.facebook.com/SunMountainSports/about/?ref=page_internal', 'https://www.facebook.com/thedesertsun/about/?ref=page_internal', 'https://www.facebook.com/sunmaid/about/?ref=page_internal', 'https://www.facebook.com/CapriSun/about/?ref=page_internal', 'https://www.facebook.com/thecalgarysun/about/?ref=page_internal', 'https://www.facebook.com/SunDevilWrestling/about/?ref=page_internal', 'https://www.facebook.com/modsun/about/?ref=page_internal', 'https://www.facebook.com/midnightsunmov/about/?ref=page_internal', 'https://www.facebook.com/sunyanzi/about/?ref=page_internal', 'https://www.facebook.com/99.9SUNFM/about/?ref=page_internal']

        time.sleep(3)

        for x in html:
            browser.get(x)
            try:
                f=browser.find_elements_by_class_name("_50f4")
                print("f:",f)
                for x in f:
                    v=x.text  # 直接拿到邮箱
                    print("v:",v)
                    for n in v:
                        if n=='@':
                            print(v)
                            # now = int(round(time.time() * 1000))
                            # now_time = time.strftime('%Y-%m-%d[%H:%M:%S]', time.localtime(now/1000))
                            # text_name= 'email+{}.txt'.format(now_time)
                            # with open(text_name,'a+') as file:
                            with open('email.txt','a+') as file:
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
run()

# t1 = threading.Thread(target=run, args=('线程1', ))
# t1.start()

# t2 = threading.Thread(target=run, args=('线程2', ))
# t2.start()