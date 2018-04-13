# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class CountriesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'CountriesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_countries(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_contracts START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		time.sleep(2)
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		time.sleep(2)
		printOk("General button click")
		# Переходим в Страны
		self.toolkit.clickByXPATH(menu_button_xpath % 'Страны')
		time.sleep(2)
		printOk("Countries button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(4)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test Country'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.fillAttributes(foreignName=name + ' Foreign Name')
		# Enter attributes
		self.toolkit.fillAttributes(codeNumeric='10')
		# Enter attributes
		self.toolkit.fillAttributes(codeAlphabetical2='0000')
		# Enter attributes
		self.toolkit.fillAttributes(codeAlphabetical3='0001')
		# Enter attributes
		self.toolkit.fillAttributes(comment='Test comment')
		# Click OK
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		# Sleep
		time.sleep(3)
		self.toolkit.clickByID('filter')
		printOk("Filter click")
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(1)
		# Choose object
		self.toolkit.clickByXPATH(cell_in_table_xpath % name)
		printOk('Choose object')
		# Click Delete
		self.toolkit.delete_in_table()
		print("", flush=True)
		print(TextColors.WARNING + "test_countries END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("----------------------------------------", flush=True)
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ContractsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
