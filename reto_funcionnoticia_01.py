import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def word_to_search(word):
    search= driver.find_element(By.XPATH,"//input[contains(@data-testid,'search-input')]" )
    search.send_keys(word + Keys.ENTER)


def sort_by(number1):
    filter_sort_by= driver.find_element(By.XPATH, "//select[@data-testid='SearchForm-sortBy']")
    filter_sort_by.click()
    filter_option= driver.find_elements(By.XPATH,"//select[@data-testid='SearchForm-sortBy']/option")[number1]
    filter_option.click()


def news(number):
    text_port = driver.find_elements(By.XPATH, "//h4[@class='css-2fgx4k']")[0:number]
    print(len(text_port))
    for title in text_port:
        title = title.text
        print(title)


def filters(d1,d2,d3):
    date_range= driver.find_element(By.XPATH, "//button[@class='css-p5555t']")
    date_range.click()
    date_option= driver.find_elements(By.XPATH,"//li/button[@class='css-jba1a6 selected' or @class='css-jba1a6']")[d1]
    date_option.click()
    section = driver.find_element(By.XPATH, "//div[@data-testid='section']//button[@class='css-4d08fs']")
    section.click()
    section_option = driver.find_elements(By.XPATH, "//li[@class='css-1qtb2wd']//input [@type='checkbox']")[d2]
    section_option.click()
    type = driver.find_element(By.XPATH, "//div[@data-testid='type']//button[@class='css-4d08fs']")
    type.click()
    type_option = driver.find_elements(By.XPATH, "//div[@class='css-tw4vmx']//li[@class='css-1qtb2wd']//input [@type='checkbox']")[d3]
    type_option.click()



#search=driver.find_element(By.XPATH,"//input[contains(@data-testid,'search-input')]")
#search.send_keys("murder" + Keys.ENTER)
#time.sleep(3)

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/")
driver.maximize_window()
t=2

time.sleep(t)
element=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-testid='search-button']")))
element.click()
time.sleep(t)


word= "revenue"
word_to_search(word)
time.sleep(t)

number=8
news(number)
time.sleep(t)


number1= 2
sort_by(number1)
time.sleep(t)

d1=2
d2=6
d3=5
filters(d1,d2,d3)
time.sleep(t)

number=5
news(number)
time.sleep(t)


driver.quit()