# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


# Открыть Chrome browser
@given('Chrome')
def step(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()


# Открыть Firefox browser
@given('Firefox')
def step(self):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()


# Передать url
@given('url = "{url}"')
def step(self, url):
    self.driver.get('%s' % url)


# Найти элемент по id
@then('find element with id = "{id_element}"')
def step(self, id_element):
    self.search_element = self.driver.find_element_by_id('%s' % id_element)


# Найти элемент по name
@then('find element with name = "{name_element}"')
def step(self, name_element):
    self.search_element = self.driver.find_element_by_neme('%s' % name_element)


# Найти элемент по link_text
@then('find element with link_text = "{link_text_element}"')
def step(self, link_text_element):
    self.search_element = self.driver.find_element_by_link_text('%s' % link_text_element)


# Найти элемент по partial_link_text
@then('find element with partial_link_text = "{partial_link_text}"')
def step(self, partial_link_text):
    self.search_element = self.driver.find_element_by_partial_link_text('%s' % partial_link_text)


# Найти элемент по tag_name
@then('find element with tag_name = "{tag_name}"')
def step(self, tag_name):
    self.search_element = self.driver.find_element_by_tag_name('%s' % tag_name)


# Найти элемент по class_name
@then('find element with class_name = "{class_name}"')
def step(self, class_name):
    self.search_element = self.driver.find_element_by_class_name('%s' % class_name)


# Найти элемент по css_selector
@then('find element with css_selector = "{css_selector}"')
def step(self, css_selector):
    self.search_element = self.driver.find_element_by_css_selector('%s' % css_selector)


# Найти элемент по css_selector
@then('find element with xpath = "{xpath}"')
def step(self, xpath):
    self.search_element = self.driver.find_element_by_xpath("" % xpath)


# Клик по элементу
@then('click')
def step(self):
    self.search_element.click()


# Очистка поля
@then('clear')
def step(self):
    self.search_element.clear()


# Подождать
@then('wait = "{wait_time}"')
def step(self, wait_time):
    self.driver.implicitly_wait("%s" % wait_time)


# Ввод данных
@then('enter the text/num = "{value}"')
def step(self, value):
    self.search_element.send_keys("%s" % value)


# Нажатие клавиши
@then('press key with value = "{value}"')
def step(self, value):
    self.search_element.send_keys(value)
