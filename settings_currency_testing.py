# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class SettingsCurrencyTesting(unittest.TestCase):

	def setUp(self):
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_currency(self):
		self.toolkit.login(login_text, password_text)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printInfo("General button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Валюты')
		printInfo("Countries button click")
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(2)
		name = 'Test Currency'
		self.toolkit.fillAttributes(name=name)
		self.toolkit.fillAttributes(foreignName=name + ' Foreign Name')
		self.toolkit.fillAttributes(codeNumeric='10')
		self.toolkit.fillAttributes(rate='100')
		self.toolkit.fillAttributes(codeAlphabetical3='0001')
		self.toolkit.fillAttributes(comment='Test comment')
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		time.sleep(3)
		self.toolkit.clickByID('filter')
		printInfo("Filter click")
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(1)
		self.toolkit.clickByXPATH(cell_in_table_xpath % name)
		printInfo('Choose object')
		self.toolkit.delete_in_table()
		printInfo('Click OK')
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
