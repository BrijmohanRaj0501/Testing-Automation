from time import sleep

from select import select
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.safari import options
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

'''driver.get('http://127.0.0.1:5500/revision.py/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1=driver.find_element(By.ID,'loc')
option=Select(dropdown1)
option.select_by_visible_text('Gujrat')'''


# select_by_index
'''driver.get('http://127.0.0.1:5500/revision.py/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1=driver.find_element(By.ID,'loc')
option=Select(dropdown1)
option.select_by_index(4)'''


# select_by_value
'''driver.get('http://127.0.0.1:5500/revision.py/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1=driver.find_element(By.ID,'loc')
option=Select(dropdown1)
option.select_by_value('MH')'''

#task-->01
# in multi select three options by values, index and visible text

'''driver.get('http://127.0.0.1:5500/revision.py/dropdown.html')
driver.maximize_window()
sleep(2)
dropdown1=driver.find_element(By.ID,'hobbies')
option1=Select(dropdown1)
option1.select_by_value('cook')
#option2=Select(dropdown1)
option1.select_by_visible_text('Singing')
#option3=Select(dropdown1)
option1.select_by_index(5)
sleep(3)'''


#deselect the dropdown

#option1.deselect_all()
#option1.deselect_by_value('cook')
#option1.deselect_by_visible_text('cooking')
#option1.deselect_by_index(3)

# TASK-->01
#1) Open https://demowebshop.tricentis.com/
#2) Click on Apperal and Shoes
#3) Choose Low to High ---> Sort By dropdown
 #  Choose 4           ---> Display dropdown
 #  Choose List        ---> View As dropdown

'''driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//li[@class="inactive"][4]').click()
dropdown1=driver.find_element(By.ID,'products-orderby')
sort=Select(dropdown1)
sort.select_by_index(3)
sleep(3)
dropdown2=driver.find_element(By.ID,'products-pagesize')
display=Select(dropdown2)
display.select_by_visible_text('4')
sleep(3)
dropdown3=driver.find_element(By.ID,'products-viewmode')
view=Select(dropdown3)
view.select_by_visible_text('List')
sleep(5)
driver.close()'''

#Task--> 02
# Open ->
# click on English
# chose from Station
# Chose To Station
# click on GET Details

'''driver.get('https://www.bmrc.co.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//span[text()="English"]').click()
sleep(2)
driver.find_element(By.XPATH,'//select[@class="form-control select fare-selects"][1]').click()
dropdown1=driver.find_element(By.XPATH,'//select[@class="form-control select fare-selects"][1]')
from1=Select(dropdown1)
from1.select_by_visible_text('Nallur Halli')
sleep(3)
driver.find_element(By.XPATH,'//select[@class="form-control select fare-selects"][2]').click()
dropdown2=driver.find_element(By.XPATH,'//select[@class="form-control select fare-selects"][2]')
from2=Select(dropdown2)
from2.select_by_visible_text('Kadugodi Tree Park')
sleep(3)
driver.find_element(By.XPATH,'//button[@class="app-btn-box"]').click()'''



# Auto Suggestion
#---------------------------------------------------------------------------------------------
#print all the suggestion text.

'''driver.get('https://www.amazon.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('Shoes')
sleep(2)
sugg=driver.find_elements(By.XPATH,'//div[@class="s-suggestion-container"]')
for i in sugg:
    #print(i.text)
    if "shoes organizer" in i.text:
        i.click()
        break

sleep(2)
driver.close()'''

'''
driver.get('https:/www.google.com')
sleep(2)
driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys('Modi')
sleep(2)
sugg=driver.find_elements(By.XPATH,'//li[@class="sbct PZPZlf sbre"]')
for i in sugg:
#    print(i.text)
#    if 'Prime Minister of India' in i.text:
#        i.click()
#        break

'''

# practice task-01
'''driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//label[text()="Colors:"]')
action=ActionChains(driver)
action.scroll_by_amount(0,600).perform()
Dropdown1=driver.find_element(By.ID,'colors')
option=Select(Dropdown1)
option.select_by_visible_text('Red')'''


#task=02
#1) Open Amazon
#2) Search for a product and click search icon
#3) Choose any one checkbox
#4) Automate the dropdown
#5) Choose a product , print its price and click on it
#6) Add to Cart

'''
driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('shoes')
driver.find_element(By.ID,'nav-search-submit-button').click()
driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-checkbox"]').click()
driver.find_element(By.XPATH,'//span[@class="a-button a-button-dropdown a-button-small"]').click()
driver.find_element(By.ID,'s-result-sort-select_2').click()
# Not_completed
'''
