# coding:utf-8
import unittest
import os
import sys
import logging
import logging.config
import time
from appium import webdriver
from selenium import webdriver
def appP():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['udid'] = '6T7HNZPJDQHQUGFA'
    desired_caps['app'] = 'C:\Program Files (x86)\Appium\\node_modules\.bin\Vbox_Phone_3.5.2.753_xianwang.apk'
    desired_caps['appPackage'] = 'com.linglong.android'
    desired_caps['appActivity'] = 'com.linglong.android.StartActivity'
    desired_caps['autoLaunch'] = True
    desired_caps['resetKeyboard'] = False
    desired_caps['noReset'] = False
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.implicitly_wait(30)
    time.sleep(10)

    driver.find_element_by_id("com.linglong.android:id/tvJDLogin").click()

    username = driver.find_element_by_id("com.linglong.android:id/phone_number")
    username.click()
    username.send_keys("16602611929")

    password = driver.find_element_by_id('com.linglong.android:id/user_password')
    password.click()
    password.send_keys("qaz123qwe")

    driver.find_element_by_id('com.linglong.android:id/login_but').click()

    # time.sleep(25)
    # driver.find_element_by_id('com.linglong.android:id / update_yes_btn').click()
    #
    # driver.find_element_by_id('com.linglong.android:id/vbox_vbox_setting').click()
    time.sleep(15)

    driver.quit()

# if __name__ == '__main__':
#
#     for i in range(3):
#         appP()