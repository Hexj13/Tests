# coding=utf-8
import unittest

from roots.roots import *


# noinspection PyUnusedLocal
class ComplexTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ComplexTesting' START" + TextColors.ENDC, flush=True)
	print("----------------------------------------", flush=True)
	print("----------------------------------------", flush=True)

	def setUp(self):
		print(TextColors.WARNING + "setUp START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit = UITestToolkit()
		self.toolkit.setSite(site_url)
		print(TextColors.WARNING + "setUp END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def test_complex(self):
		self.toolkit.login(login_text, password_text)
		print("", flush=True)
		print(TextColors.WARNING + "test_complex START" + TextColors.ENDC, flush=True)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printInfo("Contracts button click")
		time.sleep(3)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printInfo("Add button click")
		time.sleep(7)
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(complex_contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		time.sleep(2)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		time.sleep(2)
		printInfo("Choose contract type")
		self.toolkit.fillAttributes(docDate=TakeDate.tomorrow)
		time.sleep(2)
		self.toolkit.clickByID("processID.stateID")
		# Ждём пока не появятся комментарии. Служит обозначением, что внутреннее тестирование началось
		self.toolkit.visibilityOfAnyElem('commentTextSystem')
		printInfo("Wait comment")
		time.sleep(2)
		# Отправляем на согласование
		self.toolkit.clickByXPATH(to_state_button_xpath % 'Отправить на согласование')
		time.sleep(2)
		# Берём ID документа
		doc_id = self.toolkit.takeDocID()
		printInfo("Take document ID")
		# ID документа созданного по шаблону (060 + ID документа)
		barcode_template_doc = "060" + doc_id
		printInfo("060 + doc_ID")
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addTestTemplateInFiles('Тест шаблон (1)')
		time.sleep(3)
		# Закрываем договор
		self.toolkit.clickByID('okb')
		printInfo("Close contract")
		time.sleep(3)
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ШТРИХ-КОД"""
		print(TextColors.WARNING + "BARCODE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Открываем подменю "Штрих-кода"
		self.toolkit.clickByXPATH(menu_button_xpath % 'Архив')
		printInfo("Barcode button click")
		# Нажимаем Архив
		time.sleep(1)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Работа с папками')
		printInfo("Archive button click")
		# Находим поле ввода
		time.sleep(1)
		self.toolkit.fillAttributes(barcode=barcode_folder_name)
		time.sleep(2)
		self.toolkit.clickByID('readBarcode')
		time.sleep(1)
		self.toolkit.fillAttributes(barcode=barcode_template_doc)
		time.sleep(2)
		self.toolkit.clickByID('readBarcode')
		# Спим (необходимо)
		time.sleep(1)
		# Проверка на наличие файлов
		self.toolkit.checkVisibility(archive_table_include_xpath)
		printInfo("Check for file")
		# Переключаемся на извлечение
		self.toolkit.clickByID('_removeDocument', "//div[@class='qx-radiobutton']")
		printInfo("Switch to extract")
		# Извлекаем
		self.toolkit.fillAttributes(barcode=barcode_template_doc)
		time.sleep(2)
		self.toolkit.clickByID('readBarcode')
		printInfo("Extract")
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОГОВОРЫ"""
		print(TextColors.WARNING + "CONTRACTS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printInfo("Contracts button click")
		# Спим
		time.sleep(3)
		# Переходим в договор
		self.toolkit.clickByXPATH(contracts_table_xpath)
		self.toolkit.clickByID('view')
		printInfo("Choose and move to contract")
		time.sleep(5)
		# Нажимаем кнопку с группой
		self.toolkit.clickByXPATH(test_group_button_xpath)
		printInfo("Group button click")
		# Нажимаем Делегировать
		self.toolkit.clickByXPATH(delegation_button_xpath)
		printInfo("Delegation button click")
		# Нажимаем Группа
		self.toolkit.clickByXPATH(group_button_xpath)
		time.sleep(2)
		printInfo("Employer button click")
		# Выбераем сотрудника
		self.toolkit.clickByXPATH(delegation_group_xpath, resetPointerEvents=True)
		printInfo("Choose employer")
		time.sleep(1)
		self.toolkit.clickByID('choose')
		time.sleep(1)
		# Закрываем окно с выбором сотрудников
		self.toolkit.clickByID('close')
		printInfo("Close window")
		# Спим
		time.sleep(10)
		# Добавление контрагента
		self.toolkit.addLinkage(("Заказчик", "Юр. лицо"), "Флексби Солюшнс")
		# TODO: Сделать проверку на инвизибл перед нажатием "удалить" !!!
		time.sleep(10)
		# Удаляем контрагента
		self.toolkit.clickByXPATH(delete_contragent_button_xpath)
		printInfo("Delete contragent")
		# Нажимаем Enter
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "CONTRACTS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(5)
		# Удалить договор
		self.toolkit.clickByID('deleteb')
		printInfo("Delete document")
		# Нажимаем Enter
		self.toolkit.clickByXPATH(ok_close_window_button_xpath)
		printInfo("ENTER click")
		time.sleep(5)
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_complex END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ComplexTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
