# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class SettingsNumeratorsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_numerators(self):
		self.toolkit.login(login_text, password_text)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printInfo("General button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Нумераторы')
		printInfo("Countries button click")
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(2)
		name = 'Test numerator'
		self.toolkit.fillAttributes(name=name)
		self.toolkit.fillAttributes(prefix='Prefix')
		self.toolkit.fillAttributes(template='Test template')
		self.toolkit.fillAttributes(comment='Test comment')
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		time.sleep(2)
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
