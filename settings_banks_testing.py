# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class BanksTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'BanksTesting' START" + TextColors.ENDC, flush=True)
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

	def test_banks(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_banks START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printOk("General button click")
		# Переходим в Адреса
		self.toolkit.clickByXPATH(menu_button_xpath % 'Банки')
		printOk("Countries button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test Bank'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.fillAttributes(nameForeign=name + ' Foreign Name')
		# Enter attributes
		self.toolkit.fillAttributes(kpp='773601001')
		# Enter attributes
		self.toolkit.fillAttributes(okpo='773601001')
		# Enter attributes
		self.toolkit.fillAttributes(inn='7707083893')
		# Enter attributes
		self.toolkit.fillAttributes(bik='044525225')
		# Enter attributes
		self.toolkit.fillAttributes(loroAccount='30301810000006000001')
		# Enter attributes
		self.toolkit.fillAttributes(regNumber='00001')
		# Enter attributes
		self.toolkit.fillAttributes(phone='+79551112233')
		# Enter attributes
		self.toolkit.fillAttributes(city='MOSCOW')
		# Enter attributes
		self.toolkit.fillAttributes(address='Moscow, test address')
		# Enter attributes
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Enter attributes
		self.toolkit.fillAttributes(comment='Test comment')
		# Click OK
		self.toolkit.clickByXPATH(ok_delete_button_window_xpath)
		# Sleep
		time.sleep(SleepSeconds.THREE)
		self.toolkit.clickByID('filter')
		printOk("Filter click")
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(SleepSeconds.ONE)
		# Choose object
		self.toolkit.clickByXPATH(cell_in_table_xpath % name)
		printOk('Choose object')
		# Delete
		self.toolkit.delete_in_table()
		print("", flush=True)
		print(TextColors.WARNING + "test_banks END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'BanksTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
