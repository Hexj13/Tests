# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class DocumentsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_documents(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Documents
		self.toolkit.clickByXPATH(menu_button_xpath % 'Документы')
		printInfo("Documents button find&click")
		self.toolkit.clickByID('new')
		printInfo("Add button find&click")
		time.sleep(2)

		""""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(documentTypeID=simple_document_name)
		time.sleep(1)
		self.toolkit.clickInPopupMenu(simple_document_name)
		printInfo("Type selected")
		time.sleep(2)
		self.toolkit.clickByID('docDate')
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		self.toolkit.action.send_keys(Keys.ENTER)
		self.toolkit.fillTextarea(subject=test_text)
		self.toolkit.fillAttributes(activateDate=TakeDate.today)
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.addLinkage('Юр. лицо', 'Флексби Солюшнс')
		time.sleep(1)
		self.toolkit.addComment()
		self.toolkit.addTag('Testing')
		# Send the document for signing
		self.toolkit.clickByXPATH(to_state_button_xpath % 'Подписание')
		printTitle("GENERAL PAGE END")

		"""MEMBERS"""
		self.toolkit.addMember("Тестовый Сотрудник", first_group_name='Исполнитель')

		""""GENERAL PAGE"""
		printTitle("GENERAL PAGE START")
		# We send the document to the state "signed"
		self.toolkit.clickTab('Общее')
		self.toolkit.clickByXPATH(to_state_button_xpath % 'Подписан')
		printTitle("GENERAL PAGE END")

		"""MEMBERS"""
		self.toolkit.deleteMember('Исполнитель')

		"""RELATED DOCUMENTS"""
		printTitle("Related documents PAGE START")
		self.toolkit.clickTab('Документы')
		self.toolkit.clickByID('new')
		printInfo("Add button clicked")
		time.sleep(3)
		self.toolkit.clickByID('okb')
		time.sleep(1)
		printTitle("Related documents PAGE END")

		"""ACTIVITY"""
		self.toolkit.addSimpleActivity()

		"""FILES"""
		self.toolkit.addTestFolderInFiles()

		"""УДАЛЕНИЕ ССЫЛОК"""
		self.toolkit.deleteObj('Активности')
		self.toolkit.deleteObj('Документы')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
