# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class PaymentPeriodTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'PaymentPeriodTesting' START" + TextColors.ENDC, flush=True)
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

	def test_payment_period(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_payment_period START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")
		# Переходим в Общее
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printOk("General button click")
		# Клик вниз
		self.toolkit.click_arrow_down(9)
		# Переходим в Адреса
		self.toolkit.clickByXPATH(menu_button_xpath % 'Периоды платежей')
		printOk("Countries button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(4)
		print("----------------------------------------", flush=True)
		# set Name
		name = 'Test payment period'
		# Enter attributes
		self.toolkit.fillAttributes(name=name)
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
		# Delete
		self.toolkit.delete_in_table()
		print("", flush=True)
		print(TextColors.WARNING + "test_payment_period END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'PaymentPeriodTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
