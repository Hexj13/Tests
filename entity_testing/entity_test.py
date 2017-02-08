# coding=utf-8

import datetime
import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
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

""""ОБЩЕЕ"""
# Вводим ИНН
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
search_element.send_keys(inn)
# Нажимаем кнопку
search_element = driver.find_element_by_id(get_data_id).click()
# Выбираем компанию
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, company_window_xpath.format(inn=inn)))).click()
# Берём ID документа
url = driver.current_url
hash_tag = url[url.find('#') + 1:]
params = dict(x.split('=') for x in hash_tag.split('&'))
doc_id = params['id']
# Проставляем email
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, email_input_xpath)))
search_element.send_keys(email_text)
# Проставляем site
search_element = driver.find_element_by_xpath(site_input_xpath).send_keys(site_example_text)
# Проставляем  phone
search_element = driver.find_element_by_xpath(phone_input_xpath).send_keys(phone_text)
# today date
today = datetime.date.today()
today_str = today.strftime("%d.%m.%Y")
# tomorrow date
tomorrow = today + datetime.timedelta(days=1)
tomorrow_str = tomorrow.strftime("%d.%m.%Y")
# Проставляем дату диактивации
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath)))
search_element.clear()
search_element.send_keys(tomorrow_str)
# Проставляем комментарий
search_element = driver.find_element_by_xpath(comment_input_xpath).send_keys(comment_text)

""""РЕКВИЗИТЫ"""
# Нажимаем Реквизиты
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, recvisits_button_xpath))).click()
# Вводим ОКПО
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, okpo_input_xpath)))
search_element.send_keys(okpo_text)
# Вводим Сокращённое имя
search_element = driver.find_element_by_xpath(foreign_short_name_input_xpath).send_keys(foreign_short_name_text)
# Вводим Полное имя
search_element = driver.find_element_by_xpath(foreign_name_input_xpath).send_keys(foreign_name_text)
# Enter по адресу
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, street_name_input_xpath)))
search_element.send_keys(Keys.RETURN)
# Выбираем первый выпавший адрес для активации Google Maps
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, proposed_address_div_xpath)))
search_element.click()
# Спим
time.sleep(two_sec)
# Нажимаем Добавить вид активности
search_element = driver.find_element_by_xpath(activity_type_button_xpath)
search_element.click()
# Вводим код активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, code_activity_type_input_xpath)))
search_element.send_keys(activity_code)
# Вводим имя активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, name_activity_type_input_xpath)))
search_element.send_keys(activity_name_text)
# Вводим коммент
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, comment_input_xpath)))
search_element.send_keys(comment_text)

"""Удаление ссылок"""
# Прохоим в Общее
search_element = driver.find_element_by_xpath(overall_button_xpath).click()
# Проходим в Сотрудники
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employees_button_xpath))).click()

"""Delete&Screen&Close"""
# Делаем скриншот
scr_name = today_str + "_" + "docID" + doc_id + "_" + "entity" + "_" + "test" + ".jpeg"
driver.save_screenshot('C:\Users\Operator\Desktop\Testing\Tests\screens\\%s' % scr_name)
time.sleep(ten_sec)
# Удаить договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
# Нажимаем Enter
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_delete_button_xpath))).click()
# Закрыть Хром
time.sleep(two_sec)
driver.close()
