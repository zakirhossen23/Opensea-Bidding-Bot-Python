#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_extension("metamask.crx")
driver=webdriver.Chrome(options=options)
driver.switch_to.window(driver.window_handles[0])
driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
#emerge address target behave attitude idea sentence junk pause smoke assume juice

while True:
    try:
        driver.refresh()
        time.sleep(2)
        WebDriverWait(driver, 6).until(EC.element_to_be_clickable(By.XPATH,'//*[@placeholder="Paste Secret Recovery Phrase from clipboard"]'))
        driver.find_element(By.XPATH,'//*[@placeholder="Paste Secret Recovery Phrase from clipboard"]').send_keys("emerge address target behave attitude idea sentence junk pause smoke assume juice")
        break
    except:
        try:
            driver.find_element(By.XPATH, '//*[@placeholder="Paste Secret Recovery Phrase from clipboard"]').send_keys("emerge address target behave attitude idea sentence junk pause smoke assume juice")
            break
        except:pass
        driver.refresh()
        pass
driver.find_element(By.XPATH,'//form//*[@aria-labelledby="ftf-chk1-label"]').click()
driver.find_element(By.XPATH,'//form//*[@id="password"]').send_keys("zakir%%$")
driver.find_element(By.XPATH,'//input[@id="confirm-password"]').send_keys("zakir%%$")
driver.find_element(By.XPATH,'(//*[@role="checkbox"])[2]').click()
driver.find_element(By.XPATH,'(//*[@type="submit"])[1]').click()
while True:
    if "Congratulations" in driver.page_source:
        driver.find_element(By.XPATH,'//*[@role="button"]').click()
        break
while True:
    if "Secret Recovery Phrase" in driver.page_source:
        print("Login successful")
        break
driver.close()
driver.switch_to.window(driver.window_handles[0])

actions = ActionChains(driver)

driver.get("https://opensea.io/collection/cool-cats-nft?search[sortAscending]=true&search[sortBy]=PRICE")
time.sleep(2)
while True:
    try:
        image = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div/div[1]/article')
        image.click()
        if "assets" in driver.current_url:
            break
    except:pass

actions.move_to_element(driver.find_element(By.XPATH,"//div[@id='__next']/div/main/div/div/div/div[2]/div/div/div/section/div[2]/div[3]/div/div/button")).perform()

actions.move_to_element(driver.find_element(By.XPATH,"//div[@id='__next']/div/aside[2]/div[2]/div/div[2]/ul/li/button/div[2]")).perform()
driver.switch_to.window(driver.window_handles[1])
print("done")