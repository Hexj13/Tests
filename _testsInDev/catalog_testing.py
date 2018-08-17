# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class CatalogTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'CatalogTesting' START" + TextColors.ENDC, flush=True)
	print("----------------------------------------", flush=True)
	print("----------------------------------------", flush=True)

	def setUp(self):
		print(TextColors.WARNING + "setUp START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)
		print("", flush=True)
		print(TextColors.WARNING + "setUp END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def test_catalog(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_catalog START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(2)
		print("----------------------------------------", flush=True)

		"""НАСТРЙОКИ КЛАССИФИКАТОРА"""
		print(TextColors.WARNING + "CLASSIFICATOR SETTINGS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		time.sleep(2)
		self.toolkit.click_arrow_down(9)
		# Переходим в Товары и услуги
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printInfo("Products button click")
		time.sleep(3)
		# Переходим в Классификатор
		self.toolkit.clickByXPATH(menu_button_xpath % 'Классификатор')
		printInfo("Classificator button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(2)
		# Проставляем Название
		self.toolkit.fillAttributes("//div[@class='qx-window']", name=class_text_name)
		# Описание
		self.toolkit.fillAttributes(comment=class_text_name)
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Сохраняем
		self.toolkit.clickByID('saveb')
		printInfo("SAVE button click")
		time.sleep(2)
		# Нажимаем Добавить Классификацию
		self.toolkit.clickByID('classification', add_button_xpath)
		printInfo("Add classification button click")
		time.sleep(2)
		# Выбираем из списка
		self.toolkit.clickByXPATH(reference_xpath % 'TestParam')
		printInfo("Choose")
		# Нажимаем Выбрать
		self.toolkit.clickByID('choose')
		printInfo("Choose button click")
		time.sleep(1)
		# Нажимаем ESC
		self.toolkit.action.send_keys(Keys.ESCAPE).perform()
		printInfo("ESC button click")
		time.sleep(1)
		# Нажимаем ОК
		self.toolkit.clickByID('okb', "", "//div[@class='qx-window']")
		printInfo("OK button click (in window)")
		time.sleep(2)
		# Закрываем выпадающее меню справа
		# self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printInfo("Close PRODUCT menu")
		time.sleep(1)
		# Закрываем выпадающее меню справа
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Close SETTINGS menu")
		print("", flush=True)
		print(TextColors.WARNING + "CLASSIFICATOR SETTINGS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ТОВАР"""
		print(TextColors.WARNING + "PRODUCT PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Каталог
		self.toolkit.clickByXPATH(menu_button_xpath % 'Каталог')
		self.toolkit.clickByXPATH(menu_button_xpath % 'Счета')
		printInfo("CATALOG button click")
		# Переходим в Товары и услуги
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printInfo("PRODUCT button click")
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(4)
		# Код товара
		self.toolkit.fillAttributes(code='0000x1')
		# Название
		self.toolkit.fillAttributes(name=product_text)
		# Код производителя
		self.toolkit.fillAttributes(productCode='0001x01')
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(5)
		# Классификатор
		self.toolkit.chooseReferenceInWindow('hierarchyID', class_text_name)
		# Описание
		self.toolkit.fillAttributes(comment=test_text)
		# Ширину
		self.toolkit.clickByID('width')
		self.toolkit.fillAttributes(width=10)
		# Высоту
		self.toolkit.clickByID('height')
		self.toolkit.fillAttributes(height='10')
		# Глубину
		self.toolkit.clickByID('depth')
		self.toolkit.fillAttributes(depth='10')
		# Масса
		self.toolkit.clickByID('weight')
		self.toolkit.fillAttributes(weight='10')
		# Единицу измерения
		self.toolkit.fillAttributes(quantityInID=quantity_text)
		# Выбор из списка
		self.toolkit.clickInPopupMenu(quantity_text)
		printInfo("Choose in popup menu")
		# Страна. Очистка поля
		self.toolkit.clearByID('countryID', "//input")
		# Вводим страну
		self.toolkit.fillAttributes(countryID=country_text)
		# Выбор страны
		self.toolkit.clickInPopupMenu(country_text)
		printInfo("Choose in popup menu")
		# Единица продажи
		self.toolkit.clickByID('salesQuantity', "//div[@class='qx-button-common-border']")
		printInfo("ADD button click")
		self.toolkit.fillAttributes("//div[@id='salesQuantity']", '', quantityInID=quantity_text)
		self.toolkit.clickInPopupMenu(quantity_text)
		printInfo("Choose in popup menu")
		self.toolkit.fillAttributes(multiplier=1)
		time.sleep(2)
		self.toolkit.clickByID('okb')
		printInfo("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "PRODUCT PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ПРАЙС-ЛИСТЫ"""
		print(TextColors.WARNING + "PRICE LISTS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Прайс-листы
		self.toolkit.clickByXPATH(menu_button_xpath % 'Прайс-листы')
		printInfo("PRICE-lists button click")
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(4)
		# Проставляем:
		# Название
		self.toolkit.fillAttributes(name=price_name_text)
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Описанеи
		self.toolkit.fillAttributes(comment=comment_text)
		# Нажимаем РЕДАКТИРОВАТЬ
		self.toolkit.clickByXPATH(edit_file_button_xpath)
		printInfo("Edit button click")
		time.sleep(2)
		# Нажмаем Добавить
		self.toolkit.clickByXPATH(add_button_element_xpath)
		printInfo("Add button click")
		# Выбор
		self.toolkit.clickByXPATH(reference_xpath % product_text)
		printInfo("Choose")
		# Нажимаем Выбрать
		self.toolkit.clickByID('choose')
		printInfo("Choose button click")
		# Нажимаем Закрыть
		self.toolkit.clickByID('close')
		printInfo("Close button click")
		# Нажимаем сохранить
		self.toolkit.clickByID('saveCosts')
		printInfo("Save button button click")
		# Нажимаем Закрыть в окне
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("Close window button button click")
		time.sleep(1)
		# ОК
		self.toolkit.clickByID('okb')
		printInfo("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "PRICE LISTS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete Links"""
		print(TextColors.WARNING + "Delete Links START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		#
		self.toolkit.clickByXPATH(cell_in_table_xpath % price_name_text)
		printInfo("Choose price-list")
		self.toolkit.clickByID('delete')
		printInfo("Delete button click")
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("OK window button click")
		#
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printInfo('Products button (in menu) click')
		self.toolkit.clickByXPATH(cell_in_table_xpath % product_text)
		printInfo('Choose')
		self.toolkit.clickByID('delete')
		printInfo('Delete button click')
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo('OK button click')
		#
		self.toolkit.clickByXPATH(menu_button_xpath % 'Каталог')
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		# Листаем вниз
		self.toolkit.click_arrow_down(9)
		# self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printInfo("Products button click")
		time.sleep(2)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Классификатор')
		printInfo("Classificator button click")
		time.sleep(4)
		self.toolkit.clickByXPATH(cell_in_table_xpath % class_text_name)
		printInfo("Choose")
		time.sleep(2)
		self.toolkit.delete_in_table()
		print("", flush=True)
		print(TextColors.WARNING + "Delete Links END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_catalog END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'CatalogTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
