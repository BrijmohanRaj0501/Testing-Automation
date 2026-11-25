# iframes= web page inside another web page
#      OR
#   IT IS A embedded web page inside a webpage
# it was developed by using tag called <iframe src="link of another web page " >


#when we are automating a web page using selenium sometimes, we may try to access the elements
# but selenium throws --> no_such_element exception , even elements is present inside a web page



# so we will use Switch_to_frame methods
# Switch_to.frame(args) --> move selenium focus from main page to iframes
# so that element can be accessed
# arguments(args) can be --> 1. index
#                            2. name
#                            3. web element



from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)



#1. index as argument
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.find_element(By.ID,'inp1').send_keys('Brihmohan')
sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp2').send_keys('Sharma')
sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp3').send_keys('done')'''

#directly switch to Page-3
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.switch_to.frame(0)
sleep(2)
driver.switch_to.frame(0)
driver.find_element(By.ID,'inp3').send_keys('done')'''

# 2.name as argument
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.find_element(By.ID,'inp1').send_keys('Brihmohan')
sleep(2)
driver.switch_to.frame('frame1')
driver.find_element(By.ID,'inp2').send_keys('Sharma')
sleep(2)
driver.switch_to.frame('frame2')
driver.find_element(By.ID,'inp3').send_keys('done')'''

#3. web element as argument
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.find_element(By.ID,'inp1').send_keys('Brihmohan')
sleep(2)
frame1=driver.find_element(By.XPATH,'//iframe[@src="page2.html"]')
driver.switch_to.frame(frame1)
driver.find_element(By.ID,'inp2').send_keys('Sharma')
sleep(2)
frame2=driver.find_element(By.XPATH,'//iframe[@src="page3.html"]')
driver.switch_to.frame(frame2)
driver.find_element(By.ID,'inp3').send_keys('done')'''


#switch to parent frames
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.find_element(By.ID,'inp1').send_keys('Brihmohan')
driver.switch_to.frame('frame1')
driver.find_element(By.ID,'inp2').send_keys('Sharma')
driver.switch_to.frame('frame2')
driver.find_element(By.ID,'inp3').send_keys('done')
driver.switch_to.parent_frame()
driver.find_element(By.ID,'inp2').clear()
driver.find_element(By.ID,'inp2').send_keys('back_to_parent')'''

#switch to default content
'''driver.get('http://127.0.0.1:5500/revision.py/practice.py/page1.html')
driver.find_element(By.ID,'inp1').send_keys('Brihmohan')
driver.switch_to.frame('frame1')
driver.find_element(By.ID,'inp2').send_keys('Sharma')
driver.switch_to.frame('frame2')
driver.find_element(By.ID,'inp3').send_keys('done')
driver.switch_to.default_content()
driver.find_element(By.ID,'inp1').clear()
driver.find_element(By.ID,'inp1').send_keys('back_to_default')
sleep(5)
driver.close()'''

#Task-->01
'''driver.get('https://www.zomato.com/kolkata/restaurants')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//button[text()="Log in"]').click()
sleep(2)
frame1=driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]')
driver.switch_to.frame(frame1)
sleep(2)
frame3=driver.find_element(By.XPATH,'//iframe[@class="L5Fo6c-PQbLGe"]')
driver.switch_to.frame(frame3)
sleep(2)
driver.find_element(By.ID,'container-div').click()'''


#task-02
'''driver.get('https://www.burgerking.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//div[@class="select-service__card_container"]').click()
sleep(2)
driver.find_element(By.XPATH,'//span[text()="login"]').click()
sleep(2)
iframe=driver.find_element(By.XPATH,'//iframe[@class="L5Fo6c-PQbLGe"]')
driver.switch_to.frame(iframe)
sleep(2)
driver.find_element(By.XPATH,'//span[text()="Sign in with Google"]').click()'''


