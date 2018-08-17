# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class InvoicesTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_invoices(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Invoices
		self.toolkit.clickByXPATH(menu_button_xpath % 'Счета')
		printInfo("Activities button find&click")
		self.toolkit.clickByID('new')
		time.sleep(2)

		""""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		self.toolkit.clickInPopupMenu(payment_plan_name)
		self.toolkit.chooseReferenceInWindow('parentID', 'Продажа (универсальный)')
		self.toolkit.addTag('Регулярный платильщик')
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.fillAttributes(signerID=signer_position_name)
		self.toolkit.clickInPopupMenu(signer_name)
		printInfo("Choose signer")
		time.sleep(2)
		self.toolkit.fillAttributes(statementDate=TakeDate.today)
		self.toolkit.addComment()
		self.toolkit.addLinkage(('Заказчик', 'Юр. лицо'), 'Адидас')
		printTitle("GENERAL END")

		"""MEMBERS"""
		self.toolkit.addMembersAndDelete()

		"""SPECIFICATION"""
		# Create a new specification, sort in the tree to "All" and select the product
		printTitle("SPECIFICATION PAGE START")
		self.toolkit.clickTab('Спецификация')
		self.toolkit.clickByID('createSpecification')
		printInfo("Add specification button click")
		time.sleep(1)
		self.toolkit.treeClick('Все')
		self.toolkit.clickByXPATH(pencil_window_xpath, resetPointerEvents=True)
		self.toolkit.clickByID('choose')
		printInfo("Choose pencil from Enter")
		self.toolkit.clickByID('close')
		printInfo("Close window")
		printTitle("SPECIFICATION PAGE END")

		"""PREPAYMENTS PAGE"""
		printTitle("PREPAYMENTS PAGE START")
		self.toolkit.clickTab('Предоплаты')
		self.toolkit.clickByXPATH(add_button_xpath)
		printInfo("Add button click")
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		time.sleep(2)
		printTitle("PREPAYMENTS PAGE END")

		"""ACTIVITY"""
		self.toolkit.addSimpleActivity()

		"""FILES"""
		self.toolkit.addTestFolderInFiles()

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
