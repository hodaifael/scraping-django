from django.shortcuts import render
from .models import Product
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getproduct(request):
    PATH = "C:\Program Files\chromedriver.exe"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.get("https://www.aliexpress.com/")
    search = driver.find_element_by_name("SearchText")
    search.send_keys("PC Portable")
    search.send_keys(Keys.RETURN)
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "right-menu"))
        )
        articles = main.find_elements_by_class_name("list-item")
        list = []  
        for article in articles:
            prix=article.find_elements_by_class_name("price-current")
            for p in prix:
                p1=p.text
            nom=article.find_elements_by_class_name("item-title")
            for n in nom:
                n1=n.text
            list.append( Product(n1, str(p1)) )
    finally:
        driver.quit()

    return  render(request, "index.html", locals())    

def getproductamazon(request):
    PATH = "C:\Program Files\chromedriver.exe"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.get("https://www.gamestop.com/")
    search = driver.find_element_by_name("q")
    search.send_keys("PC Portable")
    search.send_keys(Keys.RETURN)
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid-wrapper"))
        )
        articles = main.find_elements_by_class_name("product-grid-tile-wrapper")
        list = []  
        for article in articles:
            prix=article.find_elements_by_class_name("variant-price")
            for p in prix:
                p1=p.text
            nom=article.find_elements_by_class_name("link-name")
            for n in nom:
                n1=n.text
            list.append( Product(n1, str(p1)) )
    finally:
        driver.quit()
    
    return  render(request, "amazon.html", locals())        