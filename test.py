import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
serv_obj = Service("/snap/chromium/2565/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://selectorshub.com/xpath-practice-page/')
driver.maximize_window()
time.sleep(2)
#driver.find_element('id', 'userId').send_keys('saira@gmail.com')
#time.sleep(1)
#driver.find_element('id', 'pass').send_keys('saira1234')
#time.sleep(1)
#driver.find_element('name', 'company').send_keys('Aleh.tech')
#time.sleep(1)
#driver.find_element('name', 'mobile number').send_keys('03214234657')
#time.sleep(1)
#driver.find_element('xpath', '//input[@value="Submit"]').click()
#time.sleep(1)
#driver.find_element('id', 'inp_val').send_keys('Nope')
#time.sleep(2)
#driver.find_element('id', 'ohrmList_chkSelectAll').click()
#driver.find_element('id', 'ohrmList_chkSelectRecord_25').click()
#time.sleep(2)
#time.sleep(2)
#driver.find_element('id', 'ohrmList_chkSelectRecord_21').click()
#time.sleep(2)
#driver.find_element('id', 'ohrmList_chkSelectRecord_2').click()
#time.sleep(2)
#driver.find_element('id', 'ohrmList_chkSelectRecord_14').click()
#time.sleep(2)
#driver.find_element('id', 'ohrmList_chkSelectRecord_15').click()
#time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='kils']").send_keys("saira")
time.sleep(2)

r5yrt7yur7u6