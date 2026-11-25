#Task-->1
#--> Open Chrome browser
#--> Open a webpage u like


'''
from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
driver.get('https://amazon.in/')
sleep(5)
'''

#task-->2
#--> Open Chrome browser
#--> Use ChromeOptions to do browser setting
#--> Open a webpage u like

'''
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://chat.qspiders.com/')'''

#Task-->3
#--> Open Chrome browser
#--> Use ChromeOptions to do browser setting
#--> Open a webpage u like
#--> Maximize

'''from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://chat.qspiders.com/')
driver.maximize_window()'''

#Task-->4
#--> Open Edge browser
#--> Use EdgeOptions to do browser setting
#--> Open a webpage u like
#--> Maximize
#--> Open another webpage
#--> Minimize

'''from time import sleep
from selenium.webdriver import Edge,EdgeOptions
o=EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
driver.get('https://www.irctc.co.in/')
driver.maximize_window()
sleep(3)
driver.get('https://chat.qspiders.com/')
sleep(5)
driver.minimize_window()'''


#Task-->5
'''from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://flipkart.com/')  # first launch the web page
driver.maximize_window()             # maximize it in full screen
sleep(5)                             # wait for 5 second
#driver.minimize_window()
driver.fullscreen_window()           # do full screen to the website
sleep(3)                             # wait for 3 second
driver.minimize_window()             # minimize the window-->applocation show in your TaskBar
'''
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


#get window size method
'''
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://www.nike.in')
size_before=driver.get_window_size()
print("size_before", size_before)
sleep(5)
driver.maximize_window()
size_after=driver.get_window_size()
print("size_after", size_after)
'''



#get window position

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


#get window rect
'''
driver.get('https://amazon.in')
before=driver.get_window_rect()
print("before", before)
sleep(2)
driver.maximize_window()
after=driver.get_window_rect()
print("after", after)
sleep(2)
driver.fullscreen_window()
after_full=driver.get_window_rect()
print("after_full", after_full)
'''

#Date-9Sept
#Task-->1
'''driver.get('https://www.flipkart.com/')
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
sleep(2)'''



#set window size
'''driver.get('https://chat.qspiders.com/')
sleep(5)
driver.set_window_size(1000,1080)'''

#set window position
'''driver.get('https://amazon.in/')
sleep(2)
driver.set_window_position(2,15)'''

#set window rect
'''driver.get('https://www.amazon.in/')
sleep(5)
driver.set_window_rect(50,50,1080,400)'''


#task-->2
# open a web page you like
# maximize
#get the size and position
# change the position to 70,70
# change the size to 600,600


'''driver.get('https://www.amazon.in/')
sleep(5)
driver.maximize_window()
size=driver.get_window_size()
print("size", size)
position=driver.get_window_position()
print("position", position)
sleep(5)
driver.set_window_size(600,600)
driver.set_window_position(70,70)
'''







