from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

time. sleep(5)
a = Workbook()
b = a.active

driver = webdriver.Chrome()
driver.get('https://iotvega.com/product')

productElements = driver.find_elements(By.CLASS_NAME, 'product-name')
priceElements = driver.find_elements(By.CLASS_NAME, 'price_item')

for product, price in zip(productElements, priceElements):
    product_name = product.text
    product_price = price.text
    b.append([product_name, product_price])

a.save('Products.xlsx')

driver.quit()
