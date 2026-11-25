# to execute a function , function calling is mandatory.

'''def add():
    a=20
    b=30
    sum=a+b
    print(sum)
add()
'''

'''class Demo:
    def Login(self):
        print('login executing....')
    def Logout(self):
        print('logout executing....')
obj=Demo()
obj.Login()
obj.Logout()
'''


'''class Cal:
    a=30
    b=20
    def add(self):
        sum=self.a + self.b
        print(sum)
    def sub(self):
        subt=self.a-self.b
        print(subt)
    def mul(self):
        mult=self.a*self.b
        print(mult)
    def div(self):
        div=self.a/self.b
        print(div)
obj=Cal()
obj.add()
obj.sub()
obj.mul()
obj.div()
'''

# assertion
# if condn. is not satisfy it moves to next line
# assert condn. is not satisfy, it stop execution
'''a=10
b=20
if a>b:    #it will check the condn. if true it goes inside, else move to next line.
    print(a)
print('seccessfull')'''

'''a=10
b=20
assert a>b,'failed'  # it will check the condn. if it is satisfy , it wove to next line
                    # else stop the whole execution , don't move to next line
print('succesful')'''


# WAP to check the number is positive or not.
'''a=int(input('enter first number'))
assert a>0,'Negative'
print('positive')'''

#WAP to check python is in sentence or not.
'''word=input('enter the sentence')
assert 'python' in word.split(),'not found'
print('found')'''

#Code using assertion
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

'''driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[text()="Mobiles"]').click()

assert 'Mobile' in driver.title
print('found Mobile in tittle')
assert 'mobiles' in driver.current_url
print('found mobiles in url')
'''
