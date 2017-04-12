# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class ParametersTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ParametersTesting' START" + TextColors.ENDC, flush=True)
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

	def test_parameters(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_parameters START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("Contracts button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		print("----------------------------------------", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID='Тестирование параметров')
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu('Тестирование параметров')
		printOk("Choose type")
		time.sleep(SleepSeconds.TWO)
		# Проставляем дату документа
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		time.sleep(SleepSeconds.ONE)
		self.toolkit.clickByID('docNum')
		time.sleep(SleepSeconds.FOUR)
		# Заполняем параметр
		self.toolkit.fillParameter('Дата', '11.11.2014')
		time.sleep(SleepSeconds.ONE)
		# Заполняем параметр
		self.toolkit.fillParameter('Дробное число', '3,14')
		time.sleep(SleepSeconds.ONE)
		# Заполняем параметр
		self.toolkit.fillParameter('Строка', 'Test string')
		time.sleep(SleepSeconds.ONE)
		# Заполняем параметр
		self.toolkit.fillParameter('Текст', 'Test text')
		time.sleep(SleepSeconds.ONE)
		# Заполняем параметр
		self.toolkit.fillParameter('Целое число', '10')
		time.sleep(SleepSeconds.THREE)
		print("----------------------------------------", flush=True)
		self.toolkit.clickByID('deleteb')
		printOk("Delete button click")
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK button click")
		time.sleep(SleepSeconds.THREE)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "test_parameters END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ParametersTesting' FINISH" + TextColors.ENDC, flush=True, end="")


if __name__ == '__main__':
	unittest.main()
