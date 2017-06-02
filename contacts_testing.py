# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class ContactsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ContactsTesting' START" + TextColors.ENDC, flush=True)
	print("----------------------------------------", flush=True)
	print("----------------------------------------", flush=True)

	def setUp(self):
		print(TextColors.WARNING + "setUp START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)
		print("", flush=True)
		print(TextColors.WARNING + "setUp END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def test_contacts(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_contacts START" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Физ. лица
		self.toolkit.clickByXPATH(menu_button_xpath % 'Физ. лица')
		printOk("Contacts button menu click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Вводим Name
		name_text_u = str(name_text)
		self.toolkit.fillAttributes(name=name_text_u)
		time.sleep(SleepSeconds.ONE)
		# Вводим Surname
		surname_text_u = str(surname_text)
		self.toolkit.fillAttributes(surname=surname_text_u)
		time.sleep(SleepSeconds.ONE)
		# Вводим Patronymic
		patronymic_text_u = str(patronymic_text)
		self.toolkit.fillAttributes(patronymic=patronymic_text_u)
		# Вводим Phone
		self.toolkit.fillAttributes(phone=phone_text)
		# Вводим Email
		self.toolkit.fillAttributes(email=email_text)
		# Выбираем пол
		self.toolkit.clickByID("gender")
		gender_text_u = str(gender_text)
		self.toolkit.clickInPopupMenu(gender_text_u)
		time.sleep(SleepSeconds.ONE)
		printOk("Choose sex")
		# Проставляем Описание
		comment_text_u = str(comment_text)
		self.toolkit.fillAttributes(comment=comment_text_u)
		# Добавляем тег
		self.toolkit.addTag(contact_tag_name)
		# Комментарий
		self.toolkit.addComment()
		# Добавляем и удаляем активность
		self.toolkit.addActivity()
		# Нажимаем Должности
		self.toolkit.clickTab('Должности')
		printOk("'Position' button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("'Add' button click")
		# Выбираем Компанию
		self.toolkit.chooseReferenceInWindow('companyID', 'Флексби Солюшнс')
		# Выбираем Должность
		self.toolkit.chooseReferenceInWindow('positionID', 'Генеральный директор')
		# Нажимаем ОК
		self.toolkit.clickInWindowByIDKey('okb')
		printOk("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОПОЛНИТЕЛЬНО"""
		print(TextColors.WARNING + "ADDITIONALLY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Дополнительно
		self.toolkit.clickTab(name='Дополнительно')
		printOk("Additionally button click")
		# Вводим День Рождения
		self.toolkit.fillAttributes(birthday=TakeDate.tomorrow)
		# Вводим ИНН
		self.toolkit.fillAttributes(inn=inn_text)
		# Вводим СНИЛС
		self.toolkit.fillAttributes(snils=snils_text)
		# Вводим Диактивацию
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Добавить Документ
		self.toolkit.clickByID('ContactPersonDocument_contactPersonID')
		time.sleep(SleepSeconds.TWO)
		printOk("Add document button click")
		"""КОСТЫЛЬ начался"""  # TODO: после исправления баги с полями в физ.лице нужно будет это всё переделать!
		# Вводим Описание
		self.toolkit.clickByID('comment')
		self.toolkit.fillAttributes(comment=comment_text_u)
		# Вводим Серию
		self.toolkit.clickByID('series')
		self.toolkit.fillAttributes(series=series_text)
		# Вводим Номер
		self.toolkit.clickByID('number')
		self.toolkit.fillAttributes(number=number_text)
		# Вводим дату выдачи паспорта
		self.toolkit.clickByID('deliveryDate')
		self.toolkit.fillAttributes(deliveryDate=TakeDate.today)
		# Вводим дату истечения паспорта
		self.toolkit.clickByID('expired')
		self.toolkit.fillAttributes(expired=TakeDate.tomorrow)
		# Вводим Кто Выдал
		self.toolkit.clickByID('issuer')
		self.toolkit.fillAttributes(issuer=issuer_text)
		# Вводим Номер Кто Выдал
		self.toolkit.clickByID('issuerCode')
		self.toolkit.fillAttributes(issuerCode=issuerCode_text)
		"""КОСТЫЛЬ закончился"""
		# Добавить Адрес
		self.toolkit.clickByID('Address_objectID')
		#
		time.sleep(SleepSeconds.ONE)
		#
		self.toolkit.clickByID('streetAddress')
		adrr_text_u = str(adrr_text)
		self.toolkit.fillAttributes(streetAddress=adrr_text_u)
		self.toolkit.clickByID('city')
		time.sleep(SleepSeconds.ONE)
		# Выбираем первый выпавший адрес для активации Google Maps
		self.toolkit.clickByID('proposed_addresses', "//a")
		printOk("Google Maps activate")
		print("", flush=True)
		print(TextColors.WARNING + "ADDITIONALLY END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""БАНКОВСКИЕ РЕКВИЗИТЫ"""
		print(TextColors.WARNING + "BANK REQUISITES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addBankAccount()
		print("", flush=True)
		print(TextColors.WARNING + "BANK REQUISITES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОГОРОВЫ"""
		print(TextColors.WARNING + "CONTRACTS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Договоры
		self.toolkit.clickTab(name='Договоры')
		printOk("Contracts button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.THREE)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose type")
		# Спим
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		# Спим
		time.sleep(SleepSeconds.FIVE)
		# Закрываем договор
		self.toolkit.clickByID('okb')
		printOk("Close contract")
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "CONTRACTS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ЗАКАЗЫ"""
		print(TextColors.WARNING + "ORDER START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Заказы
		self.toolkit.clickTab(name='Заказы')
		printOk("Orders button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.THREE)
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		# Спим
		time.sleep(SleepSeconds.FIVE)
		# Закрываем заказ
		self.toolkit.clickByID('okb')
		printOk("Close order")
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "ORDER END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СЧЕТА"""
		print(TextColors.WARNING + "INVOICES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Счета
		self.toolkit.clickTab(name='Счета')
		printOk("Invoices button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.THREE)
		# Находим поле Типа счёта и Вводим тип
		account_type_name_u = str(account_type_name)
		self.toolkit.fillAttributes(planTypeID=account_type_name_u)
		# Находим и нажимаем в списке нужный тип счёта
		self.toolkit.clickInPopupMenu(account_type_name_u)
		printOk("Choose document type")
		# Нажимаем на кнопку для выбора договора
		self.toolkit.chooseReferenceInWindow('parentID', contract_type_name)
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем счёт
		self.toolkit.clickByID('okb')
		printOk("Invoices close")
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "INVOICES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ПРОДАЖИ"""
		print(TextColors.WARNING + "OPPORTUNITIES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Продажи
		self.toolkit.clickTab(name='Продажи')
		printOk("Opportunities button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.THREE)
		# Находим поле Типа продажи и Вводим тип
		sales_type_name_u = str(sales_type_name)
		self.toolkit.fillAttributes(documentTypeID=sales_type_name_u)
		# Находим и нажимаем в списке нужный тип продажи
		self.toolkit.clickInPopupMenu(sales_type_name_u)
		printOk("Choose contract")
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем продажи
		self.toolkit.clickByID('okb')
		printOk("Opportunities close")
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "OPPORTUNITIES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СОГЛАСОВАНИЕ"""
		print(TextColors.WARNING + "APPROVALS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Согласование
		self.toolkit.clickTab(name='Согласование')
		printOk("Approvals button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем продажи
		self.toolkit.clickByID('okb')
		printOk("Approvals close")
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "APPROVALS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addTestFolderInFiles()
		print("", flush=True)
		print(TextColors.WARNING + "FILES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE LINKS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Удаляем Договор
		self.toolkit.deleteObj('Договоры')
		printOk("Delete Contract")
		# Удаляем Заказ
		self.toolkit.deleteObj('Заказы')
		printOk("Delete Order")
		# Удаляем Счёт
		self.toolkit.deleteObj('Счета')
		printOk("Delete Invoices")
		# Удаляем Продажу
		self.toolkit.deleteObj('Продажи')
		printOk("Delete Opportunities")
		# Удаляем Согласование
		self.toolkit.deleteObj('Согласование')
		printOk("Delete Approval")
		# Прохоим в Общее
		self.toolkit.clickTab('Общее')
		printOk("GO to General")
		# Спим
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "DELETE LINKS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Удаить договор
		self.toolkit.delete_into_doc()
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_contacts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ContactsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
