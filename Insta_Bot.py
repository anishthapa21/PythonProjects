#Using Selenium with Python to automate and like all the post of a given profile.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


s = Service("D:/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options = options, service = s)

#Input a website to start
driver.get("https://www.instagram.com/")
time.sleep(3)

#Providing Username and Password
username = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input""")
username.send_keys("playersbuzz")

password = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input""")
password.send_keys("Club@Softwarica@007")
password.send_keys(Keys.ENTER)
time.sleep(3)

#Input a channel name to search
search_btn = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]""")
search_btn.click()

search_term = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input""")
search_term.send_keys("goatairjordan")
time.sleep(3)

#Clicking on the first appeared Result
click_result = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div""")
click_result.click()
time.sleep(3)

#Like first post
click_post = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a""")
click_post.click()
time.sleep(2)
click_btn = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div""")
click_btn.click()
time.sleep(3)
click_next_post = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button""")
click_next_post.click()

#Using loop to like all posts 
for i in range(2, 10):
#Get to Next Post
    click_next_posts = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button""")
    click_next_posts.click()
    click_btn = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div""")
    click_btn.click()
    time.sleep(3)




