'''from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://www.flipkart.com/')
size_before=driver.get_window_size()
print("size_before", size_before)
sleep(5)
driver.maximize_window()
size_after=driver.get_window_size()
print("size_after", size_after)
sleep(3)
driver.fullscreen_window()
size_after_full=driver.get_window_size()
print("size_after_full", size_after_full)'''

'''driver.get('https://chat.qspiders.com/')
sleep(2)
position_before=driver.get_window_position()
print("position_before", position_before)
driver.maximize_window()
position_after=driver.get_window_position()
print("position_after", position_after)
sleep(2)
driver.fullscreen_window()
pos_after_full=driver.get_window_position()
print("pos_after_full", pos_after_full)'''



'''driver.get('https://amazon.in')
before=driver.get_window_rect()
print("before", before)
sleep(2)
driver.maximize_window()
after=driver.get_window_rect()
print("after", after)
sleep(2)
driver.fullscreen_window()
after_full=driver.get_window_rect()
print("after_full", after_full)'''



'''from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://www.flipkart.com/')
before_size=driver.get_window_size()
print("before_size", before_size)
before_pos=driver.get_window_position()
print("before_pos", before_pos)
before_rect=driver.get_window_rect()
print("before_rect", before_rect)
sleep(2)
driver.maximize_window()
after_max_size=driver.get_window_size()
print("after_max_size", after_max_size)
after_pos=driver.get_window_position()
print("after_pos", after_pos)
after_rect=driver.get_window_rect()
print("after_rect", after_rect)
sleep(2)
driver.fullscreen_window()
after_full_scr=driver.get_window_rect()
print("after_full_scr", after_full_scr)
'''
'''from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)'''
'''driver.get('https://www.amazon.in/')
sleep(5)
driver.maximize_window()
size=driver.get_window_size()
print("size", size)
position=driver.get_window_position()
print("position", position)
sleep(5)
driver.set_window_size(600,600)
driver.set_window_position(70,70)'''


#Task date -->11 sept



'''import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
dropdowns=driver.find_elements("tag name","select")
print(len(dropdowns))
country_dropdown=driver.find_element("id","country")
ob=Select(country_dropdown)
#count no of options
list_options=ob.options
print(len(list_options))
#print all the options
for i in list_options:
    print(i.text)
#select perticuler option
ob.select_by_value("germany")
#or
ob.select_by_index(3)
#or
ob.select_by_visible_text("Germany")
time.sleep(3)'''
