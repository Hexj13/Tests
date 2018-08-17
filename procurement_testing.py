# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class OrdersTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_procurement(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Procurement
		self.toolkit.clickByXPATH(menu_button_xpath % 'Закупки')
		printInfo("Procurement button click")
		self.toolkit.clickByID('new')

		"""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		self.toolkit.fillTextarea(subject=comment_text)
		self.toolkit.addTag(procurement_tag_name)
		self.toolkit.addComment()
		self.toolkit.fillAttributes(signerID=signer_position_name)
		self.toolkit.clickInPopupMenu(signer_name)
		printInfo("Choose signer")
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
		time.sleep(2)
		printTitle("GENERAL PAGE END")

		"""MEMBERS"""
		self.toolkit.addMembersAndDelete()

		"""PAYMENT SCHEDULE"""
		printTitle("PAYMENT SCHEDULE PAGE START")
		self.toolkit.clickTab('График платежей')
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(2)
		# Select payment period
		self.toolkit.fillAttributes(paymentPeriodID=payment_period_name)
		self.toolkit.clickInPopupMenu(payment_period_name)
		printInfo("Choose payment period")
		# Select payment plan
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		self.toolkit.clickInPopupMenu(payment_plan_name)
		printInfo("Enter payment plan")
		time.sleep(1)
		self.toolkit.clickByID('taxClassID', "//div")
		self.toolkit.clickInPopupMenu('НДС 18%')
		self.toolkit.fillAttributes("//div[@class='qx-window']", "", cost=payment_cost_name)
		self.toolkit.clickInWindowByIDKey("activateDate")
		time.sleep(1)
		self.toolkit.clickByXPATH(okb_id_window_button_xpath)
		printTitle("PAYMENT SCHEDULE PAGE END")

		"""ADDING OBJECTS"""
		self.toolkit.addSimpleInvoice()
		self.toolkit.addSimpleActivity()

		"""FILES PAGE"""
		self.toolkit.addTestFolderInFiles()

		"""DELETING OBJECTS"""
		self.toolkit.deleteObj('Счета')
		self.toolkit.deleteObj('Активности')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
