# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class ContactsTesting(unittest.TestCase):

	def setUp(self):
		printTitle(self.__class__.__name__, TextColors.HEADER)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)

	def test_contacts(self):
		self.toolkit.login(login_text, password_text)
		# Click in the sidebar on Contacts
		self.toolkit.clickByXPATH(menu_button_xpath % 'Физ. лица')
		printInfo("Contacts button find&click")
		self.toolkit.clickByID('new')

		""""ОБЩЕЕ"""
		printTitle("GENERAL PAGE START")
		self.toolkit.fillAttributes(name=name_text)
		time.sleep(1)
		self.toolkit.fillAttributes(surname=surname_text)
		time.sleep(1)
		self.toolkit.fillAttributes(patronymic=patronymic_text)
		self.toolkit.fillAttributes(phone=phone_text)
		self.toolkit.fillAttributes(email=email_text)
		self.toolkit.clickByID("gender")
		self.toolkit.clickInPopupMenu(gender_text)
		time.sleep(1)
		self.toolkit.fillTextarea(comment=comment_text)
		self.toolkit.addTag(contact_tag_name)
		self.toolkit.addComment()
		self.toolkit.addActivity()
		# Create new position
		printInfo("Creating new position")
		self.toolkit.clickTab('Должности')
		self.toolkit.clickByID('new')
		self.toolkit.chooseReferenceInWindow('companyID', 'Флексби Солюшнс')
		self.toolkit.chooseReferenceInWindow('positionID', 'Отдел разработки')
		self.toolkit.clickInWindowByIDKey('okb')
		printInfo("New position created")
		printTitle("GENERAL END")

		"""ADDITIONALLY PAGE"""
		printTitle("ADDITIONALLY START")
		self.toolkit.clickTab(name='Дополнительно')
		self.toolkit.fillAttributes(birthday=TakeDate.tomorrow)
		self.toolkit.fillAttributes(inn=inn_text)
		self.toolkit.fillAttributes(snils=snils_text)
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.toolkit.clickByID('ContactPersonDocument_contactPersonID')
		time.sleep(2)
		# You must click (for activation) before filling in the field
		self.toolkit.clickByID('comment')
		self.toolkit.fillAttributes(comment=comment_text)
		self.toolkit.clickByID('series')
		self.toolkit.fillAttributes(series=series_text)
		self.toolkit.clickByID('number')
		self.toolkit.fillAttributes(number=number_text)
		self.toolkit.clickByID('deliveryDate')
		self.toolkit.fillAttributes(deliveryDate=TakeDate.today)
		self.toolkit.clickByID('expired')
		self.toolkit.fillAttributes(expired=TakeDate.tomorrow)
		self.toolkit.clickByID('issuer')
		self.toolkit.fillAttributes(issuer=issuer_text)
		self.toolkit.clickByID('issuerCode')
		self.toolkit.fillAttributes(issuerCode=issuerCode_text)
		# Add the address. Activate the address field by clicking. Since the address is already put down, you do not need to enter data. /
		# Then you need to remove the focus to generate a list of possible addresses in Google Maps. Then select the first item from the list.
		self.toolkit.clickByID('Address_objectID')
		time.sleep(1)
		self.toolkit.clickByID('streetAddress')
		self.toolkit.fillAttributes(streetAddress=adrr_text)
		self.toolkit.clickByID('city')
		time.sleep(1)
		self.toolkit.clickByID('proposed_addresses', "//a")
		printInfo("Selected first address to activate Google Maps")
		printTitle("ADDITIONALLY END")

		"""ADDING OBJECTS"""
		# Next, we add such objects as: bank accounts, document, contract, /
		# procuremet, invoice with contract, oppotunity, approval
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
		self.toolkit.deleteObj('Договоры')
		self.toolkit.deleteObj('Закупки')
		self.toolkit.deleteObj('Счета')
		self.toolkit.deleteObj('Продажи')
		self.toolkit.deleteObj('Согласование')
		self.toolkit.clickTab('Общее')

		"""REMOVE OBJECT CARD & EXIT"""
		self.toolkit.delete_into_doc()
		printTitle("SUCCESS", TextColors.OKGREEN)

	def tearDown(self):
		self.toolkit.quit()


if __name__ == '__main__':
	unittest.main()
