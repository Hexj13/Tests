# coding=utf-8
# noinspection PyUnresolvedReferences
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class RequestsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'RequestsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_requests(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_requests START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим в меню Заявки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Заявки')
		printOk("Activities button find&click")
		time.sleep(2)
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(4)
		print("", flush=True)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID='Запрос справки')
		time.sleep(2)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu('Запрос справки')
		printOk("Choose type")
		time.sleep(3)
		# Добавляем Тег
		self.toolkit.addTag('Срочно')
		# Вводим дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(1)
		self.toolkit.action.send_keys(Keys.ENTER)
		self.toolkit.action.perform()
		time.sleep(1)
		# Описание
		self.toolkit.fillAttributes(subject=test_text)
		# Комментарий
		self.toolkit.addComment()
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addMembersAndDelete()
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addSimpleActivity()
		print("", flush=True)
		print(TextColors.WARNING + "ACTIVITY END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addTestFolderInFiles()
		print("", flush=True)
		print(TextColors.WARNING + "FILES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Удаить договор
		self.toolkit.delete_into_doc()
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_requests END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'RequestsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
