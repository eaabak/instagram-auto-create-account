from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse

#writes registred accounts into "accounts.txt" file.
acc = open("accounts.txt", "a")
text = "qwertyuiopasdfghjklzxcvbnm1234567890"

#if you use firefox, change it to driver= webdriver.Firefox(executable_path=r"C:\Users\user\Downloads\Geckodriver.exe")

driver = webdriver.Chrome(r'C:\Users\user\Downloads\chromedriver.exe') #change it to your path.
driver.set_window_position(-10000,0) #hides the window, delete it if you don't need it.

ua = UserAgent()
userAgent = ua.random
print(userAgent)


driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(4)
try:
    cookie = driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
except:
    pass
name = account.username()

#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
fake_email = email.getFakeMail()
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
# Fill username value
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)
# Fill password value
# fixed the problem with wrong printed password
password_field = driver.find_element_by_name('password')
acc_password = account.generatePassword()
password_field.send_keys(acc_password)

#writes name + password into "accounts.txt" file.
print(name,acc_password, file=acc)

acc.close()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

time.sleep(8)

#Birthday verification
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
time.sleep(3)
#
fMail = fake_email[0].split("@")
mailName = fMail[0]
domain = fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)

#accepts the notifications.
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(4)

#logout from the account
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()

try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass
time.sleep(3)
driver.quit()
