from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# 1. click()
#       syntax= element.click()

# 2. Send_keys()
#       syntax= element.send_keys('Text')

#3. clear()
#        Syntax= element.clear()
'''
driver.get('https://www.youtube.com/')
sleep(2)
ele = driver.find_element(By.XPATH,'//input[@class="ytSearchboxComponentInput yt-searchbox-input title"]')
ele.send_keys('Tom and jerry')
but=driver.find_element(By.XPATH,'//button[@class="ytSearchboxComponentSearchButton"]')
but.click()
sleep(2)
ele.clear()
sleep(2)
driver.close()'''



# WEB ELEMENT METHOD
#_________________________________________________________________________________

# 1.) is_displayed()

#    when the element is displayed on screen, it will return 'True'
#    when the input is not present in screen,  it will displayed 'False'
#
#
'''driver.get('https://www.facebook.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//input[@name="email"]')
print('element is displayed: ',ele.is_displayed())
hid=driver.find_element(By.XPATH,'//input[@type="submit"]/..')
print('element is displayed: ',hid.is_displayed())'''


# 2.)   is_enabled()
#   it is a web element method that is used to check where the button is enabled or not.
#    it will return True and False.

'''driver.get('https://www.naukri.com/registration/createAccount?othersrcp=22636')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//button[@type="submit"]')
print('button is displayed',ele.is_displayed())
print('button is enabled',ele.is_enabled())'''



# 3.) is_selected()
# it is a web element method used to check whether element is selected or not.
# is_selected()--> it will return 'True' if the element is selected., otherwise 'False'


'''driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(2)
yes=driver.find_element(By.ID,'yesRadio')
print('yes is displayed: ',yes.is_displayed())
print('yes is enabled: ',yes.is_enabled())
print('yes is selected: ',yes.is_selected())
sleep(4)
yes.click()
print('after clicking on yes')
print('yes is selected: ',yes.is_selected())'''


# Task--> 01
#open this web page('https://demowebshop.tricentis.com/register')
#locate any one of the gender
#check all things-> check is it is_dsiaplayed(), is_enabled(), is_selected()
# click on it
# after clicking, check it is enabled or not.
'''driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
sleep(2)
M=driver.find_element(By.ID,'gender-male')
print('Male is displayed: ',M.is_displayed())
print('Male is enabled: ',M.is_enabled())
print('Male is selected: ',M.is_selected())
sleep(4)
M.click()
print('after clicking on Male')
print('Male is selected: ',M.is_selected())'''



# ATTRIBUTE AND CONTENT METHOD
# 1.) Tag name

#                 syntax: Element.tag_name

'''driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
sleep(2)
M=driver.find_element(By.ID,'gender-male')
print(M.tag_name)
'''


# 2.) Attribute
# It is a web element method used to get attribute and value of a web element

 #                syntax=element.get_attribute('attribute_name')

#       < id='para1' class='basic para' name='intro'>

#            ele.get_attribute('id') ---> para1
#            ele.get_attribute('class')  --> basic para


#3) text
# it is used to get visible text of an element

#               syntax: element.text


# TASK--> open https://demowebshop.tricentis.com/register
# locate Register link, Register button
# find their tagname
# find any two attribute value for each
# find the visible text of the element
'''driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
sleep(2)
R=driver.find_element(By.XPATH,'//a[text()="Register"]')
R2=driver.find_element(By.ID,'register-button')
print('Register link tagname :',R.tag_name)
print('Register button tagname :',R2.tag_name)
print('Register link :',R.get_attribute('href'))
print('Register link class :',R.get_attribute('class'))
print('Register button type : ',R2.get_attribute('type'))
print('Register button Id :',R2.get_attribute('id'))
print('Register link text : ',R.text)
print('Register button text : ',R2.text)'''





#------------------------------------------------------------------------------

# size and location


# Size, Location and Rect of a particular element


'''
driver.get('https://demowebshop.tricentis.com/register')
driver.maximize_window()
sleep(2)
R=driver.find_element(By.XPATH,'//a[text()="Register"]')
print(R.size)
print(R.location)
print(R.rect)'''



# task--> # TASK--> 01

# #1) Open Amazon
# #2) Fetch size,position and rect of search field and search button
# #3) Fetch its 2 attribute values
# #4) Check if its displayed and enabled
# #5) Pass and input and click on the button

'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(2)
search=driver.find_element(By.ID,'twotabsearchtextbox')
button=driver.find_element(By.ID,'nav-search-submit-button')
print('search field size : ',search.size)
print('serarch field location :',search.location)
print('search field rect :',search.rect)
print('attribute of search field :',search.get_attribute('class'))
print('attribute of search field :',search.get_attribute('role'))
print('search is displayed : ',search.is_displayed())
print('search is enabled :',search.is_enabled())
print('search button size :',button.size)
print('search button location:',button.location)
print('search button rect :',button.rect)'''


# TASK-->02

#1) Open Flipkart
#2) Sleep - close the popup manually
#3) Search for mobiles
#4) Using mobile name , fetch the price


'''driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(5)
search=driver.find_element(By.XPATH,'//input[@class="nw1UBF v1zwn26"]')
search.send_keys('mobiles')
driver.find_element(By.XPATH,'//button[@class="XFwMiH"]').click()
sleep(2)
price=driver.find_element(By.XPATH,'//div[text()="REDMI A7 Pro 5G (Black, 64 GB)"]/../../div[2]//div[1]')
print(price.text)'''