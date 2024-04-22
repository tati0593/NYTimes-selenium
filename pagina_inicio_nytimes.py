import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from class_nytimes import Searcher
from class_nytimes import Filters


t=2

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/")
driver.maximize_window()
time.sleep(t)

search_screen = Searcher(driver)
search_screen.open_search_box()
search_screen.type_in_search_input("murder")
search_screen.perform_search()

time.sleep(t)

search_by_filter = Filters(driver)
search_by_filter.open_date_range_filter()
time.sleep(t)
search_by_filter.choose_date_range_option("Past Week")

search_by_filter.open_section_filter()
time.sleep(t)
search_by_filter.choose_section_option("Arts")

search_by_filter.open_type_filter()
time.sleep(t)
search_by_filter.choose_type_option("article")

search_by_filter.open_sort_by()
time.sleep(t)
search_by_filter.choose_sort_by_option("oldest")


time.sleep(5)


driver.quit()