#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by kereh

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class missCall():
    def __init__(self, nomor_hp):
        self.nomor_hp = nomor_hp
        self.path = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.url = "https://www.citcall.com/demo/"

    def tutup_driver(self):
        self.driver.quit()

    def mainProgram(self):
        self.driver.get(self.url)
        self.hp = self.driver.find_element_by_xpath(
            "//input[@id='cellNo']"
        )
        self.hp.send_keys(self.nomor_hp)
        self.click_button = self.driver.find_element_by_xpath(
            "//div[@class='container']//div[@class='row']//div[@class='col-sm-4 col-md-4 col-md-offset-4']//div[@class='account-wall']//button[@id='btnSend']"
        )
        self.click_button.click()
        try:
            self.verify = self.driver.find_element_by_xpath(
                "//button[@id='btnMisscall']"
            )
            self.verify.click()
            print("Send misscall success")
        except:
            print("We Have A Problem Sorry")


if __name__ == "__main__":
    inputUser = input("nomor telp : ")
    miss = missCall(inputUser)
    miss.mainProgram()
