# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class FilesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'FilesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_files(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_files START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(2)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		time.sleep(2)
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printOk("General button click")
		self.toolkit.click_arrow_down(8)
		# Переходим в Адреса
		self.toolkit.clickByXPATH(menu_button_xpath % 'Файлы')
		printOk("Countries button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(4)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test file'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.clearByID('priority', "//input")
		self.toolkit.fillAttributes(priority=30)
		# Enter attributes
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
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
		print("", flush=True)
		print(TextColors.WARNING + "test_files END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'FilesTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
