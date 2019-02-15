# import time, datetime
# # t = time.time()
# # print(int(t))
# # print(t)
# i=0
# now = int(round(time.time()*1000))
# now_time = time.strftime('%Y-%m-%d[%H:%M:%S]',time.localtime(now/1000))
# print(now_time)
# # text_name = 'email{}.txt'.format(now_time)
# with open("text_name.txt",'a+') as file:
#     i=i+1
#
# # nums = range(2,20)
# # print(nums)
# # for i in nums:
# #     nums = filter(lambda x :x == i or x % i,nums)
# #     print(nums)
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import sleep
import win32api,win32gui,win32con
from ctypes import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains

#鼠标的移动
def moveCurPos(x, y):
    windll.user32.SetCursorPos(x, y)

#获得当前鼠标的位置
def getCurPos():
    return win32gui.GetCursorPos()

#鼠标左键按下或者放开
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

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
def run():
    GainEmailNumber=0
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    session.headers.clear()
    browser = webdriver.Chrome()
    a=getCurPos()
    GainEmails=int(input("请输入想要获取的邮箱个数："))
    Input_Login_name=input("请输入登陆的用户名：")
    Input_Login_password=input("请输入登陆的密码：")
    # browser.set_page_load_timeout(30)
    browser.get('https://www.facebook.com')
    LoginName =browser.find_element_by_id('email')
    LoginName.send_keys(Input_Login_name)
    LoginPassworld=browser.find_element_by_id('pass')
    LoginPassworld.send_keys(Input_Login_password)
    sleep(2)
    LoginPassworld.send_keys(Keys.ENTER)
    clickLeftCur()

    while(1):
        key_word =input("请输入搜索词")
        Common_page_url="https://www.facebook.com/search/pages/?q="+key_word
        i = 0
        browser.get(Common_page_url)
        # print(browser.get(Common_page_url))

        while i<=1000:
            i+=1
            scroll(browser)
            js = "var q =document.documentElement.scrollTop=10000"
            browser.execute_script(js)

        Search_User_Elements=browser.find_elements_by_class_name("_32mo")
        print("搜索到的用户的节点:", Search_User_Elements)

        Search_User_Element_list =[]
        for User_Element in Search_User_Elements:  # 遍历搜索出来的每一个用户
            User_Element_url=User_Element.get_attribute("href")  # 每一个用户详情页的超链接
            print("每一个用户详情页的超链接1:", User_Element_url)
            # 匹配确保用户的详情页超链接正确
            User_Element_url = re.match(r'(.*)/?ref=br_rs', User_Element_url)
            print("每一个用户详情页的超链接2:", User_Element_url.group(1))
            User_Element_url = User_Element_url.group(1)
            User_Element_url = list(User_Element_url)
            print("每一个用户详情页的超链接列表1:", User_Element_url)
            User_Element_url.remove('?')
            User_Element_url = "".join(str(m) for m in User_Element_url)  # 遍历每一个元素
            print("每一个用户详情页的超链接3:", User_Element_url)
            User_Element_url = User_Element_url + 'about/?ref=page_internal'
            print("每一个用户详情页的超链接4:", User_Element_url)  #
            Search_User_Element_list.append(User_Element_url)
            print("每一个用户详情页的超链接列表2：", Search_User_Element_list)
        time.sleep(3)

        # 遍历每一个用户的详情页
        for user_info_url in Search_User_Element_list:
            browser.get(user_info_url)
            try:
                Email_Elements=browser.find_elements_by_class_name("_50f4")
                print("找到所有用户邮箱的节点:",Email_Elements)
                for Email_Element in Email_Elements:
                    catch_emails=Email_Element.text
                    print("获取到的邮箱:", catch_emails)
                    for avail_catch_email in catch_emails:
                        if avail_catch_email=="@":
                            print("找到邮箱：",avail_catch_email)
                            with open("email_v1.txt","a+") as file:
                                file.writelines(avail_catch_email)
                                file.writelines('\n')
                                GainEmailNumber +=1
                            break
            except:
                pass
            if GainEmailNumber >= GainEmails:
               break
        sleep(2)
        if GainEmailNumber >= GainEmails:
            print("收集成功！")
            break

if __name__ == '__main__':
    run()