# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_new_object(obj_xpath, web_driver):
	wait = WebDriverWait(web_driver, 60)
	search_element = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//div[text() = %s]" % obj_xpath)))
	search_element.click()
	time.sleep(2)
	search_element = wait.until(
		EC.element_to_be_clickable(
			(By.XPATH, ".//div[.='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
			           "ancestor::div[contains(@style,'display: none')])] ")))
	search_element.click()
