# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class AccountsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_accounts(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Accounts
		self.toolkit.clickByXPATH(menu_button_xpath % 'Юр. лица')
		printInfo("Account button find&click")
		self.toolkit.clickByID('new')

		""""GENERAL PAGE """
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(inn=inn)
		# Click the button to get the list of companies by TIN
		self.toolkit.clickByID('getCompanyData')
		printInfo("'Get data' button find&click")
		# Choose company
		self.toolkit.clickByXPATH(company_window_xpath)
		self.toolkit.fillAttributes(email=email_text)
		self.toolkit.fillAttributes(url='www.mcdonalds.com')
		self.toolkit.fillAttributes(phone=phone_text)
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.addTag(account_tag_name)
		self.toolkit.addComment()
		self.toolkit.addActivity()
		# Add structure
		printInfo("Adding structure")
		self.toolkit.clickTab("Структура")
		self.toolkit.clickByID('new')
		self.toolkit.fillAttributes(name=structure_name)
		self.toolkit.clickByID('okb')
		printInfo("Structure added")
		printTitle("GENERAL PAGE END")

		""""REQUISITES PAGE"""
		printTitle("REQUISITES PAGE START")
		self.toolkit.clickTab('Реквизиты')
		self.toolkit.fillAttributes(okpo=okpo_text)
		self.toolkit.fillAttributes(foreignLegalShortName=foreign_short_name_text)
		self.toolkit.fillAttributes(foreignLegalName=foreign_name_text)
		# Add the address. Activate the address field by clicking. Since the address is already put down, you do not need to enter data. /
		# Then you need to remove the focus to generate a list of possible addresses in Google Maps. Then select the first item from the list.
		self.toolkit.clickByID('streetAddress')
		self.toolkit.clickByID('city')
		printInfo("Press ENTER on address")
		self.toolkit.clickByID('proposed_addresses', "//a")
		printInfo("Selected first address to activate Google Maps")
		# Add the type of activity of the company
		self.toolkit.clickByID('CompanyActivityType_objectID', "//div[text() = 'Добавить']")
		printInfo("Activity type button click")
		self.toolkit.fillAttributes(code=activity_code)
		self.toolkit.fillAttributes(name=activity_name_text)
		self.toolkit.fillAttributes(comment=comment_text)
		printTitle("REQUISITES PAGE END")

		"""ADDING OBJECTS"""
		# Next, we add such objects as: bank accounts, document, contract, procuremet, /
		# invoice with contract, oppotunity, approval
		self.toolkit.addBankAccount()
		self.toolkit.addSimpleDocument()
		self.toolkit.addSimpleContract()
		self.toolkit.addSimpleProcurement()
		self.toolkit.addSimpleInvoiceWithContract()
		self.toolkit.addSimpleOppotunity()
		self.toolkit.addApproval()

		"""FILES PAGE"""
		self.toolkit.addTestFolderInFiles()

		"""DELETING OBJECTS"""
		self.toolkit.deleteObj('Документы')
		self.toolkit.deleteObj('Договоры')
		self.toolkit.deleteObj('Закупки')
		self.toolkit.deleteObj('Счета')
		self.toolkit.deleteObj('Продажи')
		self.toolkit.deleteObj('Согласование')
		# Delete an employee on the General page in the Employees tab
		printInfo("Choose employees")
		self.toolkit.clickTab('Общее')
		self.toolkit.clickTab('Сотрудники')
		self.toolkit.clickByXPATH(employee_table_xpath, resetPointerEvents=True)
		self.toolkit.clickByID('delete')
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("Delete click")
		# Remove the structure
		printInfo("Choose Structure")
		self.toolkit.clickTab('Структура')
		self.toolkit.clickByXPATH(employee_table_xpath, resetPointerEvents=True)
		self.toolkit.clickByID('delete')
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("Delete click")

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
