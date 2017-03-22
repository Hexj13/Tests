# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class OrdersTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'OrdersTesting' START" + TextColors.ENDC, flush=True)
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

	def test_orders(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_orders START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Переходим в Заказы
		self.toolkit.clickByXPATH(menu_button_xpath % 'Заказы')
		printOk("ORDERS button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.TWO)
		# Проставляем дату документа
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		# Добавляем тег
		self.toolkit.addTag(order_tag_name)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Комментарий
		self.toolkit.addComment()
		# Проставляем Описание
		self.toolkit.fillAttributes(subject=comment_text)
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
		# Добавляем Связь
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
		time.sleep(SleepSeconds.TWO)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL PAGE END" + TextColors.ENDC, flush=True)
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
		# Нажимаем карандаш через Enter
		self.toolkit.clickByXPATH(pencil_window_xpath)
		self.toolkit.clickByID('choose')
		printOk("Choose pencil")
		# Закрываем окно
		self.toolkit.clickByID('close')
		# Спим
		time.sleep(SleepSeconds.TWO)
		printOk("Close window")
		#
		print("", flush=True)
		print(TextColors.WARNING + "SPECIFICATION PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ГРАФИК ПЛАТЕЖЕЙ"""
		print(TextColors.WARNING + "PAYMENT SCHEDULE PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем График Платежей
		self.toolkit.clickTab('График платежей')
		printOk("Payment schedule button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.TWO)
		# Вводим Переодичность
		payment_period_name_u = str(payment_period_name)
		self.toolkit.fillAttributes(paymentPeriodID=payment_period_name_u)
		self.toolkit.clickInPopupMenu(payment_period_name_u)
		printOk("Choose payment period")
		time.sleep(SleepSeconds.ONE)
		# Вводим Статью бюджета
		payment_plan_name_u = str(payment_plan_name)
		self.toolkit.fillAttributes(planTypeID=payment_plan_name_u)
		self.toolkit.clickInPopupMenu(payment_plan_name_u)
		printOk("Enter payment plan")
		time.sleep(SleepSeconds.ONE)
		# Вводим Итого
		self.toolkit.fillAttributes(cost=payment_cost_name)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_id_window_button_xpath)
		printOk("OK button click")
		time.sleep(SleepSeconds.ONE)
		print("", flush=True)
		print(TextColors.WARNING + "PAYMENT SCHEDULE PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СЧЕТА"""
		print(TextColors.WARNING + "INVOICES PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Счета
		self.toolkit.clickTab('Счета')
		printOk("Invoices button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.THREE)
		# Закрываем счёт
		self.toolkit.clickByID('okb')
		printOk("Invoices close")
		# Спим
		time.sleep(SleepSeconds.THREE)
		print("", flush=True)
		print(TextColors.WARNING + "INVOICES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		activities_type_name_u = str(activities_activity_type_name)
		# Нажимаем Активности
		self.toolkit.clickTab('Активности')
		printOk("Activities button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Вводим тип Активности
		self.toolkit.fillAttributes(documentTypeID=activities_type_name_u)
		time.sleep(SleepSeconds.THREE)
		# Выбираем тип Активности
		self.toolkit.clickInPopupMenu(activities_type_name_u)
		printOk("Choose activity type")
		time.sleep(SleepSeconds.FIVE)
		# Нажимаем OK
		self.toolkit.clickByID('okb')
		time.sleep(SleepSeconds.TWO)
		printOk("OK button click")
		print("", flush=True)
		print(TextColors.WARNING + "ACTIVITY PAGE END" + TextColors.ENDC, flush=True)
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
		# Удаляем Счёт
		self.toolkit.deleteObj('Счета')
		printOk("Delete Invoices")
		time.sleep(SleepSeconds.FOUR)
		# Удаляем Активность
		self.toolkit.deleteObj('Активности')
		printOk("Delete Activity")
		time.sleep(SleepSeconds.FOUR)
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
		print(TextColors.WARNING + "test_orders END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'OrdersTesting' FINISH" + TextColors.ENDC, flush=True)


if __name__ == '__main__':
	unittest.main()
