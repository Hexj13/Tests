# coding=utf-8

import datetime
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from RootsLib.roots import *
from RootsLib.content import *


# noinspection PyUnusedLocal

class AccountsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'AccountsTesting' START" + TextColors.ENDC, flush=True)
	print("----------------------------------------", flush=True)
	print("----------------------------------------", flush=True)

	def setUp(self):
		print(TextColors.WARNING + "setUp START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Driver init
		self.driver = webdriver.Chrome()
		print("Webdriver ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Maximaze
		self.driver.maximize_window()
		print("Maximaze window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Заходим на сайт
		self.driver.get(site_url)
		print(
			"Get URL = " + TextColors.UNDERLINE + site_url + TextColors.ENDC + " ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "setUp END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def test_accounts(self):
		print(TextColors.WARNING + "test_accounts START" + TextColors.ENDC, flush=True)
		driver = self.driver
		print("Driver set ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		action = action_chains.ActionChains(driver)
		print("ActionChains set ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		wait = WebDriverWait(driver, 40)
		print("WebDriverWait set ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим логин
		search_element = driver.find_element_by_id(login_id)
		search_element.clear()
		search_element.send_keys(login_text)
		print("Enter login ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим пароль
		search_element = driver.find_element_by_id(password_id)
		search_element.send_keys(password_text)
		print("Enter password ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Войти
		search_element = driver.find_element_by_id(submit_button_id)
		search_element.click()
		print("Submit button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Юр. лица
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, entity_menu_button_xpath))).click()
		print("Account button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Вводим ИНН
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
		search_element.send_keys(inn)
		print("Enter INN ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку
		search_element = driver.find_element_by_id(get_data_by_INN_button_id).click()
		print("'Get data' button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем компанию
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, company_window_xpath.format(inn=inn)))).click()
		print("Choose company ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Берём ID документа
		url = driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		doc_id = params['id']
		print("Take document ID ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем email
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, email_input_xpath)))
		search_element.send_keys(email_text)
		print("Enter E-mail ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем site
		search_element = driver.find_element_by_xpath(site_input_xpath).send_keys(site_example_text)
		print("Enter Site ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем  phone
		search_element = driver.find_element_by_xpath(phone_input_xpath).send_keys(phone_text)
		print("Enter phone number ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# today date
		today = datetime.date.today()
		today_str = today.strftime("%d.%m.%Y")
		print("Take today date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# tomorrow date
		tomorrow = today + datetime.timedelta(days=1)
		tomorrow_str = tomorrow.strftime("%d.%m.%Y")
		print("Take tomorrow date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем дату диактивации
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath)))
		search_element.clear()
		search_element.send_keys(tomorrow_str)
		print("Enter deactivate date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем комментарий
		search_element = driver.find_element_by_xpath(comment_input_xpath).send_keys(comment_text)
		print("Enter description ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавляем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_tag_button_xpath))).click()
		print("Add Tag button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, selected_tag_xpath % account_tag_name))).click()
		action.send_keys(Keys.RETURN).perform()
		print("Choose tag----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Закрываем окно с тегами
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, close_window_button_xpath))).click()
		time.sleep(SleepSeconds.TWO)
		print("Close tag window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку Добавить Комментарий
		search_element = driver.find_element_by_xpath(add_comment_button_xpath).click()
		print("Add Comment button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле и вводим текст
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, comment_textarea_xpath))).click()
		action.send_keys(comment_text).perform()
		print("Enter comment----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Сохранить
		search_element = driver.find_element_by_xpath(save_comment_button_xpath).click()
		print("Save button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить Автивность
		search_element = driver.find_element_by_xpath(activity_add_button_xpath).click()
		print("Activity button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле Типа активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
		print("Activity type input find----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		activity_type_text_u = str(account_activity_type_text)
		search_element.send_keys(activity_type_text_u)
		print("Enter Activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % activity_type_text_u))).click()
		print("Choose activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.TWO)

		# TODO : Добавление парамов в ОБЩЕМ
		# # Переходим в Параметры
		# search_element = wait.until(
		# 	EC.element_to_be_clickable((By.XPATH, params_button_xpath))).click()
		# # Нажимаем на поле значения
		# search_element = wait.until(
		# 	EC.element_to_be_clickable((By.XPATH, empty_table_xpath))).click()
		# # Вводим в поле текст
		# params_text = str(params_text)
		# action.send_keys(params_text)
		# # Находим и нажимаем в списке нужный тип параметра
		# search_element = wait.until(
		# 	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % params_text))).click()

		# Нажимаем Структура
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, structure_button_xpath))).click()
		print("Structure button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Декод
		structure_name_u = str(structure_name)
		print("Structure name decode ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим название Структуры
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, structure_name_input_xpath))).send_keys(structure_name_u)
		print("Enter structure name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Ок
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		""""РЕКВИЗИТЫ"""
		print(TextColors.WARNING + "REQUISITES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Реквизиты
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, recvisits_button_xpath))).click()
		print("Requisites button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим ОКПО
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, okpo_input_xpath)))
		search_element.send_keys(okpo_text)
		print("Enter OKPO ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Сокращённое имя
		search_element = driver.find_element_by_xpath(foreign_short_name_input_xpath).send_keys(foreign_short_name_text)
		print("Enter foreign short name  ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Полное имя
		search_element = driver.find_element_by_xpath(foreign_name_input_xpath).send_keys(foreign_name_text)
		print("Enter foreign name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Enter по адресу
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, street_name_input_xpath)))
		search_element.send_keys(Keys.RETURN)
		print("Press ENTER on address ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем первый выпавший адрес для активации Google Maps
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, proposed_address_div_xpath)))
		search_element.click()
		print("Choose first address to activate Google Maps ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить вид активности
		search_element = driver.find_element_by_xpath(activity_type_button_xpath)
		search_element.click()
		print("Activity type button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим код активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, code_activity_type_input_xpath)))
		search_element.send_keys(activity_code)
		print("Enter activity code ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим имя активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, name_activity_type_input_xpath)))
		search_element.send_keys(activity_name_text)
		print("Enter activity name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим коммент
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, comment_input_xpath)))
		search_element.send_keys(comment_text)
		print("Enter comment ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "REQUISITES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""БАНКОВСКИЕ РЕКВИЗИТЫ"""
		print(TextColors.WARNING + "BANK REQUISITES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Добавить банковский реквизит
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_bank_button_xpath))).click()
		print("Add bank requisites button ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим БИК
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, bik_bank_xpath)))
		search_element.send_keys(bik_number_text)
		print("Enter BIK ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Имя банка
		search_element = driver.find_element_by_xpath(name_foreign_bank_xpath).send_keys(bank_name_text)
		print("Enter Bank Name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим ИНН
		search_element = driver.find_element_by_xpath(inn_bank_xpath).send_keys(inn_bank_text)
		print("Enter INN ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим КПП
		search_element = driver.find_element_by_xpath(kpp_bank_xpath).send_keys(kpp_bank_text)
		print("Enter KPP ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Р/с Банка
		search_element = driver.find_element_by_xpath(rs_bank_xpath).send_keys(rs_bank_text)
		print("Enter R/S ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Л/с Банка
		search_element = driver.find_element_by_xpath(ls_bank_xpath).send_keys(ls_bank_text)
		print("Enter L/S ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем Основной счёт
		search_element = driver.find_element_by_xpath(main_bank_xpath).click()
		print("Enter Main S ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим дату диактивации
		search_element = driver.find_element_by_xpath(deactivateDate_bank_xpath).send_keys(tomorrow_str)
		print("Enter deactivate date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим коммент
		search_element = driver.find_element_by_xpath(text_comment_bank_xpath).send_keys(comment_text)
		print("Enter comment ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем ОК
		search_element = driver.find_element_by_xpath(ok_button_window_xpath).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "BANK REQUISITES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОГОРОВЫ"""
		print(TextColors.WARNING + "CONTRACTS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Договоры в меню
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_button_xpath))).click()
		print("Contracts button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле Типа документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
		print("Document type input find ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		contract_type_name = str(contracts_type_name)
		search_element.send_keys(contract_type_name)
		print("Enter document type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % contract_type_name))).click()
		print("Choose type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем дату документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
		search_element.send_keys(today_str)
		search_element.send_keys(Keys.RETURN)
		print("Enter document date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.FIVE)
		# Закрываем договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("Close contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "CONTRACTS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ЗАКАЗЫ"""
		print(TextColors.WARNING + "ORDER START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Заказы в меню
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, orders_button_xpath))).click()
		print("Orders button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем дату документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
		search_element.send_keys(today_str)
		search_element.send_keys(Keys.RETURN)
		print("Enter document date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.FIVE)
		# Закрываем заказ
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("Close order ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "ORDER END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СЧЕТА"""
		print(TextColors.WARNING + "INVOICES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Счета в меню
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, accounts_button_xpath))).click()
		print("Invoices button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле Типа счёта
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, account_type_input_xpath)))
		print("Document type input find ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		account_type_name_u = str(account_type_name)
		search_element.send_keys(account_type_name_u)
		print("Enter document type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип счёта
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % account_type_name_u))).click()
		print("Choose document type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем на кнопку для выбора договора
		search_element = driver.find_element_by_xpath(account_doc_select_button_xpath).click()
		print("Select button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		#
		time.sleep(SleepSeconds.TWO)
		# Выбираем договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		action.send_keys(Keys.RETURN).perform()
		print("Choose contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем счёт
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("Invoices close ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "INVOICES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ПРОДАЖИ"""
		print(TextColors.WARNING + "OPPORTUNITIES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Продажи в меню
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, sales_button_xpath))).click()
		print("Opportunities button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле Типа продажи
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
		print("Document type input find ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		sales_type_name_u = str(sales_type_name)
		search_element.send_keys(sales_type_name_u)
		print("Enter document type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип продажи
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % sales_type_name_u))).click()
		print("Choose contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем продажи
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("Opportunities close ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "OPPORTUNITIES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СОГЛАСОВАНИЕ"""
		print(TextColors.WARNING + "APPROVALS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Согласование в меню
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, matching_button_xpath))).click()
		print("Approvals button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.FOUR)
		# Закрываем продажи
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("Approvals close ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "APPROVALS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		# Нажимаем Файлы
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, files_button_xpath))).click()
		print("Files button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажиаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_file_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавить Папку
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_folder_button_xpath))).click()
		print("Add folder button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Вводим название Папки
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, file_name_input_xpath))).send_keys(structure_name_u)
		print("Enter folder name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Ок
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_id_window_button_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE LINKS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete Contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Заказ
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, orders_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete Order ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Счёт
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, accounts_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete Invoices ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Продажу
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, sales_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete Opportunities ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Согласование
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, matching_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete Approval ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Прохоим в Общее
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, overall_button_xpath))).click()
		print("GO to General ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проходим в Сотрудники
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, employees_button_xpath))).click()
		print("GO to employees ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем сотрудника ссылающегося на док
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, employee_table_xpath))).click()
		print("Choose employees ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Удалить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		print("Delete click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем ОК
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Проходим в Структуру
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, structure_button_xpath))).click()
		print("GO to Structure ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем структуру ссылающегося на док
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, employee_table_xpath))).click()
		print("Choose Structure ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Удалить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		print("Delete click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем ОК
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "DELETE LINKS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Screen&Close"""
		print(TextColors.WARNING + "Delete&Screen&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Делаем скриншот
		scr_name = today_str + "_" + "docID" + "_" + doc_id + "_" + "accounts" + "_" + "testing" + ".png"
		driver.save_screenshot(r'C:\Users\Operator\Desktop\Testing\Tests\Screenshots\%s' % scr_name)
		time.sleep(SleepSeconds.TWO)
		print(
			"Screenshot with name = " + TextColors.BOLD + scr_name + TextColors.ENDC + " added ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		# Удаить договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_entity_button_xpath))).click()
		print("Delete document ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Enter
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("ENTER click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Screen&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_accounts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.driver.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'AccountsTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
