from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import accountInfoGenerator as account


browser= webdriver.Chrome("your chrome driver path here")
browser.get("http://www.instagram.com/accounts/emailsignup/")
time.sleep(8) #time.sleep count can be changed depending on the Internet speed.
name = account.username()

#Fill the email value
email_field = browser.find_element_by_name('emailOrPhone')
email_field.send_keys(account.generatingEmail())
print(account.generatingEmail())

#Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)
#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys('aa12345bb12345cc'+name) #You can determine another password here.


WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))).click()

time.sleep(8)

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[3]").click()

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select"))).click()

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[12]").click()

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"))).click()

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[26]").click()


WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[6]"))).click()

#

print('Registering....')



