from time import sleep
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#1. find elements with ID locators

'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,'slot-list-container')
print("element found!!")
'''
#by find_elements with id locators
'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(3)
print(driver.find_elements(By.ID,'product-4'))
print("element found!!")'''


#try to locate and give input to the elements
'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('watch')
driver.find_element(By.ID,'nav-search-submit-button').click()
sleep(5)
driver.close()'''


#or
'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(3)
ele = driver.find_element(By.ID,'twotabsearchtextbox')
ele.send_keys('watch')
btn = driver.find_element(By.ID,'nav-search-submit-button')
btn.click()
sleep(3)
driver.close()'''


# --> 2. Find elements with name locator
'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.NAME,'field-keywords').send_keys('mobile')
driver.find_element(By.ID,'nav-search-submit-button').click()
sleep(5)
driver.close()
'''

# --> Find elements with CLASS NAME
'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.CLASS_NAME,'nav-input.nav-progressive-attribute.hokuto-rotate-fade').send_keys('watch')'''


# TAG NAME
'''driver.get('https://www.google.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.TAG_NAME,'textarea').send_keys('python selenium')'''



#task--1
# using tag_name, click on the link on google.com
'''driver.get('https://www.google.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.TAG_NAME,'a').click()'''

# Task-2

'''driver.get('https://demoqa.com/text-box')
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,'userName').send_keys('Brijmohan')
driver.find_element(By.ID,'userEmail').send_keys('Brij@gmail.com')
driver.find_element(By.ID,'currentAddress').send_keys('Kolkata')
driver.find_element(By.ID,'permanentAddress').send_keys('jharkhand')
driver.find_element(By.ID,'submit').click()'''


# LINK_TEXT
'''driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,'Hello,.sign.in').click()'''


#BY CSS SELECTOR
'''driver.get('https://www.lenskart.com')
sleep(5)
driver.maximize_window()
sleep(3)
driver.find_element(By.CSS_SELECTOR,'a[href="https://www.johnjacobseyewear.com/"]').click()'''

'''driver.get('https://www.instagram.com/?hl=en')
sleep(3)
driver.maximize_window()
sleep(3)
driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username webauthn"]').send_keys('brij_2729')
sleep(3)
driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('Rajsharma@011953')
sleep(5)
driver.find_element(By.CSS_SELECTOR,'div[class="x9f619 x1n2onr6 x1ja2u2z x193iq5w xeuugli x6s0dn4 x78zum5 x2lah0s x10ksdce x16k4gxc"]').click()'''


#--> task-1
# open youtube
# search for a video
# click on search button
# fetch tittle and url of the page


'''driver.get('https://www.youtube.com/')
sleep(3)
driver.maximize_window()
sleep(3)
Pawan=driver.find_element(By.CSS_SELECTOR,'input[class="ytSearchboxComponentInput yt-searchbox-input title"]')
Pawan.send_keys('tom and jerry')
driver.find_element(By.CSS_SELECTOR,'button[class="ytSearchboxComponentSearchButton"]').click()
sleep(5)
print("current URL: ",driver.current_url)
print("tittle: ",driver.title)'''



# Task --> 01

'''driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
sleep(3)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'[name="username"]').send_keys('Admin')
sleep(3)
driver.find_element(By.CSS_SELECTOR,'[type="password"]').send_keys('admin123')
sleep(3)
driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()'''








## TASK

#1) Open https://demoqa.com/text-box
#2) Fill the tests fields and click on submit button
'''
driver.get('https://demoqa.com/text-box')
sleep(3)
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'//input[@placeholder="Full Name"]').send_keys('brijmohan sharma')
driver.find_element(By.XPATH,'//input[@placeholder="name@example.com"]').send_keys('brij@gmail.com')
driver.find_element(By.XPATH,'//textarea[@placeholder="Current Address"]').send_keys('Kolkata')
driver.find_element(By.XPATH,'//textarea[@id="permanentAddress"]').send_keys('jharkhand')
driver.find_element(By.XPATH,'//button[@id="submit"]').click()'''

# date--22-09-26

#--> XPATH by Text
'''driver.get('https://www.amazon.in/')
sleep(3)
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH,'//a[text()=" Electronics "]').click()'''


#--> XPATH by group by index
'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH,'(//div[@dir="auto"])[3]').click()'''


#--> task-01
'''
driver.get('https://www.amazon.in/')
sleep(3)
driver.find_element(By.XPATH,'//a[text()=" Electronics "]').click()
sleep(3)
driver.find_element(By.XPATH,'(//span[@dir="auto"])[4]').click()'''


#xpath by forward traversing

#-->task-2
#go to amazon.com-> go to bestseller-> choose a product -> add to cart
'''driver.get('https://www.amazon.in/')
sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH,'//a[@data-csa-c-content-id="nav_cs_bestsellers"]').click()
sleep(5)
driver.find_element(By.XPATH,'(//div[@class="p13n-sc-uncoverable-faceout"])[3]').click()
sleep(5)
driver.find_element(By.XPATH,'//input[@name="submit.add-to-cart"]').click()
'''



#XPATH by Backward Traversing
#Task-->1
'''driver.get('https://demoqa.com/webtables')
sleep(2)
driver.maximize_window()
coll=driver.find_element(By.XPATH,'//td[text()="Cierra"]/../td[3]')
print("Age :",coll.text)
sal=driver.find_element(By.XPATH,'//td[text()="Cierra"]/../td[5]')
print("Sal :",sal.text)
dept=driver.find_element(By.XPATH,'//td[text()="Cierra"]/../td[6]')
print("Dept :",dept.text)'''




'''driver.get('https://www.prokabaddi.com/standings')
driver.maximize_window()
play=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../../div[3]')
print("Play :",play.text)
won=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../../div[4]')
print("Won :",won.text)
lost=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../../div[5]')
print("Lost :",lost.text)
diff=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../../div[6]')
print("Score Difference :",diff.text)
total=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../../div[8]')
print("Total Points:",total.text)'''


#xpath with following siblings
'''driver.get('https://demoqa.com/webtables')
sleep(2)
driver.maximize_window()
sal=driver.find_element(By.XPATH,'//td[text()="Vega"]/following-sibling::td[3]')
print("Sal :",sal.text)
sleep(2)
driver.quit()'''

#xpath by preceding siblings
'''driver.get('https://demoqa.com/webtables')
sleep(2)
driver.maximize_window()
first=driver.find_element(By.XPATH,'//td[text()="Insurance"]/preceding-sibling::td[5]')
print("First Name :",first.text)'''

## Task--> 01
'''driver.get('https://www.prokabaddi.com/standings')
sleep(2)
driver.maximize_window()
total=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../following-sibling::div[1]')
print("Total Points :",total.text)
won=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../following-sibling::div[2]')
print("Won Points :",won.text)
lost=driver.find_element(By.XPATH,'//p[text()="Puneri Paltan"]/../../../following-sibling::div[3]')
print("Lost Points :",lost.text)
sleep(2)
driver.quit()'''

