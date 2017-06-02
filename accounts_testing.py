# coding=utf-8
import unittest
from RootsLib.roots import *


# noinspection PyUnusedLocal
class AccountsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'AccountsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_accounts(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_accounts START" + TextColors.ENDC, flush=True)
		print("")
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Юр. лица
		self.toolkit.clickByXPATH(menu_button_xpath % 'Юр. лица')
		printOk("Account button find&click")
		time.sleep(SleepSeconds.ONE)
		# Добавить
		self.toolkit.clickByID('new')
		print("Add button find&click")
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.THREE)
		# Вводим ИНН
		self.toolkit.fillAttributes(inn=inn)
		# Нажимаем кнопку
		self.toolkit.clickByID('getCompanyData')
		printOk("'Get data' button find&click")
		# Выбираем компанию
		self.toolkit.clickByXPATH(company_window_xpath.format(inn=inn))
		printOk("Choose company")
		# Проставляем email
		self.toolkit.fillAttributes(email=email_text)
		# Проставляем site
		self.toolkit.fillAttributes(url='www.mcdonalds.com')
		printOk("Enter Site")
		# Проставляем  phone
		self.toolkit.fillAttributes(phone=phone_text)
		# time.sleep(SleepSeconds.FIVE)
		# self.toolkit.driver.find_element_by_id('photo').send_keys(os.getcwd() + r"C:\Users\Operator\Pictures\1378.jpg")
		# time.sleep(60)
		# Проставляем дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		printOk("Enter deactivate date")
		# Проставляем комментарий
		self.toolkit.fillAttributes(comment=comment_text)
		# Добавляем тег
		self.toolkit.addTag(account_tag_name)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Комментарий
		self.toolkit.addComment()
		# Добавляем Автивность и удаляем
		self.toolkit.addActivity()
		# TODO : Добавление парамов в ОБЩЕМ
		# Нажимаем Структура
		self.toolkit.clickTab("Структура")
		printOk("Structure button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Декод
		structure_name_u = str(structure_name)
		printOk("Structure name decode")
		# Вводим название Структуры
		self.toolkit.fillAttributes(name=structure_name_u)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Ок
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		#
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		""""РЕКВИЗИТЫ"""
		print(TextColors.WARNING + "REQUISITES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Реквизиты
		self.toolkit.clickTab('Реквизиты')
		printOk("Requisites button click")
		# Вводим ОКПО
		self.toolkit.fillAttributes(okpo=okpo_text)
		# Вводим Сокращённое имя
		self.toolkit.fillAttributes(foreignLegalShortName=foreign_short_name_text)
		# Вводим Полное имя
		self.toolkit.fillAttributes(foreignLegalName=foreign_name_text)
		# Клик по адресу
		self.toolkit.clickByID('streetAddress')
		# Клик по городу, чтобы снять фокус и сгенерилась ссылка Google Maps
		self.toolkit.clickByID('city')
		printOk("Press ENTER on address")
		# Выбираем первый выпавший адрес для активации Google Maps
		self.toolkit.clickByID('proposed_addresses', "//a")
		printOk("Choose first address to activate Google Maps")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить вид активности
		self.toolkit.clickByID('CompanyActivityType_objectID', "//div[text() = 'Добавить']")
		printOk("Activity type button click")
		# Вводим код активности
		self.toolkit.fillAttributes(code=activity_code)
		# Вводим имя активности
		self.toolkit.fillAttributes(name=activity_name_text)
		# Вводим коммент
		self.toolkit.fillAttributes(comment=comment_text)
		print("", flush=True)
		print(TextColors.WARNING + "REQUISITES END" + TextColors.ENDC, flush=True)
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
		time.sleep(SleepSeconds.SEVEN)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose type")
		time.sleep(SleepSeconds.FOUR)
		# Спим
		# Проставляем дату документа
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		self.toolkit.clickByID('processID.stateID')
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
		time.sleep(SleepSeconds.ONE)
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
		# Проходим в Сотрудники
		self.toolkit.clickTab('Сотрудники')
		printOk("GO to employees")
		# Выбираем сотрудника ссылающегося на док
		self.toolkit.clickByXPATH(employee_table_xpath)
		printOk("Choose employees")
		# Нажимаем Удалить
		self.toolkit.clickByID('delete')
		printOk("Delete click")
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Проходим в Структуру
		self.toolkit.clickTab('Структура')
		printOk("GO to Structure")
		# Выбираем структуру ссылающегося на док
		self.toolkit.clickByXPATH(employee_table_xpath)
		printOk("Choose Structure")
		# Нажимаем Удалить
		self.toolkit.clickByID('delete')
		printOk("Delete click")
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
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
		print(TextColors.WARNING + "test_accounts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'AccountsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
