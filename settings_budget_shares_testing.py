# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class BudgetSharesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'BudgetSharesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_budget_shares(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_budget_shares START" + TextColors.ENDC, flush=True)
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
		self.toolkit.clickByXPATH(menu_button_xpath % 'Статьи бюджета')
		printOk("Countries button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test budget share'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
		# Enter attributes
		self.toolkit.clickByID("color")
		self.toolkit.clickInPopupMenu('red')
		# Enter attributes
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Enter attributes
		self.toolkit.fillAttributes(comment='Test comment')
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
		print(TextColors.WARNING + "test_budget_shares END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'BudgetSharesTesting' FINISH" + TextColors.ENDC, flush=True, end="")


if __name__ == '__main__':
	unittest.main()
