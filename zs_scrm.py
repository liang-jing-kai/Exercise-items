from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

option = Options()  # 实例化option对象
option.add_argument("--headless")  # 给option对象添加无头参数

import xlwings as xw

app = xw.App(visible=False, add_book=False)
wb = app.books.open('excel/zs.xlsx') # 打开Excel文件
sheet = wb.sheets[0]  # 选择第0个表单，也可以使用wb.sheets['sheet1']指定sheet的名字
# 将A1到A2的值，读取到a列表中
user_list = sheet.range('B2:B7').value
passwd_list = sheet.range('C2:C7').value

# 时间模块
# 获取昨天时间
from datetime import timedelta, datetime
yesterday = datetime.today()+timedelta(-1)
yesterday_format = yesterday.strftime('%Y-%m-%d')
# print('昨天是：%s' %yesterday_format)
# yesterday_format = input("输入要查找的时间：（格式：2022-07-07）")
yester_day = yesterday_format
# yester_day = input("输入日期：2022-07-12")

for input_user,input_passwd in zip(user_list,passwd_list):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://scrm.miaoxing100.com/scrm/#/login')
    driver.implicitly_wait(5)
    # print(driver.page_source)
    driver.find_element(By.XPATH,value="/html/body/div[2]/div/div[3]/span/button").click()
    driver.implicitly_wait(5000)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div[1]/input').send_keys(input_user)
    driver.implicitly_wait(5000)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input').send_keys(input_passwd)
    driver.implicitly_wait(5000)
    yzm = input('输入验证码：')
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div[1]/div[1]/div/input').send_keys(yzm)
    # driver.find_element_by_class_name("person-commitment-footer")
    # driver.implicitly_wait(30)
    driver.implicitly_wait(5000)
    # 单击登录
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[5]/div/button').click()
    driver.implicitly_wait(5000)
    # 单击数据报表
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/div').click()
    # driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[10]/div')
    driver.implicitly_wait(5000)
    print("good!")
    # # 单击集约运营
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[1]').click()
    driver.implicitly_wait(5000)
    # 输入起始时间
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/div/input[1]').send_keys(yester_day + " 00:00:00")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/div/input[2]').send_keys(yester_day + " 23:59:59")
    driver.implicitly_wait(5)
    # 单击查询
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/button[1]').click()
    driver.implicitly_wait(5000)
    time.sleep(3)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/button[2]').click()
    driver.implicitly_wait(5000)
    # # 在线企微数
    # zxqws_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[6]/div/span').text
    # driver.implicitly_wait(5)
    # # 在线企微客户数
    # zxqwkhs_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[11]/div/span').text
    # driver.implicitly_wait(5)
    # # 日新增粉丝数
    # rxzfss_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[12]/div/span').text
    # # print(rxzfss_scrm)
    # driver.implicitly_wait(5)
    # # 咨询客户数
    # zxkhs_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[13]/div/span').text
    # # print(zxkhs_scrm)
    # driver.implicitly_wait(5)
    # # 咨询消息数
    # zxxxs_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[14]/div/span').text
    # # print(zxxxs_scrm)
    # driver.implicitly_wait(5)
    # # 企微发送消息总数
    # qwfsxxzs_scrm = driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr/td[15]/div/span').text
    # driver.implicitly_wait(5)
    # print(zxqws_scrm,' 	',zxqwkhs_scrm,' 	',rxzfss_scrm,' 	',zxkhs_scrm,' 	',zxxxs_scrm,' 	',qwfsxxzs_scrm)
    # 单击企微号运营报表
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[2]').click()
    driver.implicitly_wait(5000)
    # 起始时间输入
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/input[1]').send_keys(yester_day + " 00:00:00")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/input[2]').send_keys(yester_day + " 23:59:59")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/button[1]').click()
    driver.implicitly_wait(5000)
    time.sleep(5)
    driver.find_element(By.XPATH,value='//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/button[2]').click()
    time.sleep(15)
    print("----------------------good!----------------------")
    driver.quit()