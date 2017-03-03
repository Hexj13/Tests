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
class ActivitiesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ActivitiesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_activities(self):
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
		# Находим в меню Активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, activities_menu_button_xpath))).click()
		print("Activities button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button find&click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.TWO)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Вводим в поле типа Активности текст
		activities_type_ok_name = str(activities_activity_type_name)
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath))).send_keys(
			activities_type_ok_name)
		print("Enter activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим и нажимаем в списке нужный тип документа
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % activities_type_ok_name))).click()
		print("Choose activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Today date
		today = datetime.date.today()
		today_str = today.strftime("%d.%m.%Y")
		print("Take today date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Проставляем дату диактивации
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath))).send_keys(today_str)
		print("Enter deactivate date ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Вводим Описание
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, subject_textarea_xpath))).send_keys(test_text)
		print("Enter description ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем кнопку Добавить Комментарий
		search_element = driver.find_element_by_xpath(add_comment_button_xpath).click()
		print("Add comment button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Находим поле и вводим текст
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, comment_textarea_xpath))).send_keys(test_text)
		print("Enter comment ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Сохранить
		search_element = driver.find_element_by_xpath(save_comment_button_xpath).click()
		print("Save button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Выбор Ответственного
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, responsible_input_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		print("Choose responsible ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем КТО
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, responsible_add_xpath))).click()
		time.sleep(SleepSeconds.ONE)
		action.send_keys(Keys.RETURN).perform()
		print("Choose WHO ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Добавляем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_tag_button_xpath))).click()
		print("Add Tag button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем тег
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, selected_tag_xpath % activities_tag_name))).click()
		time.sleep(SleepSeconds.ONE)
		action.send_keys(Keys.ENTER).perform()
		print("Choose tag ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Закрываем окно с тегами
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, close_window_button_xpath))).click()
		time.sleep(SleepSeconds.TWO)
		print("Close tag window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Участники
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, members_button_xpath))).click()
		print("Members button click----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Инициатор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, qx_menu_menu_select_xpath % iniciator_name))).click()
		print("Initiator button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Должность
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, qx_menu_menu_select_xpath % position_name))).click()
		print("Position button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Выбираем Генерального директора
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, responsible_add_xpath))).click()
		action.send_keys(Keys.RETURN).perform()
		print("Choose director ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем закрыть окно
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, close_window_button_xpath))).click()
		print("Close window ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, activities_button_xpath))).click()
		print("Activities button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Добавить
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
		print("Add button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Вводим тип Активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath))).send_keys(activities_type_ok_name)
		print("Enter activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.THREE)
		# Выбираем тип Активности
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % activities_type_ok_name))).click()
		print("Choose activity type ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.FIVE)
		# Нажимаем OK
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
		print("OK button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "ACTIVITY END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		search_element = wait.until(
			EC.invisibility_of_element_located((By.ID, shadow_id)))
		print("NO shadow", flush=True)
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Файлы
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, files_button_xpath))).click()
		print("Files button click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		time.sleep(SleepSeconds.TWO)
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
			EC.element_to_be_clickable((By.XPATH, file_name_input_xpath))).send_keys(test_text)
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
		print("Shadow delete ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Удаляем Активность
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, activities_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		time.sleep(SleepSeconds.FOUR)
		print("Delete activity ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "DELETE LINKS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Screen&Close"""
		print(TextColors.WARNING + "Delete&Screen&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Берём ID документа
		url = driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		doc_id = params['id']
		# Делаем скриншот
		scr_name = today_str + "_" + "docID" + "_" + doc_id + "_" + "activities" + "_" + "testing" + ".png"
		driver.save_screenshot(r'C:\Users\Operator\Desktop\Testing\Tests\screens\%s' % scr_name)
		time.sleep(SleepSeconds.TWO)
		print(
			"Screenshot with name = " + TextColors.BOLD + scr_name + TextColors.ENDC + " added ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		# Удалить договор
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, delete_entity_button_xpath))).click()
		print("Delete document ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Нажимаем Enter
		search_element = wait.until(
			EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
		print("ENTER click ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
		# Sleep
		time.sleep(SleepSeconds.TWO)
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
		print(TextColors.HEADER + "Test 'ActivitiesTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
