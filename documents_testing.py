# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class DocumentsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'DocumentsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_documents(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_documents START" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(2)
		# Находим в меню Счета
		self.toolkit.clickByXPATH(menu_button_xpath % 'Документы')
		printOk("Documents button find&click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(2)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		document_type_name = 'Входящий'
		self.toolkit.fillAttributes(documentTypeID=document_type_name)
		# Находим и нажимаем в списке нужный тип документа
		time.sleep(2)
		self.toolkit.clickInPopupMenu(document_type_name)
		printOk("Choose type")
		time.sleep(5)
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		time.sleep(1)
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		time.sleep(1)
		self.toolkit.action.send_keys(Keys.ENTER)
		time.sleep(1)
		#
		self.toolkit.fillAttributes(subject=test_text)
		time.sleep(1)
		#
		self.toolkit.fillAttributes(activateDate=TakeDate.today)
		time.sleep(1)
		#
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(1)
		# Добавляем Связь
		self.toolkit.addLinkage('Юр. лицо', 'Флексби Солюшнс')
		time.sleep(3)
		# Комментарий
		self.toolkit.addComment()
		# Добавляем Тег
		self.toolkit.addTag('Testing')
		# Отправляем на подписание
		self.toolkit.clickByXPATH(to_state_button_xpath % 'Подписание')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addMember("Тестовый Сотрудник", first_group_name='Исполнитель')
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ_2"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Участники
		self.toolkit.clickTab('Общее')
		printOk("Members button click")
		# Отправляем в Подписан
		self.toolkit.clickByXPATH(to_state_button_xpath % 'Подписан')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ_2"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.deleteMember('Исполнитель')
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОКУМЕНТЫ"""
		print(TextColors.WARNING + "Related documents PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Связанные документы
		self.toolkit.clickTab('Документы')
		printOk("Related documents button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(3)
		# Закрываем связанные документы
		self.toolkit.clickByID('okb')
		printOk("Related documents close")
		# Спим
		time.sleep(4)
		print("", flush=True)
		print(TextColors.WARNING + "Related documents PAGE END" + TextColors.ENDC, flush=True)
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
		# Удаляем связанный документ
		self.toolkit.deleteObj('Документы')
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
		print(TextColors.WARNING + "test_documents END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'DocumentsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
