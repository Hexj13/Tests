# coding=utf-8
import unittest

from RootsLib.roots import *


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
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Заявки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Заявки')
		printOk("Activities button find&click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Добавляем Тег
		self.toolkit.addTag('Срочно')
		# Вводим дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Описание
		self.toolkit.fillAttributes(subject=test_text)
		# Комментарий
		self.toolkit.addComment()
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addMembers()
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Активности
		self.toolkit.clickTab('Активности')
		printOk("Activities button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Вводим тип Активности
		activities_type_name_u = str(activities_activity_type_name)
		self.toolkit.fillAttributes(documentTypeID=activities_type_name_u)
		time.sleep(SleepSeconds.THREE)
		# Выбираем тип Активности
		self.toolkit.clickInPopupMenu(activities_type_name_u)
		printOk("Choose activity type")
		time.sleep(SleepSeconds.FIVE)
		# Нажимаем OK
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		time.sleep(SleepSeconds.TWO)
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
		self.toolkit.clickByID('deleteb')
		printOk("Delete document")
		# Нажимаем Enter
		self.toolkit.clickByXPATH(ok_button_window_xpath)
		printOk("ENTER click")
		time.sleep(SleepSeconds.FIVE)
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_requests END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'RequestsTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
