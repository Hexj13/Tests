# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class OpportunitiesTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'OpportunitiesTesting' START" + TextColors.ENDC, flush=True)
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

	def test_opportunities(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_opportunities START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проваливаемся на сайт
		time.sleep(SleepSeconds.TWO)
		# Находим в меню Продажи
		self.toolkit.clickByXPATH(menu_button_xpath % 'Продажи')
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
		# Вводим статью бюджета
		self.toolkit.fillAttributes(documentTypeID=sales_type_name)
		# Выбираем статью бюджета
		self.toolkit.clickInPopupMenu(sales_type_name)
		# Добавляем Тег
		self.toolkit.addTag('event')
		# Описание
		self.toolkit.fillAttributes(subject=test_text)
		# Вводим e-mail
		self.toolkit.fillAttributes(email=email_text)
		# Вводим deactivate date
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		# Выбираем Процент
		self.toolkit.clearByID("percent", "//input")
		printOk("Choose signer")
		# Проставляем процент
		self.toolkit.fillAttributes(percent=50)
		time.sleep(SleepSeconds.TWO)
		# Проставляем цену
		self.toolkit.fillAttributes(cost=100000)
		# Комментарий
		self.toolkit.addComment()
		# Добавляем Автивность и удаляем
		self.toolkit.addActivity()
		# Добавляем Связь
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
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
		# Нажимаем Сотрудник
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
		time.sleep(SleepSeconds.THREE)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose type")
		# Спим
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		self.toolkit.fillAttributes(docDate=TakeDate.today)
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
		# Удаляем Договор
		self.toolkit.deleteObj('Договоры')
		printOk("Delete Contract")
		# Удаляем Заказ
		self.toolkit.deleteObj('Заказы')
		printOk("Delete Order")
		print("", flush=True)
		print(TextColors.WARNING + "DELETE LINKS END" + TextColors.ENDC, flush=True)
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
		print(TextColors.WARNING + "test_opportunities END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'OpportunitiesTesting' FINISH" + TextColors.ENDC, flush=True, end="")


if __name__ == '__main__':
	unittest.main()
