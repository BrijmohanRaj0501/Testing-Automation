from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# for scroll the window/screen

#scroll by
'''driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollBy(0,400)") #from origin it will scroll to 400px
sleep(2)
driver.execute_script("window.scrollBy(0,400)")# from now it will again scroll to 400px.'''

# scroll to
'''driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0,400)")# from origin it will scroll to 400px
sleep(2)
driver.execute_script("window.scrollTo(0,600)")# noe again from origin it will scroll 600px'''



# Scroll to bottom
'''driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")'''


# scroll to element

#element is at top of the page
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//h2[text()="Mouse Hover"]')
driver.execute_script("arguments[0].scrollIntoView(true)",ele)'''

#element is at bottom of the page
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'//h2[text()="Mouse Hover"]')
driver.execute_script("arguments[0].scrollIntoView(false)",ele)'''


# click()
'''driver.get('https://www.ilovepdf.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.XPATH,'(//a[@href="/split_pdf"])[3]')
driver.execute_script("arguments[0].click()",ele)'''

#value --> for sending keys

'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.ID,'name')
driver.execute_script("arguments[0].value='Brijmohan'",ele)'''

#Task-->01
# Open Amazon
# Search for a product
# click on search icon
# Scroll By 500px

'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(2)
search=driver.find_element(By.ID,'twotabsearchtextbox')
driver.execute_script("arguments[0].value='Shoes'",search)
icon=driver.find_element(By.ID,'nav-search-submit-button')
driver.execute_script("arguments[0].click()",icon)
driver.execute_script("window.scrollTo(0,800)")'''