# synchronization---
# make selenium wait until the web page is-ready
# because sometimes web page load takes times(dur to dynamic element)
# and selenium is much faster than the browser
from calendar import firstweekday

from selenium import webdriver
from selenium.common import NoSuchElementException
#so we get an error called --> no such element expectation , time-out expectation ,
# element not interactable etc .

# there are four type of wait :-
# 1. static wait -> Fixed Wait/force wait for a fixed duration of time
#                   (nothing will execute in this time) and it is hard coded.
#                  => eg - sleep(3) | after 3 sec. it will move to next execution
# it doesn't check if the page is ready for interaction
# wait for fixed time of duration
#Disadvantage--> 1. it's not dynamic
#                2. Time is wasted
#                3. slower Execution

# 2. Implicit wait -> implicit wait it waits for maximum amount of time
#                    while finding the element before throwing the exception.
#                  -> only for find_element() or find_elements() method
#                  -> not for element actions
# -> if the element appears early , selenium contains immediately with the next step
#                  -> implicit wait is called as GLOBAL DYNAMIC WAIT.
#                    -> GLOBAL ->applies to all the element in webdriver session.
#                    -> DYNAMIC ->doesn't wait for full,
#                                 stop wait as soon as element is encountered
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


# execution of implicit wait
'''driver.get("https://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="✕"]').click()'''


#Task-01 implicit wait
'''driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[@href="/shop/Bags-Store"]').click()
driver.find_element(By.XPATH,'//a[@href="/c/little-explorers-930014"]').click()
driver.find_element(By.XPATH,'(//div[@data-tests-id="product-card-content"])[4]').click()
driver.find_element(By.XPATH,'(//button[@data-tests-id="pdp:add-to-cart-button"])').click()
driver.close()'''


'''
#task-02
driver.get('https://www.nike.in')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'(//span[text()="Kids"])[1]').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,'(//a[text()="Clothing"])[5]').click()
driver.find_element(By.XPATH,'//a[@class="css-1o8jw7q"]').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,'//label[text()="M"]').click()
driver.find_element(By.XPATH,'//button[text()="Add to Bag"]').click()
'''
'''
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,'start').click()
print(driver.find_element(By.ID,'finish').text)'''
# window,

# 3. explicit wait ->
'''driver.get('https://www.shoppersstack.com/')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'')'''

# 4. fluent wait ->
# Fluent wait is a advanced Synchronization mechanism in selenium webdriver that
# let you define how long to wait or a condition, how often to check for it.
# and which exception to ignore while Polling.

'''driver.get('https://www.shoppersstack.com/')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'(//div[@data-aos="zoom-in"])[6]').send_keys('822101')
Pin=driver.find_element(By.ID,'Check Delivery').send_keys('822101')
Pin.click()
Pin.send_keys("822101")
wait=WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
check_btn=wait.until(EC.element_to_be_clickable(By.ID,'Check'))
check_btn.click()
--> not completed
'''

#task-->01
'''driver.get('https://www.amazon.in/')
driver.maximize_window()
wait=WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
search=wait.until(EC.visibility_of_element_located((By.ID,'twotabsearchtextbox')))
search.send_keys('phones')
icon=wait.until(EC.visibility_of_element_located((By.ID,'nav-search-submit-button')))
icon.click()
phn=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="a-section"])[2]')))
phn.click()
driver.switch_to.window(driver.window_handles[-1])
cart=wait.until(EC.visibility_of_element_located(By.XPATH,'//input[@id="add-to-cart-button"]')))
--> not completed'''


#task-> 02
# open -> https://demowebshop.tricentis.com/
# click on Register
# Fill all details and click on Register_btn.

'''driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
driver.implicitly_wait(30)
wait= WebDriverWait(driver,10)
register=wait.until(EC.visibility_of_element_located((By.XPATH,'//a[text()="Register"]')))
register.click()
gender=wait.until(EC.element_to_be_clickable((By.ID,'gender-male')))
gender.click()
first_name =wait.until(EC.visibility_of_element_located((By.ID,'FirstName')))
first_name.send_keys('Brijmohan')
last_name =wait.until(EC.visibility_of_element_located((By.ID,'LastName')))
last_name.send_keys('Sharma')
email=wait.until(EC.visibility_of_element_located((By.ID,'Email')))
email.send_keys('brij1234@gmail.com')
pas=wait.until(EC.visibility_of_element_located((By.ID,'Password')))
pas.send_keys('Rajsharma%01')
cnf_pas=wait.until(EC.visibility_of_element_located((By.ID,'ConfirmPassword')))
cnf_pas.send_keys('Rajsharma%01')
register_btn=wait.until(EC.element_to_be_clickable((By.ID,'register-button')))
register_btn.click()
'''





















