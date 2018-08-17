# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class ContractsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_contracts(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Contracts
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printInfo("Contracts button find&click")
		self.toolkit.clickByID('new')
		time.sleep(2)

		"""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(documentTypeID=contracts_type_name)
		self.toolkit.clickInPopupMenu(contracts_type_name)
		printInfo("Type selected")
		time.sleep(1)
		self.toolkit.clickByID('docDate')
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.addTag('FAIL')
		self.toolkit.addComment()
		# Send for approval
		self.toolkit.clickByID('_processID_process_panel', "//div[text()='Отправить на согласование']")
		time.sleep(1)
		# Select a signer
		self.toolkit.fillAttributes(signerID=signer_position_name)
		self.toolkit.clickInPopupMenu(signer_name)
		printInfo("Choose signer")
		# Add A Linkage
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
		printTitle("GENERAL PAGE END")

		"""MEMBERS"""
		self.toolkit.addMembersAndDelete('Инициатор', 'Согласователь')

		"""PAYMENT SCHEDULE PAGE"""
		printTitle("PAYMENT SCHEDULE PAGE START")
		self.toolkit.clickTab('График платежей')
		self.toolkit.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(1)
		# Select payment period
		self.toolkit.fillAttributes(paymentPeriodID=payment_period_name)
		self.toolkit.clickInPopupMenu(payment_period_name)
		printInfo("Payment period selected")
		# Select payment plan
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		self.toolkit.clickInPopupMenu(payment_plan_name)
		printInfo("Enter payment plan")
		self.toolkit.clickByID('cost')
		time.sleep(1)
		self.toolkit.clearByID('cost', '//input')
		self.toolkit.fillAttributes(cost=payment_cost_name)
		self.toolkit.fillAttributes(comment=test_text)
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		printInfo("OK button click")
		printTitle("PAYMENT SCHEDULE PAGE END")

		"""SPECIFICATION PAGE START"""
		printTitle("SPECIFICATION PAGE START")
		self.toolkit.clickTab('Спецификация')
		self.toolkit.clickByID('createSpecification')
		printInfo("Add specification button click")
		time.sleep(2)
		# Click in the tree on " All"
		self.toolkit.treeClick('Все')
		# Product select
		self.toolkit.clickByXPATH(pencil_window_xpath, resetPointerEvents=True)
		self.toolkit.clickByID('choose')
		printInfo("Choose button click")
		self.toolkit.clickByID('close')
		printInfo("Close window")
		printTitle("SPECIFICATION PAGE END")

		"""ADDING OBJECTS"""
		# Next, we add such objects as: Invoice, Activity, Supplement
		self.toolkit.addSimpleInvoice()
		self.toolkit.addSimpleActivity()
		self.toolkit.addSupplement()

		"""FILES PAGE"""
		self.toolkit.addTestFolderInFiles()

		"""DELETING OBJECTS"""
		self.toolkit.deleteObj('Счета')
		self.toolkit.deleteObj('Активности')
		self.toolkit.deleteObj('Доп. соглашения')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
