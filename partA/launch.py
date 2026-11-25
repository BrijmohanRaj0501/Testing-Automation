#for launch a browser
'''from selenium.webdriver import Chrome
driver= Chrome()'''

#for launch and wait for a minutes
'''from time import sleep
from selenium.webdriver import Chrome
driver= Chrome()
sleep(5)
'''



#from chrome --> Browser setting

'''from selenium.webdriver import Chrome,ChromeOptions
o= ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
'''


#launch brave browser
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")
o.binary_location=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = Chrome(options=o)

driver.get("https://www.burgerking.in/")
driver.maximize_window()
driver.switch_to.alert.accept()
