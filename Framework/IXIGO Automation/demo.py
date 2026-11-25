from time import sleep
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.ixigo.com/")
driver.maximize_window()
sleep(8)
driver.switch_to.frame(0)
popup=driver.find_element(By.XPATH,'//span[text()="×"]')
popup.click()
driver.switch_to.default_content()
from_input=driver.find_element(By.XPATH,'//p[@data-testid="originId"]')
from_input.click()
from_input.send_keys(Keys.CLEAR)
