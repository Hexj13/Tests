# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class CurrencyTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'CurrencyTesting' START" + TextColors.ENDC, flush=True)
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

	def test_currency(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_currency START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(2)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printOk("General button click")
		# Переходим в Валюта
		self.toolkit.clickByXPATH(menu_button_xpath % 'Валюты')
		printOk("Countries button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(4)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test Currency'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.fillAttributes(foreignName=name + ' Foreign Name')
		# Enter attributes
		self.toolkit.fillAttributes(codeNumeric='10')
		# Enter attributes
		self.toolkit.fillAttributes(rate='100')
		# Enter attributes
		self.toolkit.fillAttributes(codeAlphabetical3='0001')
		# Enter attributes
		self.toolkit.fillAttributes(comment='Test comment')
		# Click OK
		self.toolkit.clickByXPATH(ok_delete_button_window_xpath)
		# Sleep
		time.sleep(3)
		self.toolkit.clickByID('filter')
		printOk("Filter click")
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(1)
		# Choose object
		self.toolkit.clickByXPATH(cell_in_table_xpath % name)
		printOk('Choose object')
		# Delete
		self.toolkit.delete_in_table()
		printOk('Click OK')
		print("", flush=True)
		print(TextColors.WARNING + "test_currency END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'CurrencyTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
