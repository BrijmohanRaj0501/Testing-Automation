from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)



#back
'''driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(10)  #click on any link manually
driver.back()'''    #it will go back to the page you click

# forward
'''sleep(5)
driver.forward()'''         # it will move to that page where you click and go previously

#reload the same page
'''sleep(3)
driver.refresh()'''

#date-->9sept
#task--> 1
'''driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.refresh()
sleep(3)
driver.get("https://www.w3schools.com")
driver.refresh()
sleep(3)
driver.back()
sleep(3)
driver.forward()'''


