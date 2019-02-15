

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')



















# 导入webdriver
# from selenium import webdriver
# import time

# 2. 创建浏览器驱动对象
# 如果你驱动和当前Chrome版本不一致, 这里就会报错
# # driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="E:\CCS\爬虫\day05\code\chromedriver.exe")
# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
# # 访问百度网页, 必须写完整网页.
# driver.get('http://www.baidu.com')
#
# # # 根据ID找到输入框,然后填写内容
# # driver.find_element_by_id('kw').send_keys('python')
# #
# # # 点击搜索按钮
# # driver.find_element_by_id('su').click()
# #
# #
# # # 获取页面内容
# # # print(driver.page_source)
# # # 获取Cookie信息
# # print(driver.get_cookies())
# # # [{'domain': 'www.baidu.com', 'expiry': 1532488921, 'httpOnly': False, 'name': 'WWW_ST', 'path': '/', 'secure': False, 'value': '1532488911873'}, {'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '26936_1463_21089_26350_26920'}, {'domain': '.baidu.com', 'expiry': 3679972554.756276, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': 'CBDA46ADCC5D2F6253781884252CEE7E'}, {'domain': '.baidu.com', 'expiry': 3679972554.756332, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1532488907'}, {'domain': 'www.baidu.com', 'expiry': 1533352910, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '123253'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.baidu.com', 'expiry': 3679972554.756184, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'CBDA46ADCC5D2F6253781884252CEE7E:FG=1'}]
# #
# # # 这个cookie信息, 他内容多, 不能直接用, requests模块要的cookies的字典, 只要cookie名称和对应的值
# # cookies = {cookie['name']:cookie['value'] for cookie in driver.get_cookies()}
# # print(cookies)
# # # {'WWW_ST': '1532489100375', 'H_PS_PSSID': '26522_1455_21088_26350_26923_22160', 'BIDUPSID': '92DF65B387C8F2CFA15769B7F74B4FD2', 'PSTM': '1532489098', 'BD_UPN': '123253', 'BD_HOME': '0', 'BAIDUID': '92DF65B387C8F2CFA15769B7F74B4FD2:FG=1'}
# #
# #
# #
# # time.sleep(5)
# # # 关闭当前窗口
# driver.close()
# # 退出浏览器
# # driver.quit()

# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application'
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')