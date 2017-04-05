# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class TypeTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'TypeTesting' START" + TextColors.ENDC, flush=True)
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

	def test_type(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_type START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printOk("General button click")
		# Переходим в OPF
		self.toolkit.clickByXPATH(menu_button_xpath % 'ОПФ')
		printOk("OPF button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'TEST'
		# Enter attributes
		self.toolkit.fillAttributes(shortName="TEST")
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.fillAttributes(foreignName=name + ' Foreign Name')
		# Enter attributes
		self.toolkit.fillAttributes(comment='Test comment')
		# Enter attributes
		self.toolkit.fillAttributes(code='100')
		# Click OK
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		# Sleep
		time.sleep(SleepSeconds.THREE)
		self.toolkit.clickByID('filter')
		printOk("Filter click")
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(SleepSeconds.ONE)
		# Choose object
		self.toolkit.clickByXPATH(cell_in_table_xpath % name)
		printOk('Choose object')
		# Click Delete button
		self.toolkit.clickByID('delete')
		printOk('Click delete')
		# Click OK
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk('Click OK')
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "test_type END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'TypeTesting' FINISH" + TextColors.ENDC, flush=True, end="")


if __name__ == '__main__':
	unittest.main()
