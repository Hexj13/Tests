# coding=utf-8
import unittest

from RootsLib.roots import *


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
		time.sleep(SleepSeconds.TWO)
		print("----------------------------------------", flush=True)

		"""НАСТРЙОКИ КЛАССИФИКАТОРА"""
		print(TextColors.WARNING + "CLASSIFICATOR SETTINGS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		self.toolkit.click_arrow_down(1)
		# Переходим в Товары и услуги
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printOk("Products button click")
		time.sleep(SleepSeconds.THREE)
		# Листаем вниз
		self.toolkit.click_arrow_down(3)
		# Переходим в Классификатор
		self.toolkit.clickByXPATH(menu_button_xpath % 'Классификатор')
		printOk("Classificator button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.TWO)
		# Проставляем Название
		self.toolkit.fillAttributes("//div[@class='qx-window']", name=classificator_name_text)
		# Описание
		self.toolkit.fillAttributes(comment=classificator_name_text)
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Сохраняем
		self.toolkit.clickByID('saveb')
		printOk("SAVE button click")
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить Классификацию
		self.toolkit.clickByID('classification', add_button_xpath)
		printOk("Add classification button click")
		time.sleep(SleepSeconds.TWO)
		# Выбираем из списка
		self.toolkit.clickByXPATH(reference_xpath % 'TestParam')
		printOk("Choose")
		# Нажимаем Выбрать
		self.toolkit.clickByID('choose')
		printOk("Choose button click")
		time.sleep(SleepSeconds.ONE)
		# Нажимаем ESC
		self.toolkit.action.send_keys(Keys.ESCAPE).perform()
		printOk("ESC button click")
		time.sleep(SleepSeconds.ONE)
		# Нажимаем ОК
		self.toolkit.clickByID('okb', "", "//div[@class='qx-window']")
		printOk("OK button click (in window)")
		time.sleep(SleepSeconds.TWO)
		# Закрываем выпадающее меню справа
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printOk("Close PRODUCT menu")
		time.sleep(SleepSeconds.ONE)
		# Закрываем выпадающее меню справа
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Close SETTINGS menu")
		print("", flush=True)
		print(TextColors.WARNING + "CLASSIFICATOR SETTINGS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ТОВАР"""
		print(TextColors.WARNING + "PRODUCT PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Каталог
		self.toolkit.clickByXPATH(menu_button_xpath % 'Каталог')
		printOk("CATALOG button click")
		# Переходим в Товары и услуги
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printOk("PRODUCT button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		# Проставляем:
		# Код товара
		self.toolkit.fillAttributes(code='0000x1')
		# Название
		self.toolkit.fillAttributes(name=product_text)
		# Код производителя
		self.toolkit.fillAttributes(productCode='0001x01')
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(SleepSeconds.FIVE)
		# Классификатор
		self.toolkit.chooseReferenceInWindow('hierarchyID', classificator_name_text)
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
		printOk("Choose in popup menu")
		# Страна. Очистка поля
		self.toolkit.clearByID('countryID', "//input")
		printOk("Clear")
		# Вводим страну
		self.toolkit.fillAttributes(countryID=country_text)
		# Выбор страны
		self.toolkit.clickInPopupMenu(country_text)
		printOk("Choose in popup menu")
		# Единица продажи
		self.toolkit.clickByID('salesQuantity', "//div[@class='qx-button-common-border']")
		printOk("ADD button click")
		self.toolkit.fillAttributes("//div[@id='salesQuantity']", '', quantityInID=quantity_text)
		self.toolkit.clickInPopupMenu(quantity_text)
		printOk("Choose in popup menu")
		self.toolkit.fillAttributes(multiplier=1)
		# Штрих-Код
		self.toolkit.clickByID('barcodes', "//div[@class='qx-button-common-border']")
		printOk("ADD button click")
		self.toolkit.fillAttributes(barcode='000101')
		# Добавялем файл
		self.toolkit.addTestFolderInFiles()
		# Удаляем Ед.продажи
		self.toolkit.clickByID('salesQuantity', "//div[@id='delete-button']")
		printOk("Delete button click")
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK button click")
		# Удаляем Штрих-код
		self.toolkit.clickByID('barcodes', "//div[@id='delete-button']")
		printOk("Delete button click")
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK button click")
		# ОК
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "PRODUCT PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ПРАЙС-ЛИСТЫ"""
		print(TextColors.WARNING + "PRICE LISTS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Прайс-листы
		self.toolkit.clickByXPATH(menu_button_xpath % 'Прайс-листы')
		printOk("PRICE-lists button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		# Проставляем:
		# Название
		self.toolkit.fillAttributes(name=price_name_text)
		# Дату деактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Описанеи
		self.toolkit.fillAttributes(comment=comment_text)
		# Нажимаем РЕДАКТИРОВАТЬ
		self.toolkit.clickByXPATH(edit_file_button_xpath)
		printOk("Edit button click")
		time.sleep(SleepSeconds.TWO)
		# Нажмаем Добавить
		self.toolkit.clickByXPATH(add_button_element_xpath)
		printOk("Add button click")
		# Выбор
		self.toolkit.clickByXPATH(reference_xpath % product_text)
		printOk("Choose")
		# Нажимаем Выбрать
		self.toolkit.clickByID('choose')
		printOk("Choose button click")
		# Нажимаем Закрыть
		self.toolkit.clickByID('close')
		printOk("Close button click")
		# Нажимаем сохранить
		self.toolkit.clickByID('saveCosts')
		printOk("Save button button click")
		# Нажимаем Закрыть в окне
		self.toolkit.clickByXPATH(close_window_button_xpath)
		printOk("Close window button button click")
		time.sleep(SleepSeconds.ONE)
		# ОК
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "PRICE LISTS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete Links"""
		print(TextColors.WARNING + "Delete Links START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		#
		self.toolkit.clickByXPATH(cell_in_table_xpath % price_name_text)
		printOk("Choose price-list")
		self.toolkit.clickByID('delete')
		printOk("Delete button click")
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK window button click")
		#
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printOk('Products button (in menu) click')
		self.toolkit.clickByXPATH(cell_in_table_xpath % product_text)
		printOk('Choose')
		self.toolkit.clickByID('delete')
		printOk('Delete button click')
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk('OK button click')
		#
		self.toolkit.clickByXPATH(menu_button_xpath % 'Каталог')
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Товары и услуги')
		printOk("Products button click")
		time.sleep(SleepSeconds.THREE)
		self.toolkit.click_arrow_down(3)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Классификатор')
		printOk("Classificator button click")
		time.sleep(SleepSeconds.TWO)
		self.toolkit.clickByXPATH(cell_in_table_xpath % classificator_name_text)
		printOk("Choose")
		self.toolkit.clickByID('delete')
		printOk("Delete button click")
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK button click")
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
		print(TextColors.HEADER + "Test 'CatalogTesting' FINISH" + TextColors.ENDC, flush=True, end="")


if __name__ == '__main__':
	unittest.main()
