import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Searcher:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = "//input[contains(@data-testid,'search-input')]"
        self.icon_search = "//button[@data-testid='search-button']"
        self.go_button = "//button[@data-testid= 'search-submit']"

    def open_search_box(self):
        button_el = self.driver.find_element(By.XPATH, self.icon_search)
        button_el.click()

    def type_in_search_input(self, text_to_search):
        box_input = self.driver.find_element(By.XPATH, self.search_input)
        box_input.send_keys(text_to_search)

    def perform_search(self):
        go_click = self.driver.find_element(By.XPATH, self.go_button)
        go_click.click()


class Filters:

    def __init__(self, driver):
        self.driver = driver
        self.date_range = "//button[@class='css-p5555t']"
        self.section = "//div[@data-testid='section']//button[@class='css-4d08fs']"
        self.type = "//div[@data-testid='type']//button[@class='css-4d08fs']"
        self.sort_by = "//select[@data-testid='SearchForm-sortBy']"
        #self.example = "//button[contains(@value, '{date_range_option}')]"

    def open_date_range_filter(self):
        date_range_button = self.driver.find_element(By.XPATH, self.date_range)
        date_range_button.click()

    def choose_date_range_option(self, date_range_option):
        date_range_op = self.driver.find_element(By.XPATH, f"//button[contains(@value, '{date_range_option}')]")
        #self.example.format(date_range_option=date_range_option)
        date_range_op.click()

    def open_section_filter(self):
        section_button = self.driver.find_element(By.XPATH, self.section)
        section_button.click()

    def choose_section_option(self, section_option):
        section_op = self.driver.find_element(By.XPATH, f"//input[contains(@value, '{section_option}')]")
        section_op.click()

    def open_type_filter(self):
        type_button = self.driver.find_element(By.XPATH, self.type)
        type_button.click()

    def choose_type_option(self, type_option):
        type_op = self.driver.find_element(By.XPATH, f"//input[contains(@value, '{type_option}')]")
        type_op.click()

    def open_sort_by(self):
        sort_by_button = self.driver.find_element(By.XPATH, self.sort_by)
        sort_by_button.click()

    def choose_sort_by_option(self, sort_by_option):
        sort_by_op = self.driver.find_element(By.XPATH, f"//option[contains(@value, '{sort_by_option}')]")
        sort_by_op.click()


class News:

    def __init__(self,driver):
        self.driver = driver
        self.tittle = "//h4[@class='css-2fgx4k']"
