# coding=utf-8
import time
import unittest
from datetime import date

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from RootsLib.roots import *
from RootsLib.content import *


# noinspection PyUnusedLocal
class ComplexTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ComplexTesting' START" + TextColors.ENDC, flush=True)
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

	def test_complex(self):
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
		# Переходим в Договоры
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_main_menu_button_xpath))).click()
		print("Contracts button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем "Добавить"
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
		print("Contract input find ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим в поле текст
		contract_type_name = str(complex_contracts_type_name)
		search_element.send_keys(contract_type_name)
		print("Enter contract type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % contract_type_name))).click()
		print("Choose contract type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем дату документа
		today = date.today()
		today = today.strftime("%d.%m.%Y")
		print("Take today date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
		search_element.send_keys(str(today))
		search_element.send_keys(Keys.RETURN)
		print("Enter document date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Ждём пока не появятся комментарии. Служит обозначением, что внутреннее тестирование началось
		search_element = wait.until(
			EC.visibility_of_any_elements_located((By.ID, comment_div_id)))
		print("Wait comment ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.TWO)
		# Отправляем на согласование
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, to_matching_button_xpath))).click()
		time.sleep(SleepSeconds.TWO)
		# Берём ID документа
		url = driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		doc_id = params['id']
		print("Take document ID ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# ID документа созданного по шаблону (060 + ID документа)
		barcode_template_doc = "060" + doc_id
		print("060 + doc_ID ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		#
		reg_num = driver.find_element_by_id('regNum')
		reg_num = reg_num.get_attribute('innerHTML')
		reg_num = reg_num.strip()
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Файлы
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, files_button_xpath))).click()
		print("Files button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем клавишу Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем на клавишу По шаблону
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_template_xpath)))
		search_element.click()
		print("Pattern ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбераем шаблон
		search_element = wait.until(
			EC.visibility_of_element_located((By.XPATH, create_template_xpath)))
		search_element.click()
		print("Choose Pattern ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Закрываем просмоторщик созданного файла
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("Close window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Закрываем договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.ID, ok_button_id))).click()
		print("Close contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.FIVE)
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ШТРИХ-КОД"""
		print(TextColors.WARNING + "BARCODE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Открываем подменю "Штрих-кода"
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, barcode_xpath))).click()
		print("Barcode button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Архив
		time.sleep(SleepSeconds.ONE)
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, archive_button_xpath))).click()
		print("Archive button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле ввода
		time.sleep(SleepSeconds.ONE)
		search_element = driver.find_element_by_id('barcode')
		print("Barcode input find ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим данные
		search_element.send_keys(barcode_folder_name)
		search_element.send_keys(Keys.RETURN)
		time.sleep(SleepSeconds.ONE)
		search_element.send_keys(barcode_template_doc)
		search_element.send_keys(Keys.RETURN)
		print("Enter data ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим (необходимо)
		time.sleep(SleepSeconds.ONE)
		# Проверка на наличие файлов
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, archive_table_include_xpath))
		)
		print("Check for file ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Переключаемся на извлечение
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, remove_radiobutton_xpath))).click()
		print("Switch to extract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Извлекаем
		search_element = driver.find_element_by_id('barcode')
		search_element.send_keys(barcode_template_doc)
		search_element.send_keys(Keys.RETURN)
		print("Extract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОГОВОРЫ"""
		print(TextColors.WARNING + "CONTRACTS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Договоры
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_main_menu_button_xpath))).click()
		print("Contracts button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Переходим в договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, contracts_table_xpath))).click()
		action.double_click().perform()
		print("Choose and move to contract ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку с группой
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, test_group_button_xpath))).click()
		print("Group button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Делегировать
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delegation_button_xpath))).click()
		print("Delegation button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Сотрудник
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, employee_button_xpath))).click()
		print("Employer button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбераем сотрудника
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delegation_member_xpath))).click()
		print("Choose employer ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.ONE)
		action.send_keys(Keys.RETURN).perform()  # Enter
		time.sleep(SleepSeconds.ONE)
		# Закрываем окно с выбором сотрудников
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, close_button_xpath))).click()
		print("Close window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TEN)
		# Нажимаем кнопку добавления контрагента
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, linkage_button_xpath))).click()
		print("Linkage button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Заказчик
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, employee_contragent_add_xpath))).click()
		print("Employee button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Юр. Лицо
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, customer_contragent_add_xpath))).click()
		print("Customer contragent button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем Юр. Лицо
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, flexbby_contragent_add_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		action.send_keys(Keys.RETURN).perform()  # Enter
		print("Choose contragent ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# TODO: Сделать проверку на инвизибл перед нажатием "удалить" !!!
		time.sleep(SleepSeconds.TEN)
		# Удаляем контрагента
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_contragent_button_xpath))).click()
		print("Delete contragent ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Подтверждаем
		# Нажимаем Enter
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "CONTRACTS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Screen&Close"""
		print(TextColors.WARNING + "Delete&Screen&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.TEN)
		# Делаем скриншот
		scr_name = today + "_" + "docID" + "_" + doc_id + "_" + "complex" + "_" + "testing" + ".png"
		driver.save_screenshot(r'C:\Users\Operator\Desktop\Testing\Tests\Screenshots\%s' % scr_name)
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
		time.sleep(SleepSeconds.FIVE)
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Screen&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_activities END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.driver.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ComplexTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
