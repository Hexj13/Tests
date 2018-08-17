# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class RelationsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)

		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_relations(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Settings
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printInfo("Settings button click")

		""""ROLES"""
		printTitle("ROLE ADDING START")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Связи')
		printInfo("Relations button click")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Роли объектов')
		printInfo("Roles button click")
		self.toolkit.clickByID('new')
		printInfo("ADD button click")
		time.sleep(2)
		self.toolkit.fillAttributes(name=test_role_text)
		self.toolkit.fillAttributes(tag='Test')
		self.toolkit.fillAttributes(comment='Test comment')
		self.toolkit.clickByID('new')
		printInfo("Click button ADD")
		self.toolkit.chooseReferenceInWindow('tableID', 'Company')
		printInfo("Add company from table")
		self.toolkit.chooseReferenceInWindow('baseTableID', 'CompanyTree')
		printInfo("Add CompanyTree from table")
		time.sleep(1)
		self.toolkit.clickByID('nameForeignID')
		printInfo("Click on input")
		self.toolkit.action.send_keys('id').perform()
		printInfo("Send keys in input")
		time.sleep(1)
		self.toolkit.clickInPopupMenu('id')
		printInfo("Choose in popup menu")
		time.sleep(1)
		self.toolkit.clickInWindowByIDKey('okb')
		printInfo("Click OK button")
		time.sleep(3)
		printTitle("ROLE ADDING END")

		"""GROUPS"""
		printTitle("GROUPS ADDING START")
		self.toolkit.clickByXPATH(menu_button_xpath % 'Группы')
		printInfo("Go to 'groups' in side-menu")
		self.toolkit.clickByID('new')
		printInfo("Click ADD button")
		time.sleep(1)
		self.toolkit.fillAttributes(name=test_group_text)
		self.toolkit.clickByXPATH('//div[@id="rolesInGroup"]//div[text()="Добавить"]')
		self.toolkit.clickByXPATH(
			"//div[@class='qx-window'and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')])]//div[@class='qooxdoo-table-cell' and (text()='%s')]" % test_role_text)
		self.toolkit.clickByID('choose')
		self.toolkit.action.send_keys(Keys.ESCAPE).perform()
		self.toolkit.clickByID('okb')
		time.sleep(2)
		printTitle("GROUPS ADDING END")

		"""DELETING"""
		self.toolkit.clickByXPATH(
			"//div[@class='qooxdoo-table-cell' and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')]) and (text()='%s')]" % test_group_text,
			resetPointerEvents=True)
		self.toolkit.clickByID('delete')
		self.toolkit.clickByID('ok-button')
		self.toolkit.clickByXPATH(menu_button_xpath % 'Роли объектов')
		printInfo("Relations button click")
		self.toolkit.clickByXPATH(
			"//div[@class='qooxdoo-table-cell' and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')]) and (text()='%s')]" % test_role_text,
			resetPointerEvents=True)
		self.toolkit.clickByID('delete')
		self.toolkit.clickByID('ok-button')

	def tearDown(self):
		self.toolkit.quit()
		printTitle("SUCCESS", TextColors.OKGREEN)


if __name__ == '__main__':
	unittest.main()
