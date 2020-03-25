from selenium import webdriver
import time
import os

from selenium.webdriver.common.keys import Keys


class stonkPrice:
    def __init__(self, whatStonk):
        self.driver = webdriver.Chrome()
        self.getStonk(whatStonk)
        self.getPriceHistory()

    def getStonk(self, whatStonk):
        self.driver.get("https://www.google.com/")
        searchBar = self.driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
        )

        searchBar.send_keys(whatStonk + " stock")
        searchBar.send_keys(Keys.RETURN)
        time.sleep(2)
        self.getPrice()

    def getPrice(self):
        try:
            price = self.driver.find_element_by_xpath(
                '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span[1]'
            )
            os.system("cls")
            print(whatStonk, "stonk price is:", price.text)
        except:
            print("try again lol")

    def getPriceHistory(self):
        self.driver.get("https://finance.yahoo.com/")
        searchBar = self.driver.find_element_by_xpath('//*[@id="yfin-usr-qry"]')
        searchBar.send_keys(whatStonk)
        searchBar.send_keys(Keys.RETURN)

        historicalData = self.driver.find_elements_by_name("Historical Data")
        print(historicalData)
        historicalData.click()


input()
os.system("cls")
whatStonk = input("what stonk would you like the price of: ")
stonk = stonkPrice(whatStonk)
