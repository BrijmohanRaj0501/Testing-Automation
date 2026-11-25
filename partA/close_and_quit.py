from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#close --> close the Current Tab
'''driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(5)  # open 2-3 tab manually
driver.close()'''

#quit --> close all the tab (means close the entire window)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5) # open 2-3 tab manually
driver.quit()


#task---> 01
# open amazon
# refresh it
# fetch the tittle
# open myntra
# fetch tittle
# close


'''driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5)
driver.refresh()
print("tittle of the amazon", driver.title)
sleep(2)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(2)
print("title of the myntra", driver.title)
driver.close()'''

# self_Practice
'''driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(10)
driver.close()'''



# Date-11sept
'''driver.get("https://www.flipkart.com/")
sleep(3)
driver.refresh()
print("title of the flipkart : ", driver.title)
print("URL of the flipkart : ", driver.current_url)
sleep(2)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.refresh()
print("tittle of amazon : ",driver.title)
print("URL of the amazon", driver.current_url)'''