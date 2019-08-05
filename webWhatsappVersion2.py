from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


with open('whatsappPhone.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        driver = webdriver.Chrome()
        driver.implicitly_wait(505) # seconds
        #open tab
        driver.get('https://web.whatsapp.com/send?phone='+row[0]+'&text='+row[1])
        driver.implicitly_wait(505) # seconds
        driver.find_element_by_class_name('_3M-N-').send_keys(Keys.ENTER) 
        driver.implicitly_wait(505) # seconds
        driver.close()

csvFile.close()
