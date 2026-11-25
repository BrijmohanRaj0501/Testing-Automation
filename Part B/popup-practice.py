from selenium.webdriver import Chrome, ChromeOptions, Keys
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")
o.add_experimental_option("prefs",{"profile.default_content_settings_notifications": 2})

driver = Chrome(options=o)

# for popups-> we have to switch the driver to alert mode
#        syntax--> driver.switch_to.alert()
#
#  there are three types of popups
#  1. simple alert
#        syntax for simple alert-> alert.accept()
#
#     -> in simple popups, we have to only click on ok/accept btn.
#
#2. confirmation alert
#3. prompt alert


#simple alert
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'alertBtn').click()
sleep(2)
simple_alert=driver.switch_to.alert
sleep(2)
simple_alert.accept()
'''

#confirmation alert
'''driver.find_element(By.ID,'confirmBtn').click()
cnf_alert=driver.switch_to.alert
cnf_alert.accept()    # for click on ok
cnf_alert.dismiss()   #for click on cancel

'''

#prompt alert
'''driver.find_element(By.ID,'promptBtn').click()
sleep(2)
prompt_alert=driver.switch_to.alert
prompt_alert.send_keys("Brijmohan")
prompt_alert.accept()
'''


'''driver.get('https://demoqa.com/alerts')
driver.maximize_window()
driver.find_element(By.ID,'alertButton').click()
driver.switch_to.alert.accept()
driver.find_element(By.ID,'timerAlertButton').click()
sleep(6)
driver.switch_to.alert.accept()
driver.find_element(By.ID,'confirmButton').click()
driver.switch_to.alert.accept()
driver.find_element(By.ID,'promtButton').click()
prompt=driver.switch_to.alert
prompt.send_keys("Brijmohan")
prompt.accept()'''




# upload single files
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'singleFileInput').send_keys("E://All resume//Brijmohan-automation-resume.pdf")
driver.find_element(By.XPATH,'//button[text()="Upload Single File"]').click()
'''
#upload multiple files
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'multipleFilesInput').send_keys("E://All resume//Brijmohan-automation-resume.pdf\n","E://link//Brijmohan_Resume_Sdet_a.pdf")
driver.find_element(By.XPATH,'//button[text()="Upload Multiple Files"]').click()'''



# task-->01
'''driver.get('https://demoqa.com/upload-download')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'uploadFile').send_keys("E://All resume//Brijmohan-automation-resume.pdf")'''


# task-02
'''driver.get('https://omayo.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'uploadfile').send_keys("E://All resume//Brijmohan-automation-resume.pdf")
driver.find_element(By.ID,'alert1').click()
driver.switch_to.alert.accept()
driver.find_element(By.ID,'prompt').click()
pro1=driver.switch_to.alert
pro1.send_keys("Brijmohan")
pro1.accept()
driver.find_element(By.ID,'confirm').click()
conf=driver.switch_to.alert
conf.accept()'''

#turn on Safe browsing
'''
from selenium.webdriver import Chrome, ChromeOptions, Keys
o=ChromeOptions()
o.add_experimental_option("detach", True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
from time import sleep
driver = Chrome(options=o)
driver.get('https://www.python.org/downloads/')
driver.find_element(By.XPATH,'(//a[text()="Python 3.15.0"])[4]').click()'''


# simple/Regular HTML popups

# handle flipkart Login Popups
'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="✕"]').click()'''


# handle IRCTC Language Selection Popups
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//button[text()="English"]').click()
driver.find_element(By.XPATH,'//div[@class="h_menu_drop_button hidden-xs"]').click()
driver.find_element(By.XPATH,'//button[text()="LOGIN / REGISTER"]').click()
driver.find_element(By.XPATH,'//input[@formcontrolname="userid"]').send_keys('Trainbooking112')
driver.find_element(By.XPATH,'//input[@formcontrolname="password"]').send_keys('Rajsharma@01')
driver.find_element(By.XPATH,'//button[text()="SIGN IN"]').click()
sleep(2)
driver.execute_script("window.scrollBy(0,400)")
FROM=driver.find_element(By.XPATH,'//input[@role="searchbox"]')
FROM.send_keys('dto')
sleep(1)
FROM.send_keys(Keys.ENTER)
TO=driver.find_element(By.XPATH,'(//input[@role="searchbox"])[2]')
TO.send_keys('HWH')
sleep(1)
TO.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'(//input[@type="text"])[3]').click()
driver.find_element(By.XPATH,'//a[text()="29"]').click()
#driver.find_element(By.XPATH,'(//input[@type="text"])[3]').send_keys('15/10/2026')
sleep(1)
driver.find_element(By.XPATH,'//button[text()=" Search Trains "]').click()
sleep(2)
driver.execute_script("window.scrollBy(0,500)")
sleep(1)
driver.find_element(By.XPATH,'(//div[@class="pre-avl"])[7]').click()
driver.find_element(By.XPATH,'//div[@class="pre-avl selected-class"]').click()
#driver.find_element(By.XPATH,'//div[@class="link ng-star-inserted"]').click()  #  error in these line
driver.find_element(By.XPATH,'//button[@type="button"]').click()


# for blocking the notification --> we have another Browser setting
#     o.add_argument("--disable-notifications")



#handle date select popups
'''driver.get('https://www.easemytrip.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,'ddate').click()
driver.find_element(By.XPATH,'(//div[@class="month3"])[2]').click()
driver.find_element(By.XPATH,'(//div[@class="month3"])[2]').click()
driver.find_element(By.ID,'trd_5_15/01/2027').click()
'''

#for blocking notification
'''o.add_argument("--disable-notifications") #--> only this line will also work
prefs = {"profile.default_content_settings.value.notifications":2} 
o.add_experimental_option("prefs",prefs)'''


# or
'''o.add_argument("--disable-notifications") 
prefs = {"profile.default_content_settings.notifications": 2 ,"safebrowsing.enabled":True}
o.add_experimental_option("prefs", { "profile.default_content_settings.notifications": 2 }) '''







# stale-element reference exception->
# Not-interactable-->element exist but not interactable
# click-intercepted--> some other element is blocking me to click on that particular element  some 2-3 element click simultaneously that only this type of error come..
#                      some 2-3 element click simultaneously that only this type of error come.



