from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 設定帳號密碼與商品網址
userName = ''
userPassword = ''
ticketUrl = ''

# 商品網址取得
driver = webdriver.Chrome('./chromedriver')
driver.get(ticketUrl)

# 等待網頁載入完成
time.sleep(5)

# 點選直接購買
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//div[@id="main"]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div[5]/div/div/button[2]').click()

# 等待網頁載入完成
time.sleep(10)

# 帳號密碼的登入
account = driver.find_element(By.NAME, "loginKey")
account.clear()
account.send_keys(userName)
password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys(userPassword)
driver.find_element(By.XPATH, "//div[@id=\'main\']/div/div[2]/div/div/div/div[2]/form/div/div[2]/button").click()

# 下面是跳轉後點選相關型號並結帳
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@id=\"main\"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button").click()
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@id=\"main\"]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[2]").click()
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@id=\"main\"]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[5]/div/div/button[2]").click()
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@id='main']/div/div[2]/div/div/div[3]/div[2]/div[6]/button[4]/span").click()
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//div[@id=\"main\"]/div/div[2]/div/div[2]/div[3]/div[2]/div[7]/button").click()




