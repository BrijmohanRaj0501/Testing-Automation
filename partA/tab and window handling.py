from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)



#current window handle --> it will return string type
'''driver.get("https://www.flipkart.com/")
sleep(2)
id_tab = driver.current_window_handle
print(id_tab)
driver.get("https://www.google.com")
sleep(2)
id_tab2=driver.current_window_handle
print(id_tab2)
driver.close()
'''

#window handles --> it will return list type
'''driver.get("https://www.flipkart.com/")
sleep(5) #manually open 2-3 tabs
id_tac = driver.current_window_handle
print(id_tac)
id_tac2=driver.window_handles
print(id_tac2)'''


#switch to new tab and new window

#1--> open two tab in same window
'''driver.get("https://www.flipkart.com/")
sleep(2)
driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
sleep(2)
#driver.close()
#driver.quit()'''


# 2--> open two tab in new new window
'''driver.get("https://www.flipkart.com/")
sleep(2)
driver.switch_to.new_window('window') # it will open the new website in new window
driver.get("https://www.amazon.in/")
#driver.quit()   # it will close both window'''

#3--> open two tab in same window
'''driver.get("https://www.flipkart.com/")
sleep(2)
driver.switch_to.new_window('Tab')
driver.get("https://www.myntra.com/")'''


'''driver.get("https://www.amazon.com/")
sleep(2)
driver.switch_to.window(arg)
driver.get("https://www.flipkart.com/")'''




# Date-12 sept
#task -->1
#manually click on About Us, Contact Us, FAQs
#fetch tittle,  url, ID for Each


'''driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
sleep(10)
handles=driver.window_handles
driver.switch_to.window(handles[1])
tittle1 = driver.title
print("tittle of the about us : ",tittle1)
URL1 = driver.current_url
print("URL of the about us : ",URL1)
id1=driver.current_window_handle
print("Id of the about Us : ",id1)
handles1=driver.window_handles
driver.switch_to.window(handles1[2])
tittle2 = driver.title
print("tittle of the contact Us : ",tittle2)
URL2 = driver.current_url
print("URL of the contact us : ",URL2)
id2=driver.current_window_handle
print("Id of the contact Us : ",id2)
handles2 = driver.window_handles
driver.switch_to.window(handles2[1])
tittle3 = driver.title
print("tittle of the FAQs : ",tittle3)
URL3 = driver.current_url
print("URL of the FAQs : ",URL3)
id3=driver.current_window_handle
print("Id of the FAQs : ",id3)'''

# OR using Loop

'''driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(15)
all_window= driver.window_handles

for i in all_window:
    driver.switch_to.window(i)
    print("ID: ",driver.current_window_handle)
    print("Title: ",driver.title)
    print("URL: ",driver.current_url)
    print()'''


# task--2
# open a web page you like
#
#

'''driver.get("https://www.flipkart.com/")
sleep(15)
handle=driver.window_handles
driver.switch_to.window(handle[6])
print("Title: ",driver.title)'''








