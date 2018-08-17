# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class DelegationTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_delegation(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Contracts
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printInfo("Contracts button click")
		self.toolkit.clickByID('new')
		time.sleep(2)

		"""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		self.toolkit.clickInPopupMenu(contract_type_name)
		printInfo("Type selected")
		self.toolkit.fillAttributes(docDate=TakeDate.tomorrow)
		self.toolkit.action.send_keys(Keys.ENTER).perform()
		self.toolkit.clickByID("processID.stateID")
		printTitle("GENERAL PAGE END")

		"""MEMBERS PAGE"""
		printTitle("MEMBERS PAGE START")
		self.toolkit.addMember(test_member)
		self.toolkit.addMember(sale_director)
		# Go to the "General" page to delegate authority
		self.toolkit.clickTab(name='Общее')
		self.toolkit.clickByID('_processID_process_panel', "//div[text()='Отправить на согласование']")
		printInfo('Send to coordination')
		time.sleep(3.5)

		# The delegation function
		def delegatingToDirector():
			self.toolkit.clickByID('_processID_process_panel',
			                       child_xpath="//div[@class='qx-circle']//div[contains(text(), "
			                                   "'Тестовый С.')]", resetPointerEvents=True)
			printInfo('Choose Test employee')
			time.sleep(1)
			self.toolkit.action.send_keys(Keys.ARROW_RIGHT)
			self.toolkit.action.perform()
			self.toolkit.clickByXPATH(employee_button_xpath)
			printInfo('"Employee" clicked')
			self.toolkit.filterInTable(sale_director)
			self.toolkit.clickByXPATH(cell_in_table_xpath % sale_director, resetPointerEvents=True)
			printInfo('Person in table selected')
			self.toolkit.clickByID('choose')
			printInfo("'Choose' button clicked")

		# Call the delegation function to check if there is an error /
		# inside the system (the error should appear in the modal window)
		delegatingToDirector()
		self.toolkit.clickByID('ok-button')
		printInfo("Error close")
		self.toolkit.clickByID('close')
		printInfo("Close window")
		self.toolkit.clickTab(name='Участники')
		self.toolkit.clickByID('processMembers', resetPointerEvents=True,
		                       child_xpath="//div[@class='qooxdoo-table-cell']")
		printInfo('Choose object')
		self.toolkit.delete_in_table()
		printInfo("'OK' button clicked")
		self.toolkit.clickTab(name='Общее')
		# Call the delegate function in order to verify the absence of errors within the system.
		delegatingToDirector()
		self.toolkit.clickByID('close')
		time.sleep(2)
		printInfo("Close window")
		printTitle("MEMBERS PAGE END")

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
