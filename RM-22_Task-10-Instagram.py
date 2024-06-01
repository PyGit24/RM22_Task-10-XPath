## Method-1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import os
import requests
paths= r"E:\PyCharm\chromedriver.exe"

## Importing Options
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

# ## Method-2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver=webdriver.Chrome()

## Get WebPage URL
driver.get("https://www.instagram.com/guviofficial/")
wait= WebDriverWait(driver,10)
time.sleep(3)

# Find the followers and following elements using explicit wait
follower_element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button")))
following_element= wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button")))

followers_count = follower_element.get_attribute("title")
following_element = following_element.text

print("Followers: ", followers_count)
print("Following: ", following_element)

driver.close()
driver.quit()