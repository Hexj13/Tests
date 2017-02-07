# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from elements_config import *
from content_config import *

# Устанавливаем драйвер
driver = webdriver.Chrome()
# Максимайз
driver.maximize_window()
# Устанавливаем экшен
action = action_chains.ActionChains(driver)
# Установим тайм для драйвера
wait = WebDriverWait(driver, 10)
# Заходим на сайт
driver.get(site_url)
# Вводим логин
search_element = driver.find_element_by_id(login_id)
search_element.clear()
search_element.send_keys(login_text)
# Вводим пароль
search_element = driver.find_element_by_id(password_id)
search_element.send_keys(password_text)
# Нажимаем Войти
search_element = driver.find_element_by_id(submit_button_id)
search_element.click()
# Проваливаемся на сайт
time.sleep(two_sec)
# Находим в меню Юр. лица
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, entity_menu_button_xpath))).click()
# Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Вводим ИНН
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
search_element.send_keys(inn)
# Нажимаем кнопку
search_element = wait.until(
	EC.element_to_be_clickable((By.ID, get_data_id))).click()
# Выбираем компанию
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, company_window_xpath.format(inn=inn)))).click()
#

"""Delete&Close"""
time.sleep(ten_sec)
# Удаить договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
# Нажимаем Enter
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_delete_button_xpath))).click()
# Закрыть Хром
time.sleep(ten_sec)
driver.close()
