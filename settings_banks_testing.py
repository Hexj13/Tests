# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class SettingsBanksTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_banks(self):
		self.toolkit.login(login_text, password_text)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Общее')
		printInfo("General button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Банки')
		printInfo("Countries button click")
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(3)
		name = 'Test Bank'
		self.toolkit.fillAttributes(name=name)
		self.toolkit.fillAttributes(nameForeign=name + ' Foreign Name')
		self.toolkit.fillAttributes(kpp='773601001')
		self.toolkit.fillAttributes(okpo='773601001')
		self.toolkit.fillAttributes(inn='7707083893')
		self.toolkit.fillAttributes(bik='044525225')
		self.toolkit.fillAttributes(loroAccount='30301810000006000001')
		self.toolkit.fillAttributes(regNumber='00001')
		self.toolkit.fillAttributes(phone='+79551112233')
		self.toolkit.fillAttributes(city='MOSCOW')
		self.toolkit.fillAttributes(address='Moscow, test address')
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
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
