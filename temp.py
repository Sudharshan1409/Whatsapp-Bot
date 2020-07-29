from selenium import webdriver
import time
import pandas as pd
import os
import xlrd
import autoit
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

fileName = 'test.csv'
messages_excel = 'messages.xlsx'
driver = webdriver.Chrome('D:\python\chromedriver')
driver.get('https://web.whatsapp.com/')
input('after QR Code')

with open(fileName) as file:
    data = pd.read_csv(file)
    df = pd.DataFrame(data)

msgdata = pd.read_excel(messages_excel, sheet_name=r'Sheet1')

for index, row in df.iterrows():
    try:
        search_phone = int(row['phone'])
        search_box = driver.find_element_by_class_name('_2zCfw')
        search_box.send_keys(search_phone)
        time.sleep(2)

        search_box.send_keys(u'\ue007')

        for i in msgdata.index:
            try:

                clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
                clipButton.click()
                time.sleep(1)

                # To send Videos and Images.
                mediaButton = driver.find_element_by_xpath(
                    '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
                mediaButton.click()
                time.sleep(3)

                image_path = os.getcwd() + "\\Media\\" + msgdata['photoName'][i]+'.jpg'

                autoit.control_focus("Open", "Edit1")
                autoit.control_set_text("Open", "Edit1", (image_path))
                autoit.control_click("Open", "Button1")
                time.sleep(1)
                previewMsg = driver.find_element_by_class_name("_3u328").send_keys(u'\ue007')

                time.sleep(3)

                productName = str(msgdata['name'][i])
                oldPrice = str(msgdata['oldqimat'][i])
                newPrice = str(msgdata['newqimat'][i])
                inventory = str(msgdata['inventory'][i])
                msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')


                msg_box.send_keys("stocks")
                msg_box.send_keys(Keys.SHIFT + '\ue007')
                msg_box.send_keys(productName)
                msg_box.send_keys(Keys.SHIFT + '\ue007')
                if oldPrice != 'nan':
                    msg_box.send_keys("oldPrice : "+ oldPrice)
                    msg_box.send_keys(Keys.SHIFT + '\ue007')
                if newPrice != 'nan':
                    msg_box.send_keys("newPrice : "+ newPrice)
                    msg_box.send_keys(Keys.SHIFT + '\ue007')
                if inventory!= 'nan':
                    msg_box.send_keys("inventory : "+ inventory)

                time.sleep(1)
                msg_box.send_keys(Keys.ENTER)

                time.sleep(3)
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        continue

print("sucessfully Done")
