# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class OpportunitiesTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_opportunities(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Opportunities
		self.toolkit.clickByXPATH(menu_button_xpath % 'Продажи')
		printInfo("Activities button find&click")
		self.toolkit.clickByID('new')
		time.sleep(3)

		""""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(documentTypeID=sales_type_name)
		time.sleep(1)
		self.toolkit.clickInPopupMenu(sales_type_name)
		self.toolkit.addTag('event')
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.fillAttributes(email=email_text)
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.clearByID("percent", "//input")
		self.toolkit.fillAttributes(percent=50)
		self.toolkit.clearByID('cost', '//input')
		self.toolkit.fillAttributes(cost=100000)
		self.toolkit.addComment()
		self.toolkit.addActivity()
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
		printTitle("GENERAL PAGE END")

		"""ADDING OBJECTS"""
		# Next, we add such objects as: Contract, Procurement
		self.toolkit.addMember(name='Прокофьев Андрей Викторович', first_group_name='Инициатор')
		self.toolkit.addSimpleContract()
		self.toolkit.addSimpleProcurement()

		"""FILES PAGE"""
		self.toolkit.addTestFolderInFiles()

		"""DELETING OBJECTS"""
		self.toolkit.deleteObj('Договоры')
		self.toolkit.deleteObj('Закупки')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
