# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class SettingsCountriesTesting(unittest.TestCase):
	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_countries(self):
		self.toolkit.login(login_text, password_text)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printInfo("General button click")
		time.sleep(1)
		self.toolkit.click_arrow_down(2)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Страны')
		time.sleep(1)
		printInfo("Countries button click")
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(2)
		name = 'Test Country'
		self.toolkit.fillAttributes(name=name)
		self.toolkit.fillAttributes(foreignName=name + ' Foreign Name')
		self.toolkit.fillAttributes(codeNumeric='10')
		self.toolkit.fillAttributes(codeAlphabetical2='0000')
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
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
