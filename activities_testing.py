# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class ActivitiesTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_activities(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Activities
		self.toolkit.clickByXPATH(menu_button_xpath % 'Активности')
		printInfo("Activities button find&click")
		self.toolkit.clickByID('new')
		printInfo("Add button find&click")
		time.sleep(2)

		""""GENERAL PAGE START"""
		printTitle("GENERAL PAGE START")
		time.sleep(2)
		# Enter the type of activity and select from the list
		self.toolkit.fillAttributes(documentTypeID=activity_type_name)
		self.toolkit.clickInPopupMenu(activity_type_name)
		printInfo("Choose activity type")
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.addComment()
		self.toolkit.chooseReferenceInWindow('responsibleID', 'Прокофьев Андрей Викторович')
		time.sleep(1)
		self.toolkit.addTag(activities_tag_name)
		self.toolkit.addLinkage('Компания', 'Флексби Солюшнс')
		self.toolkit.clickByID('close')
		time.sleep(2)
		printTitle("GENERAL END")

		"""MEMBERS"""
		self.toolkit.addMember(name='Прокофьев Андрей Викторович', first_group_name='Инициатор')

		"""ACTIVITIES"""
		self.toolkit.addSimpleActivity()

		"""FILES"""
		self.toolkit.addTestFolderInFiles()

		"""DELETING OBJECTS"""
		self.toolkit.deleteObj('Активности')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
