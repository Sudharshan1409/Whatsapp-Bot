from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'))
print(os.path.join(os.getcwd(),'chromedriver'))
driver.get('https://web.whatsapp.com/')
import time
# import pandas as pd

# df = pd.read_csv('selected_contacts.csv')
phone_number = [
    9844010709,
    9900561823,
    8123926718,
    9904911355,
    8050601265,
    9980074684,
    7019563339,
    9945560402,
    9163916684,
    7022720023,
    9845304408,
    8861361406,
    9980643140,
    9886046793,
    9886430874,
    9738956815,
    9901152742,
    9845947220,
    8861139945,
    9900035142,
    9663009990,
    8095019708,
    7259691900,
    9916681927,
    8121546547,
    9945770902,
    8217894226,
    9980531902,
    9880022552,
    9740126512,
    9591745454,
    9591411225,
    9886394833,
    9448191016,
    7338300379,
    9880162063,
    9663020230,
    7259252997,
    9482399706,
    9606408841,
    9986261137,
    9880704500,
    9731985544,
    9900106693,
    7406740740,
    9900144679,
    7406387747,
    9482604097,
    9980934650,
    8951525964,
    9845195909,
    9042729165,
    9900915929,
    9945915303,
    9980133251,
    8050949878,
    9742265184,
    9035478948,
    9845794299,
    9845736972,
    9841699182,
    8050518950,
    9341229259,
    9740509000,
    8197071484,
    9930661539,
    9538504832,
    9845199691,
    9538553334,
    9845734747,
    9901034009,
    9845040962,
    9342575252,
    9686278602,
    7338346113,
    9449078798,
    9741751498,
    8498057794,
    8308773100,
    9900369130,
    7353650321,
    9845093009,
    9945226465,
    7975242956,
    9986445810,
    9901407672,
    9880321754,
    9901646224,
    9844473178,
    8050692818,
    9099050063,
    9739162700,
    9844479145,
    9663033048,
    9686401019,
    9342569346,
    9945392547,
    9742219059,
    9901380649,
    9886642276,
    9008034922,
    8618643637,
    9739798432,
    8660897885,
    9980813832,
    9880250578,
    9886855588,
    9731155226,
    9844475449,
    9448991389,
    9449830365,
    9845015828,
    9538318415,
    8095763903,
    9886715367,
    9666899122,
    8618514466,
    8095632517,
    9980582562,
    8762638900,
    9900960401,
    9136916684,
    9886065039,
    7829371161,
    9008705706,
    9743153650,
    9581581646,
    9902265350,
    9341319102,
    9738580492,
    8867472178,
    7676855018,
    9980139938,
    8143292181,
    9741448538,
    9663899122,
    9886969656,
    9535081846,
    9945518661,
    7892472785,
    9449349540,
    9886139330,
    9740544464,
    8277490650,
    9611668296,
    9845367367,
    9916899216,
    8660672150,
    9535611554,
    9845257423,
    9980141346,
]
# filepath = os.path.join(os.getcwd(),input('Enter File Name: '))
content = """Greetings from SukalpaSeva!!!

We are now on WhatsApp to make the communication much more easier...

Last few days of Dhanurmaasa. Huggi Naivedya is vishesha. 

Hurry up and book Huggi Seva from SukalpaSeva with a discounted price of 10%.

You can also book Rathotsava and other Sevas for Thursday through E-Seva.

Download and register here if you haven't done so...

“Sukalpa Seva" — Just book and relax
https://play.google.com/store/apps/details?id=com.event.sukalpaseva

Do refer your friends and relatives to get exclusive referral cashback

For any queries, Contact us on: +91 8660672150 / 8618880643"""

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

search_element = driver.find_element_by_xpath('//div[@class = "{}"]'.format('_1awRl copyable-text selectable-text'))
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
for name in phone_number:
    print(name)
    search_element.send_keys(name)
    time.sleep(2)
    search_element.send_keys(u'\ue007')
    # attach_button = driver.find_element_by_xpath('//div[@title = "{}"]'.format('Attach'))
    # attach_button.click()
    # image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    # image_box.send_keys(filepath)
    # time.sleep(1)
    content_button = driver.find_element_by_xpath('//div[@class = "{}" and @data-tab = "6"]'.format('_1awRl copyable-text selectable-text'))
    for line in content.split('\n'):
        content_button.send_keys(line, Keys.SHIFT, Keys.ENTER)
    time.sleep(1)
    send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()
    time.sleep(1)
