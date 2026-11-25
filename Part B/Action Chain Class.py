from time import sleep
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#1.--> click()
'''driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//a[text()="Coupons"]')
action=ActionChains(driver)
action.click(ele)
action.perform()'''

#2.--> move_to_element()
'''driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//span[text()="Hello, sign in"]')
action=ActionChains(driver)
action.move_to_element(ele).perform()'''

#TASK-->01
#1)open nike('https://www.nike.in/')

'''driver.get('https://www.nike.in/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//div[@class="css-xxb30g"][5]')
action=ActionChains(driver)
action.move_to_element(ele).perform()
sleep(5)
action.click(ele).perform()'''

#3.--> double_click()
'''driver.get('https://demoqa.com/buttons')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'doubleClickBtn')
sleep(2)
action=ActionChains(driver)
action.double_click(ele).perform()'''

#4.--> Right click
'''driver.get('https://demoqa.com/buttons')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.ID,'rightClickBtn')
sleep(2)
action=ActionChains(driver)
action.context_click(ele).perform()'''

#Task--> ## TASK #1) Open https://testautomationpractice.blogspot.com/
# #2) Click on START button
# #3) Mouse hover on POINT ME
# #4) Double click on COPY TEXT

'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//button[@class="start"]')
action=ActionChains(driver)
action.click(ele).perform()
sleep(5)
ele2=driver.find_element(By.XPATH,'//button[text()="Point Me"]')
action.move_to_element(ele2).perform()
sleep(5)
ele3=driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
action.double_click(ele3).perform()
'''


#5.--> Click_and_hold
'''driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(7)
driver.find_element(By.ID,'password').send_keys('asdfg1234@')
sleep(2)
ele=driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action=ActionChains(driver)
action.click_and_hold(ele).perform()'''

#6.--> Release
'''driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(7)
driver.find_element(By.ID,'password').send_keys('asdfg1234@')
sleep(2)
ele=driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action=ActionChains(driver)
action.click_and_hold(ele).release().perform()'''

#7.--> pause for 5 sec. and release
'''driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(7)
driver.find_element(By.ID,'password').send_keys('asdfg1234@')
sleep(2)
ele=driver.find_element(By.XPATH,'//img[@class="ng-star-inserted"]')
action=ActionChains(driver)
action.click_and_hold(ele).pause(5).release().perform()'''


#8.--> Drag and Drop
'''driver.get('https://www.selenium.dev/selenium/web/mouse_interaction')
driver.maximize_window()
sleep(2)
drag=driver.find_element(By.ID,'draggable')
drop=driver.find_element(By.ID,'droppable')
action=ActionChains(driver)
action.drag_and_drop(drag,drop).perform()'''

#drag and drop by offset(size)
'''driver.get('https://www.selenium.dev/selenium/web/mouse_interaction')
driver.maximize_window()
sleep(2)
drag=driver.find_element(By.ID,'draggable')
#drop=driver.find_element(By.ID,'droppable')
action=ActionChains(driver)
action.drag_and_drop_by_offset(drag,60,70).perform()'''


#Scroll to element
'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(5)
ele=driver.find_element(By.XPATH,'//a[text()="Cancellation & Returns"]')
action=ActionChains(driver)
action.scroll_to_element(ele).perform()'''


#scroll by amount(pixels)
'''driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]').send_keys('R rajesh vlog')
sleep(2)
driver.find_element(By.XPATH,'//button[@class="ytSearchboxComponentSearchButton"]').click()
sleep(3)
action=ActionChains(driver)
action.scroll_by_amount(0,600).perform()'''

#scroll from origin(select one element ,
# assume it as starting, from that element , we want to scroll)
'''
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(5)
ele=driver.find_element(By.XPATH,'//button[text()="Point Me"]')
action=ActionChains(driver)
origin=ScrollOrigin.from_element(ele)
action.scroll_from_origin(origin,0,200).perform()'''

#Click ENTER in selenium
'''driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
asdf=driver.find_element(By.XPATH,'//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
asdf.send_keys('Rajesh vlog')
asdf.send_keys(Keys.ENTER)'''

# send keys in capital letter
'''driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
asdf=driver.find_element(By.XPATH,'//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
action=ActionChains(driver)
action.key_up(Keys.SHIFT).send_keys_to_element(asdf,"tom-and-jerry").perform()'''


# remove the text
'''action.key_down(Keys.CONTROL).send_keys('a').send_keys_to_element(asdf,Keys.BACKSPACE).perform()'''


