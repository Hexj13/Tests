# coding=utf-8
import unittest

from RootsLib.roots import *


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
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Активности
		self.toolkit.clickByXPATH(menu_button_xpath % 'Активности')
		printOk("Activities button find&click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(SleepSeconds.TWO)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.TWO)
		# Вводим в поле типа Активности текст
		activities_type_name_u = str(activities_activity_type_name)
		self.toolkit.fillAttributes(documentTypeID=activities_type_name_u)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(activities_type_name_u)
		printOk("Choose activity type")
		# Проставляем дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Вводим Описание
		self.toolkit.fillAttributes(subject=test_text)
		# Комментарий
		self.toolkit.addComment()
		# Выбор Ответственного
		self.toolkit.chooseReferenceInWindow('responsibleID', 'Генеральный директор')
		time.sleep(SleepSeconds.ONE)
		# Добавляем тег
		self.toolkit.addTag(activities_tag_name)
		# Добавляем Связь
		self.toolkit.addLinkage('Компания', 'Флексби Солюшнс')
		self.toolkit.clickByID('close')
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Участники
		self.toolkit.clickTab('Участники')
		printOk("Members button click")
		# Нажимаем Добавить
		self.toolkit.clickByXPATH(add_button_xpath)
		printOk("Add button click")
		# Нажимаем Инициатор
		self.toolkit.clickByXPATH(qx_menu_menu_select_xpath % 'Инициатор')
		# Нажимаем Должность
		self.toolkit.clickByXPATH(qx_menu_menu_select_xpath % 'Сотрудник')
		printOk("Position button click")
		# Выбираем Генерального директора
		self.toolkit.clickByXPATH(cell_in_table_xpath % 'Генеральный директор')
		self.toolkit.clickByID('choose')
		printOk("Choose director")
		# Нажимаем закрыть окно
		self.toolkit.clickByID('close')
		printOk("Close window")
		# Спим
		time.sleep(SleepSeconds.TWO)
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
		time.sleep(SleepSeconds.FIVE)
		# Вводим тип Активности
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

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE LINKS START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("Shadow delete")
		# Удаляем Активность
		self.toolkit.deleteObj('Активности')
		time.sleep(SleepSeconds.TWO)
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
