# coding=utf-8
# noinspection PyUnresolvedReferences
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class RequestsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_requests(self):
		self.toolkit.login(login_text, password_text)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Заявки')
		printInfo("Activities button find&click")
		self.toolkit.clickByID('new')
		time.sleep(2)

		""""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(documentTypeID='Запрос справки')
		time.sleep(1)
		self.toolkit.clickInPopupMenu('Запрос справки')
		printInfo("Choose type")
		time.sleep(2)
		self.toolkit.addTag('Срочно')
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.action.send_keys(Keys.ENTER).perform()
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.addComment()
		printTitle("GENERAL END")

		"""MEMBERS"""
		self.toolkit.addMembersAndDelete()

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
