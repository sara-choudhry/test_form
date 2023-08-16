import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
serv_obj = Service("/snap/chromium/2565/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.orangehrm.com/Security/login?BackURL=%2Fadmin%2Fpages%2F')
driver.maximize_window()
driver.find_element(By.NAME,"Email").send_keys("sairamehmood@gmail.com")
driver.find_element(By.ID,"MemberLoginForm_LoginForm_Password").send_keys("saira")
print(driver.title) #To capture the title of the current page
print(driver.current_url) #To capture the current url of web page
print(driver.page_source) #To capture the source code of the page
Email=driver.find_element(By.NAME,"Email")
print("Email field is enable:", Email.is_enabled())
print("Email is displayed:", Email.is_displayed())
act_title = driver.title
exp_title = "OrangeHRM: Log in"
if act_title == exp_title:
    print("Login test Passed")
else:
    print("Login test Failed")
time.sleep(2)


