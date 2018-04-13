# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class ActivitiesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ActivitiesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_activities(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_activities START" + TextColors.ENDC, flush=True)
		# Находим в меню Активности
		self.toolkit.clickByXPATH(menu_button_xpath % 'Активности')
		printOk("Activities button find&click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(2)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(2)
		# Вводим в поле типа Активности текст
		activities_type_name_u = str(activities_activity_type_name)
		self.toolkit.fillAttributes(documentTypeID=activities_type_name_u)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(activities_type_name_u)
		printOk("Choose activity type")
		# # Проставляем дату диактивации
		# self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# # Вводим Описание
		# self.toolkit.fillAttributes(subject=test_text)
		# # Комментарий
		# self.toolkit.addComment()
		# Выбор Ответственного
		self.toolkit.chooseReferenceInWindow('responsibleID', 'Прокофьев Андрей Викторович')
		time.sleep(1)
		# Добавляем тег
		self.toolkit.addTag(activities_tag_name)
		# Добавляем Связь
		self.toolkit.addLinkage('Компания', 'Флексби Солюшнс')
		self.toolkit.clickByID('close')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addMember(name='Генеральный директор', first_group_name='Инициатор')
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

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE LINKS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("Shadow delete")
		# Удаляем Активность
		self.toolkit.deleteObj('Активности')
		time.sleep(2)
		printOk("Delete activity")
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
		print(TextColors.WARNING + "test_activities END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ActivitiesTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
