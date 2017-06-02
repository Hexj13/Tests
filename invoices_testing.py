# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class InvoicesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'InvoicesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_invoices(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_invoices START" + TextColors.ENDC, flush=True)
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Счета
		self.toolkit.clickByXPATH(menu_button_xpath % 'Счета')
		printOk("Activities button find&click")
		# Добавить
		self.toolkit.clickByID('new')
		printOk("Add button find&click")
		time.sleep(SleepSeconds.TWO)
		print("----------------------------------------", flush=True)

		""""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Вводим статью бюджета
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		# Выбираем статью бюджета
		self.toolkit.clickInPopupMenu(payment_plan_name)
		# Выбираем Договор
		self.toolkit.chooseReferenceInWindow('parentID', 'Подписан')
		# Добавляем Тег
		self.toolkit.addTag('Регулярный платильщик')
		# Описание
		self.toolkit.fillAttributes(subject=test_text)
		# Стрингуем Подписанта
		signer_position_name_u = str(signer_position_name)
		signer_name_u = str(signer_name)
		# Вводим подписанта
		self.toolkit.fillAttributes(signerID=signer_position_name_u)
		# Выбираем подписанта
		self.toolkit.clickInPopupMenu(signer_name_u)
		printOk("Choose signer")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Проставляем дату Акта
		self.toolkit.fillAttributes(statementDate=TakeDate.today)
		# Комментарий
		self.toolkit.addComment()
		# Добавляем Связь
		self.toolkit.addLinkage(('Заказчик', 'Юр. лицо'), 'Адидас')
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

		"""СПЕЦИФИКАЦИЯ"""
		print(TextColors.WARNING + "SPECIFICATION PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Спецификация
		self.toolkit.clickTab('Спецификация')
		printOk("Specification button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('createSpecification')
		printOk("Add specification button click")
		time.sleep(SleepSeconds.TWO)
		# Выбираем в деревьях ВСЕ
		self.toolkit.treeClick('Все')
		# Нажимаем карандаш через Enter
		self.toolkit.clickByXPATH(pencil_window_xpath)
		self.toolkit.clickByID('choose')
		printOk("Choose pencil from Enter")
		# Закрываем окно
		self.toolkit.clickByID('close')
		# Спим
		time.sleep(SleepSeconds.TWO)
		printOk("Close window")
		#
		print("", flush=True)
		print(TextColors.WARNING + "SPECIFICATION PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ПРЕДОПЛАТЫ"""
		print(TextColors.WARNING + "PREPAYMENTS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Предоплаты
		self.toolkit.clickTab('Предоплаты')
		printOk("Members button click")
		# Нажимаем Добавить
		self.toolkit.clickByXPATH(add_button_xpath)
		printOk("Add button click")
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_id_window_button_xpath)
		# Спим
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "PREPAYMENTS PAGE END" + TextColors.ENDC, flush=True)
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
		activities_type_name_u = str(activities_activity_type_name)
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
		# TODO: Сделать закрытие просмоторщика файлов через крестик после того, когда у него появится ID
		# self.toolkit.addTestTemplateInFiles('Пакет документов')
		print("", flush=True)
		print(TextColors.WARNING + "FILES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""Delete&Close"""
		print(TextColors.WARNING + "Delete&Close START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.delete_into_doc()
		print("", flush=True)
		print(TextColors.WARNING + "Delete&Close END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "test_invoices END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'InvoicesTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
