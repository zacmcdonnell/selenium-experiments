from selenium import webdriver
import time
import os

from selenium.webdriver.chrome.options import Options


WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


class jobChecker:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def navigate(self, link):
        self.driver.get(link)

    def displayJobs(self):
        jobdetails = self.driver.find_elements_by_class_name("fsize11")

        count = 0
        os.system("cls")
        print("-------------------\n")
        for i in jobdetails:
            print(i.text)
            count += 1
            if count == 5:
                print("-------------------\n")
                count = 0


jbhifi = jobChecker()

jbhifi.navigate("https://assets.jbhifi.com.au/jobs/qld/")
jbhifi.displayJobs()
