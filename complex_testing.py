# coding=utf-8
import unittest
from RootsLib.roots import *


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
		print("", flush=True)
		print(TextColors.WARNING + "setUp END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def test_complex(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_activities START" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("Contracts button click")
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.TWO)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(complex_contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose contract type")
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		self.toolkit.clickTab("Общее")
		# Ждём пока не появятся комментарии. Служит обозначением, что внутреннее тестирование началось
		self.toolkit.visibilityOfAnyElem('commentTextSystem')
		printOk("Wait comment")
		time.sleep(SleepSeconds.TWO)
		# Отправляем на согласование
		self.toolkit.clickByXPATH(to_matching_button_xpath)
		time.sleep(SleepSeconds.TWO)
		# Берём ID документа
		doc_id = self.toolkit.takeDocID()
		printOk("Take document ID")
		# ID документа созданного по шаблону (060 + ID документа)
		barcode_template_doc = "060" + doc_id
		printOk("060 + doc_ID")
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addTestTemplateInFiles('Тест шаблон (1)')
		time.sleep(SleepSeconds.TWO)
		# Закрываем договор
		self.toolkit.clickByID('okb')
		printOk("Close contract")
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ШТРИХ-КОД"""
		print(TextColors.WARNING + "BARCODE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Открываем подменю "Штрих-кода"
		self.toolkit.clickByXPATH(menu_button_xpath % 'Штрих-код')
		printOk("Barcode button click")
		# Нажимаем Архив
		time.sleep(SleepSeconds.ONE)
		self.toolkit.clickByXPATH(menu_button_xpath % 'Архив')
		printOk("Archive button click")
		# Находим поле ввода
		time.sleep(SleepSeconds.ONE)
		self.toolkit.fillAttributes(barcode=barcode_folder_name)
		time.sleep(SleepSeconds.TWO)
		self.toolkit.clickByID('readBarcode')
		time.sleep(SleepSeconds.ONE)
		self.toolkit.fillAttributes(barcode=barcode_template_doc)
		time.sleep(SleepSeconds.TWO)
		self.toolkit.clickByID('readBarcode')
		# Спим (необходимо)
		time.sleep(SleepSeconds.ONE)
		# Проверка на наличие файлов
		self.toolkit.checkVisibility(archive_table_include_xpath)
		printOk("Check for file")
		# Переключаемся на извлечение
		self.toolkit.clickByID('_removeDocument', "//div[@class='qx-radiobutton']")
		printOk("Switch to extract")
		# Извлекаем
		self.toolkit.fillAttributes(barcode=barcode_template_doc)
		time.sleep(SleepSeconds.TWO)
		self.toolkit.clickByID('readBarcode')
		printOk("Extract")
		print("", flush=True)
		print(TextColors.WARNING + "FILES END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОГОВОРЫ"""
		print(TextColors.WARNING + "CONTRACTS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("Contracts button click")
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Переходим в договор
		self.toolkit.clickByXPATH(contracts_table_xpath)
		self.toolkit.clickByID('view')
		printOk("Choose and move to contract")
		# Нажимаем кнопку с группой
		self.toolkit.clickByXPATH(test_group_button_xpath)
		printOk("Group button click")
		# Нажимаем Делегировать
		self.toolkit.clickByXPATH(delegation_button_xpath)
		printOk("Delegation button click")
		# Нажимаем Группа
		self.toolkit.clickByXPATH(group_button_xpath)
		time.sleep(SleepSeconds.TWO)
		printOk("Employer button click")
		# Выбераем сотрудника
		self.toolkit.clickByXPATH(delegation_group_xpath)
		printOk("Choose employer")
		time.sleep(SleepSeconds.ONE)
		self.toolkit.clickByID('choose')
		time.sleep(SleepSeconds.ONE)
		# Закрываем окно с выбором сотрудников
		self.toolkit.clickByID('close')
		printOk("Close window")
		# Спим
		time.sleep(SleepSeconds.TEN)
		# Добавление контрагента
		self.toolkit.addLinkage(("Заказчик", "Юр. лицо"), "Флексби Солюшнс")
		# TODO: Сделать проверку на инвизибл перед нажатием "удалить" !!!
		time.sleep(SleepSeconds.TEN)
		# Удаляем контрагента
		self.toolkit.clickByXPATH(delete_contragent_button_xpath)
		printOk("Delete contragent")
		# Нажимаем Enter
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "CONTRACTS END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.FIVE)
		# Удалить договор
		self.toolkit.clickByID('deleteb')
		printOk("Delete document")
		# Нажимаем Enter
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("ENTER click")
		time.sleep(SleepSeconds.FIVE)
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_activities END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ComplexTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
