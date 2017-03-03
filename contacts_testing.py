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
class ContactsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ContactsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_contacts(self):
		print(TextColors.WARNING + "test_activities START" + TextColors.ENDC, flush=True)
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
		# Находим в меню Физ. лица
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contacts_menu_button_xpath))).click()
		print("Contacts button menu click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Today date
		today = datetime.date.today()
		today_str = today.strftime("%d.%m.%Y")
		print("Take today date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Tomorrow date
		tomorrow = today + datetime.timedelta(days=1)
		tomorrow_str = tomorrow.strftime("%d.%m.%Y")
		print("Take tomorrow date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Birthday date
		birthday = today - datetime.timedelta(days=2)
		birthday_str = birthday.strftime("%d.%m.%Y")
		print(
			"Enter birthday" + TextColors.BOLD + "(TODAY + 2)" + TextColors.ENDC + "----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Name
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, name_input_xpath)))
		name_text_u = str(name_text)
		search_element.send_keys(name_text_u)
		time.sleep(SleepSeconds.ONE)
		print("Enter Name ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Surname
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, surname_input_xpath)))
		surname_text_u = str(surname_text)
		search_element.send_keys(surname_text_u)
		time.sleep(SleepSeconds.ONE)
		print("Enter Surname ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Patronymic
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, patronymic_input_xpath)))
		patronymic_text_u = str(patronymic_text)
		search_element.send_keys(patronymic_text_u)
		print("Enter Patronymic ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Phone
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, phone_input_xpath)))
		search_element.send_keys(phone_text)
		print("Enter Phone ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Email
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, email_input_xpath)))
		search_element.send_keys(email_text)
		print("Enter Email ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем пол
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, gender_div_xpath))).click()
		gender_text_u = str(gender_text)
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % gender_text_u))).click()
		time.sleep(SleepSeconds.ONE)
		print("Choose sex ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем Описание
		comment_text_u = str(comment_text)
		search_element = driver.find_element_by_xpath(text_comment_bank_xpath).send_keys(comment_text_u)
		print("Enter description ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавляем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_tag_button_xpath))).click()
		print("'Add Tag' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, selected_tag_xpath % contact_tag_name))).click()
		action.send_keys(Keys.RETURN).perform()
		print("Choose tag ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Закрываем окно с тегами
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, close_window_button_xpath))).click()
		time.sleep(SleepSeconds.TWO)
		print("Close window with tags ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку Добавить Комментарий
		search_element = driver.find_element_by_xpath(add_comment_button_xpath).click()
		print("'Add comment' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле и вводим текст
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, comment_textarea_xpath))).click()
		action.send_keys(comment_text_u).perform()
		print("Find input & enter text ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Сохранить
		search_element = driver.find_element_by_xpath(save_comment_button_xpath).click()
		print("'Save' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить Автивность
		search_element = driver.find_element_by_xpath(activity_add_button_xpath).click()
		print("'Add activity' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле Типа активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
		print("Find input ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		activity_type_text_u = str(activity_contact_type_text)
		search_element.send_keys(activity_type_text_u)
		print("Enter activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % activity_type_text_u))).click()
		time.sleep(SleepSeconds.ONE)
		print("Choose activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Должности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, position_button_xpath))).click()
		print("'Position' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("'Add' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку выбора Компании
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, company_choose_button_xpath))).click()
		print("'Choose company' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем Юр. Лицо
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, flexbby_contragent_add_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		action.send_keys(Keys.RETURN).perform()
		print("Choose account ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку выбора Должности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, position_choose_button_xpath))).click()
		print("'Choose position' button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем Должность
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, director_contragent_add_xpath))).click()
		time.sleep(SleepSeconds.TWO)
		action.send_keys(Keys.RETURN).perform()
		print("Choose position ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем ОК
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_id_window_button_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Берём ID документа
		url = driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		doc_id = params['id']
		print("Take document ID ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОПОЛНИТЕЛЬНО"""
		print(TextColors.WARNING + "ADDITIONALLY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Дополнительно
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, additionally_button_xpath))).click()
		print("Additionally button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим День Рождения
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, birthday_input_xpath))).send_keys(birthday_str)
		print("Enter br-day date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим ИНН
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
		search_element.send_keys(inn_text)
		print("Enter INN ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим СНИЛС
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, snils_input_xpath)))
		search_element.send_keys(snils_text)
		print("Enter SNILS ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Диактивацию
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath)))
		search_element.send_keys(tomorrow_str)
		print("Enter deactivate date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавить Документ
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_buton_doc_xpath)))
		search_element.click()
		time.sleep(SleepSeconds.TWO)
		print("Add document button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		"""КОСТЫЛЬ начался"""  # TODO: после исправления баги с полями в физ.лице нужно будет это всё переделать!
		# Вводим Описание
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, comment_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(comment_input_xpath).send_keys(comment_text_u)
		print("Enter description  ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Серию
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, series_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(series_input_xpath).send_keys(series_text)
		print("Enter serial number----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Номер
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, number_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(number_input_xpath).send_keys(number_text)
		print("Enter number ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим дату выдачи паспорта
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, deliveryDate_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(deliveryDate_input_xpath).send_keys(today_str)
		print("Enter delivery date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим дату истечения паспорта
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, expired_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(expired_input_xpath).send_keys(tomorrow_str)
		print("Enter expired date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Кто Выдал
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, issuer_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(issuer_input_xpath).send_keys(issuer_text)
		print("Enter WHO issuer ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Номер Кто Выдал
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, issuerCode_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_xpath(issuerCode_input_xpath).send_keys(issuerCode_text)
		print("Enter issuer code ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		"""КОСТЫЛЬ закончился"""
		# Добавить Адрес
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_buton_adrr_xpath)))
		search_element.click()
		time.sleep(SleepSeconds.ONE)
		#
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, street_name_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		adrr_text_u = str(adrr_text)
		search_element = driver.find_element_by_xpath(street_name_input_xpath).send_keys(adrr_text_u)
		search_element = driver.find_element_by_xpath(street_name_input_xpath).send_keys(Keys.RETURN)
		time.sleep(SleepSeconds.ONE)
		print("Enter addr ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем первый выпавший адрес для активации Google Maps
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, proposed_address_div_xpath)))
		search_element.click()
		print("Google Maps activate ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "ADDITIONALLY END" + TextColors.ENDC, flush=True)
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
			EC.element_to_be_clickable((By.XPATH, file_name_input_xpath))).send_keys(comment_text)
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
		print("", flush=True)
		print(TextColors.WARNING + "DELETE LINKS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Screen&Close"""
		print(TextColors.WARNING + "Delete&Screen&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Делаем скриншот
		scr_name = today_str + "_" + "docID" + "_" + doc_id + "_" + "contacts" + "_" + "testing" + ".png"
		driver.save_screenshot(r'C:\Users\Operator\Desktop\Testing\Tests\Screenshots\%s' % scr_name)
		print(
			"Screenshot with name = " + TextColors.BOLD + scr_name + TextColors.ENDC + " added ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		time.sleep(SleepSeconds.TWO)
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
		print(TextColors.WARNING + "test_contacts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		# Sleep
		time.sleep(SleepSeconds.FIVE)

	def tearDown(self):
		self.driver.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ContactsTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
