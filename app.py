from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'))
print(os.path.join(os.getcwd(),'chromedriver'))
driver.get('https://web.whatsapp.com/')
import time
import pandas as pd

df = pd.read_csv('selected_contacts.csv')

filepath = os.path.join(os.getcwd(),input('Enter File Name: '))
content = input('Enter the content: ')
# msg = input('Enter Your Message : ')
# count = int(input('Enter the count : '))
input('Enter Anything after scanning QR code')

# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
#
# msg_box = driver.find_element_by_xpath('//*[@id = "main"]/footer/div[1]/div[2]/div/div[2]')
#
# for i in range(count):
#     msg_box.send_keys(msg+str(i))
#     button = driver.find_element_by_xpath('//*[@id = "main"]/footer/div[1]/div[3]/button')
# button.click()

search_element = driver.find_element_by_xpath('//div[@class = "{}"]'.format('_3FRCZ copyable-text selectable-text'))
# search_focus = driver.find_element_by_xpath('//div[@class = "{}"]'.format('_2FVVk cBxw-'))
# search_visible = driver.find_element_by_xpath('//div[@class = "{}"]'.format('_2FbwG'))
#
# value = user.get_attribute('class')
# print(value)
# driver.execute_script('arguments[0].innerHTML = "smitha"', search_element)
# driver.execute_script('arguments[0].setAttribute("class","_2FVVk cBxw- focused")', search_focus)
# driver.execute_script('arguments[0].style.visibility = "hidden"', search_visible)
# driver.findElement(By.xpath("(//input[@id='search-text'])[2]")).sendKeys("FAA");


# search_box = driver.find_element_by_class_name('_3FRCZ copyable-text selectable-text')
for name in df['Name']:
    print(name)
    search_element.send_keys(name)
    time.sleep(2)
    search_element.send_keys(u'\ue007')
    attach_button = driver.find_element_by_xpath('//div[@title = "{}"]'.format('Attach'))
    attach_button.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    time.sleep(1)
    content_button = driver.find_element_by_xpath('//div[@class = "{}" and @data-tab = "1"]'.format('_3FRCZ copyable-text selectable-text'))
    content_button.send_keys(content)
    time.sleep(1)
    send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()
    time.sleep(1)
