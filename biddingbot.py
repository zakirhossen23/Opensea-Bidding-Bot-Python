#!/usr/bin/env python3
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_extension("metamask.crx")
driver=webdriver.Chrome(options=options)
driver.switch_to.window(driver.window_handles["MetaMask"])

