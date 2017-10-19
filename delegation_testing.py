# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class DelegationTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'DelegationTesting' START" + TextColors.ENDC, flush=True)
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

	def test_delegation(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_delegation START" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(5)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("Contracts button click")
		time.sleep(3)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(7)
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		time.sleep(2)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		time.sleep(2)
		printOk("Choose contract type")
		self.toolkit.fillAttributes(docDate=TakeDate.tomorrow)
		time.sleep(2)
		self.toolkit.clickByID("processID.stateID")

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		test_member = 'Тестовый Сотрудник'
		delegation_text = 'Делегировать ...'
		sale_director = 'Чёсов Роман Геннадьевич'
		employee = str("Сотрудник")
		# Добавляем согласователя
		self.toolkit.addMember(test_member)
		time.sleep(2)
		# Добавляем согласователя
		self.toolkit.addMember(sale_director)
		time.sleep(2)
		# Переходим в Общее
		self.toolkit.clickTab(name='Общее')
		time.sleep(2)
		# Отправляем на согласование
		self.toolkit.clickByID('_processID_process_panel', "//div[text()='Отправить на согласование']")
		printOk('Send to coordination')
		time.sleep(10)

		#
		def delegatingToDirector():
			# Нажимаем на сотрудника
			self.toolkit.clickByID('_processID_process_panel', "//div[@class='qx-button-box']//div[contains(text(), "
			                                                   "'Тестовый Сотрудник')]")
			printOk('Choose Test employee')
			time.sleep(2)
			#
			self.toolkit.action.send_keys(Keys.ARROW_RIGHT).perform()
			time.sleep(2)
			# Нажимаем Сотрудник
			self.toolkit.clickByXPATH(employee_button_xpath)
			printOk('Click "Employee"')
			time.sleep(2)
			# Выбираем директора
			self.toolkit.clickByXPATH(cell_in_table_xpath % sale_director)
			printOk('Choose person in table')
			time.sleep(2)
			# Нажимаем выбрать
			self.toolkit.clickByID('choose')
			time.sleep(2)
			printOk("Choose click")

		#
		delegatingToDirector()
		# Нажимаем закрыть
		self.toolkit.clickByID('ok-button')
		time.sleep(2)
		printOk("Error close")
		# Нажимаем закрыть окно
		self.toolkit.clickByID('close')
		time.sleep(2)
		printOk("Close window")
		# Переходим в Участники
		self.toolkit.clickTab(name='Участники')
		# 
		self.toolkit.clickByID('filter')
		printOk("Filter click")
		#
		self.toolkit.sendKeysByXPATH("//div[@class='qx-popup']//input", sale_director)
		time.sleep(3)
		# Choose object
		self.toolkit.clickByID('processMembers', "//div[@class='qooxdoo-table-cell']")
		printOk('Choose object')
		# Delete
		self.toolkit.delete_in_table()
		printOk('Click OK')
		# Переходим в Общее
		self.toolkit.clickTab(name='Общее')
		time.sleep(2)
		delegatingToDirector()
		# Нажимаем закрыть окно
		self.toolkit.clickByID('close')
		time.sleep(2)
		printOk("Close window")
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Удаить договор
		self.toolkit.delete_into_doc()
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_contracts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'DelegationTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
