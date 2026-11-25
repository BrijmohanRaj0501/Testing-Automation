'''from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)'''

#tittle_property
'''driver.get("https://www.flipkart.com/")
sleep(2)'''

#current page link
'''before=driver.current_url
print("before", before)
print('after clicking on some links')
driver.maximize_window()
sleep(10)
after=driver.current_url
print("after", after)'''


#page source code
'''pg_src=driver.page_source
print("page_source",pg_src)'''



#task-->1
#open any web page
#fetch its tittle and URL

'''driver.get("https://www.lenskart.com/")
sleep(3)
print("Tittle of the Page: ",driver.title)
print("url of the Page: ",driver.current_url)'''


#Task--->2
#open amazon
#fetch tittle nad url
#open flipkart
#fetch tittle  and url
#go back
#fetch tittle and url
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
'''print("opening amazon")
driver.get("https://www.amazon.in/")
sleep(3)
print("Title of the amazon Page: ",driver.title)
print("url of the Page: ",driver.current_url)
sleep(2)
print("opening flipkart")
driver.get("https://www.flipkart.com/")
sleep(2)
print("Title of the flipkart Page: ",driver.title)
print("url of the flipkart Page: ",driver.current_url)
driver.back()
sleep(2)
print("go back to the previous website")
print("Title of the previous Page: ",driver.title)
print("url of the Page: ",driver.current_url)'''


# Task-->3
# open crocs
# fetch tittle and url
# select any one product manually
# fetch the tittle and url


driver.get("https://www.crocs.in/")
sleep(2)
print("Title of the Crocs Page: ",driver.title)
print("url of the Crocs Page: ",driver.current_url)
print("select any one product manually")
sleep(10)
print("after select product tittle is: ", driver.title)
print("after select product current URL is : ",driver.current_url)
#verification of the script
if 'chrome' in driver.title:
    print("succesful verification")
else:
    print("failed ")

















