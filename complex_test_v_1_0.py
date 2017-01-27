# coding=utf-8
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configs.complex_test_config import *

# Откроем Хром
driver = webdriver.Chrome()
driver.maximize_window()
# Добавляем action
action = action_chains.ActionChains(driver)
#
wait = WebDriverWait(driver, 20)
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
# Переходим в Договоры
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_xpath))).click()
# Находим и нажимаем "Добавить" новый договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
# Находим поле Типа документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_type_input_xpath)))
# Вводим в поле текст
contract_type_name = unicode(contracts_type_name.decode("utf-8"))
search_element.send_keys(contract_type_name)
# Находим и нажимаем в списке нужный тип документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % contract_type_name))).click()
# Проставляем дату документа
today = date.today()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
search_element.send_keys(str(today.strftime("%d.%m.%Y")))
search_element.send_keys(Keys.RETURN)
# Ждём пока не появятся комментарии. Служит обозначением, что внутреннее тестирование началось
search_element = wait.until(
	EC.visibility_of_any_elements_located((By.ID, comment_div_id)))
# Переходим в раздел с переданным значением
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_file_button_xpath))).click()
# Нажимаем клавишу Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
# Нажимаем на клавишу По шаблону
search_element = wait.until(
	EC.visibility_of_element_located((By.XPATH, contracts_template_xpath)))
search_element.click()
# Выбераем шаблон
search_element = wait.until(
	EC.visibility_of_element_located((By.XPATH, create_template_xpath)))
search_element.click()
# Закрыть Хром
time.sleep(sleep_time)
driver.close()
