# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 17:14
# @Author  : KXT
from selenium import webdriver
from scrapy.selector import Selector
from scrapy import Request
import time
import re
import xlrd
from xlutils.copy import copy
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
user_id = []
url = "https://www.facebook.com/"
#url='https://www.facebook.com/ChinaGlobalTVNetwork/?hc_ref=ARTyWF-9Z77AHB-6xQFKNLOoJU3z_O5CfmaP5REUESVYvAa6yymHNBBGKYkQ9XelqxE&fref=nf'
browser = webdriver.Chrome()
# browser = webdriver.Chrome(
#     executable_path="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")  # 获取chrome的driver路径
browser.get(url)  # 浏览器打开页面
# browser.find_element_by_css_selector("#email").send_keys("")
# browser.find_element_by_css_selector("#pass").send_keys("")
browser.find_element_by_css_selector("#email").send_keys("MihalinaKonstantinova9818@mail.ru")
passworld=browser.find_element_by_css_selector("#pass").send_keys("bkwgkk")

# passworld.send_keys(Keys.ENTER)  # 键盘输入enter
# clickLeftCur()

serachmodel3='<input value="登录" tabindex="4" data-testid="royal_login_button" type="submit" id="(.*?)" /></label></td></tr><tr><td class="login_form_label_field'
c=re.findall(serachmodel3,browser.page_source)
# print(c[0])
try:
   browser.find_element_by_css_selector('#'+c[0]).click()
except:
    pass

# serachmodel1='<div class="_585-" aria-label="Facebook" role="search" data-testid="facebar_root" id="([\s\S]*?)"><form action="/search/web/direct_search.php"'
# b=re.findall(serachmodel1,browser.page_source)
# print(b[0])
# browser.find_element_by_css_selector('#'+b[0]+' > input._1frb').send_keys("belt and road")
#
# serachmodel2='<div class="_585-" aria-label="Facebook" role="search" data-testid="facebar_root" id="([\s\S]*?)"><form action='
# a=re.findall(serachmodel2,browser.page_source)
# print(a[0])
# browser.find_element_by_css_selector('#'+a[0]+' > form > button > i').click()

# time.sleep(12*60)
#
#


# time_move = 1
# while time_move<600:
#     browser.execute_script("window.scrollBy(0,5000)")
#     time.sleep(1)
#     time_move += 1



a=browser.page_source
# try:
#     txt = 'D:\\result.html'
#     f = open(txt, "w+",encoding = 'utf-8')
#     f.write(a)
# except:
#     pass
model = 'rank&quot([\s\S]*?)寄送這個給朋友或張貼在你的動態時報中'#所有页面
text_list = re.findall(model,a)#初步提

def try_get_info(model,text):
    result = "error"
    try:
        result = re.findall(model,text)[0]
    except:
        pass
    return result

error=0

for p in text_list:
    shipinshu= 0
    tupianshu = 0
    name_model='https://www.facebook.com/([\s\S]*?)/?hc_ref'
    prise_model_chu='<span class="_4arz"><span data-hover="tooltip"(.*?)</span></span>'
    liuyan_model='>([0-9]*?)則留言</a>'
    fenxiang_model='>([0-9]*?)則分享</a>'
    text_model_chu='<div class="_5pbx userContent _3576" data-ft="{&quot;tn&quot;:&quot;K&quot;}">(.*?)</div></div></div>'
    person_page_url_model='<a href="(.*?)" data-hovercard'

    prise_chu=try_get_info(prise_model_chu,p)
    liuyan = try_get_info(liuyan_model, p)
    if liuyan=='error':
        liuyan=0
    fenxiang = try_get_info(fenxiang_model, p)
    if fenxiang=='error':
        fenxiang=0
    text_chu = try_get_info(text_model_chu, p)
    person_page_url = try_get_info(person_page_url_model, p)
    name = try_get_info(name_model, person_page_url)[:-2]

    prise_model='>([\s\S]*)'
    if prise_chu=='error':
        prise=0
    else:
        prise=re.findall(prise_model,prise_chu)

    if text_chu=='erroe':
        text='none'
    else:
        text = re.sub(r'</?\w+[^>]*>', '', text_chu)

    for i in re.findall('取消靜音',p):
        shipinshu=shipinshu+1
    for i in re.findall('圖像裡',p):
        tupianshu=tupianshu+1

    try:
        tupianshu=tupianshu+int(re.findall('還有 [0-9] 張',p)[0][2:-1])-1
    except:
        pass

    time=try_get_info('<abbr title="([\s\S]*?)" data-utime', p)



    # import requests
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    # text = requests.get(person_page_url[0], headers=headers)
    #
    # # url = "https://www.facebook.com/"
    # # url='https://www.facebook.com/ChinaGlobalTVNetwork/?hc_ref=ARTyWF-9Z77AHB-6xQFKNLOoJU3z_O5CfmaP5REUESVYvAa6yymHNBBGKYkQ9XelqxE&fref=nf'
    # from selenium import webdriver
    #
    # browser = webdriver.Chrome(
    #     executable_path="D:/chromedriver_win32/chromedriver.exe")  # 获取chrome的driver路径
    # browser.get(person_page_url[0])  # 浏览器打开页面
    # name = browser.find_element_by_css_selector('#seo_h1_tag > a').text
    # hhh = browser.page_source
    #
    # zhiye_model_chu = '="_4-u2 _3-96 _4-u8([\s\S]*?)</div></div></div></div></div>'
    # import re
    #
    # try:
    #     zhiye_place = re.findall(zhiye_model_chu, hhh)
    # except:
    #     zhiye_place = "unknown zhiye,didian"
    #
    # print("ok!")


    try:
        book = xlrd.open_workbook("face.xlsx")
        booknew = copy(book)
        sh = book.sheet_by_name('Sheet1')
        shnew = booknew.get_sheet(0)
        rows = sh.nrows
        shnew.write(rows,0,name)#用户名
        shnew.write(rows, 1, prise)#点赞数
        shnew.write(rows, 2, liuyan)#留言数
        shnew.write(rows, 3, fenxiang)#分享数
        shnew.write(rows, 4, text)#文章内容
        shnew.write(rows, 5, person_page_url)#个人主页
        shnew.write(rows, 6,shipinshu)  # 视频数
        shnew.write(rows, 7, tupianshu)  # 图片数
        shnew.write(rows, 8, time)  # 发帖时间


        booknew.save("face.xlsx")
        print("第{0}行完成".format(rows))
    except:
        error=error+1
        pass

print(error)


browser.close()



