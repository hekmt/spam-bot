from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   
import time,sys,os

os.system("cls")

team = ("                                       This program by \u001b[31m@H.CZ_\u001b[0m")
for i in team:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.03)

print("")
print("")
#driver



#info
username= input("username :>> \u001b[34m")
password= getpass("\u001b[0mPassword :>> \u001b[31m")
user_report= input("\u001b[0mTarget :>> \u001b[33m")

#driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options = chrome_options)
#driver = webdriver.Chrome()


#login instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
#login user
try:
    user_int=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
    user_int.send_keys(username)
except :
    driver.refresh()
#login pass
try:
    pass_int=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
    pass_int.send_keys(password)
except:
    pass_int=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
    pass_int.send_keys(password)
#login click
try:
    login_butun=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
    time.sleep(5)
except:
    login_butun.click()
#going to user for report
driver.get(f"https://instagram.com/{user_report}")

num = 0
ii= 0





def spam():
    
    try:

        time.sleep(2)
        try:
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div/button").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div/div[2]/button").click()

        time.sleep(2)

        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/button[3]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div/div[2]/button").click()
        time.sleep(1.5)

        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div/div[2]/button").click()

        time.sleep(2)
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div[2]/button").click()
        except:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

        time.sleep(2)

        num ++ 1
    except:
        print(f"\u001b[31mspam flase :>>{num}\u001b[0m")
    else:
        ii ++ 1
        print(f"spam done :>> @{ii}")
    







while True:
    spam()



        
input("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
