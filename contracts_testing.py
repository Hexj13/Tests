# coding=utf-8
import unittest

from RootsLib.roots import *


# noinspection PyUnusedLocal
class ContractsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'ContractsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_contracts(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_contracts START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("ORDERS button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.SIX)
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		time.sleep(SleepSeconds.TWO)
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose type")
		time.sleep(SleepSeconds.FIVE)
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		time.sleep(SleepSeconds.ONE)
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		time.sleep(SleepSeconds.ONE)
		self.toolkit.action.send_keys(Keys.ENTER)
		time.sleep(SleepSeconds.ONE)
		self.toolkit.fillAttributes(subject=test_text)
		time.sleep(SleepSeconds.FOUR)
		# Добавляем тег
		self.toolkit.addTag('FAIL')
		# Проверяем на отсутвие shadow
		time.sleep(SleepSeconds.ONE)
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Комментарий
		time.sleep(SleepSeconds.ONE)
		self.toolkit.addComment()
		# Отправляем на согласование
		self.toolkit.clickByID('_processID_process_panel', "//div[text()='Отправить на согласование']")
		time.sleep(SleepSeconds.THREE)
		# Стрингуем Подписанта
		signer_position_name_u = str(signer_position_name)
		signer_name_u = str(signer_name)
		time.sleep(SleepSeconds.ONE)
		# Вводим подписанта
		self.toolkit.fillAttributes(signerID=signer_position_name_u)
		time.sleep(SleepSeconds.TWO)
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
		self.toolkit.addMembers('Инициатор', 'Согласователь')
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ГРАФИК ПЛАТЕЖЕЙ"""
		print(TextColors.WARNING + "PAYMENT SCHEDULE PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.ONE)
		# Нажимаем График Платежей
		self.toolkit.clickTab('График платежей')
		printOk("Payment schedule button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(SleepSeconds.FOUR)
		# Вводим Переодичность
		self.toolkit.fillAttributes(paymentPeriodID=payment_period_name)
		time.sleep(SleepSeconds.ONE)
		self.toolkit.clickInPopupMenu(payment_period_name)
		printOk("Choose payment period")
		time.sleep(SleepSeconds.ONE)
		# Вводим Статью бюджета
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		self.toolkit.clickInPopupMenu(payment_plan_name)
		printOk("Enter payment plan")
		time.sleep(SleepSeconds.ONE)
		self.toolkit.clickByID('cost')
		time.sleep(SleepSeconds.ONE)
		# Вводим Итого
		self.toolkit.clearByID('cost', '//input')
		time.sleep(SleepSeconds.ONE)
		#
		self.toolkit.fillAttributes(cost=payment_cost_name)
		#
		self.toolkit.fillAttributes(comment=test_text)
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_id_window_button_xpath)
		printOk("OK button click")
		time.sleep(SleepSeconds.ONE)
		print("", flush=True)
		print(TextColors.WARNING + "PAYMENT SCHEDULE PAGE END" + TextColors.ENDC, flush=True)
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
		time.sleep(SleepSeconds.FIVE)
		# Выбираем в деревьях ВСЕ
		self.toolkit.treeClick('Все')
		# Нажимаем карандаш через Enter
		self.toolkit.clickByXPATH(pencil_window_xpath)
		self.toolkit.clickByID('choose')
		printOk("Choose button click")
		# Закрываем окно
		self.toolkit.clickByID('close')
		# Спим
		time.sleep(SleepSeconds.TWO)
		printOk("Close window")
		#
		print("", flush=True)
		print(TextColors.WARNING + "SPECIFICATION PAGE END" + TextColors.ENDC, flush=True)
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
		time.sleep(SleepSeconds.FOUR)
		print("", flush=True)
		print(TextColors.WARNING + "INVOICES PAGE END" + TextColors.ENDC, flush=True)
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
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		# Спим
		time.sleep(SleepSeconds.FIVE)
		# Закрываем заказ
		self.toolkit.clickByID('okb')
		printOk("Close order")
		time.sleep(SleepSeconds.FOUR)
		print("", flush=True)
		print(TextColors.WARNING + "ORDER END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Активности
		self.toolkit.clickTab('Активности')
		printOk("Activities button click")
		time.sleep(SleepSeconds.TWO)
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
		time.sleep(SleepSeconds.FOUR)
		print("", flush=True)
		print(TextColors.WARNING + "ACTIVITY END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОП.СОГЛАШЕНИЯ"""
		print(TextColors.WARNING + "SUPPLEMENT START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Доп. соглашения
		self.toolkit.clickTab('Доп. соглашения')
		printOk("Activities button click")
		time.sleep(SleepSeconds.TWO)
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(SleepSeconds.SIX)
		# Проставляем дату документа
		self.toolkit.fillAttributes(docDate=TakeDate.tomorrow)
		time.sleep(SleepSeconds.TWO)
		# Проставляем дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(SleepSeconds.TWO)
		# Нажимаем OK
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		time.sleep(SleepSeconds.FOUR)
		print("", flush=True)
		print(TextColors.WARNING + "SUPPLEMENT END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ФАЙЛЫ"""
		print(TextColors.WARNING + "FILES PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Добавляем Папку
		self.toolkit.addTestFolderInFiles()
		# Добавляем Шаблон
		self.toolkit.addTestTemplateInFiles('Сопроводительная записка')
		print("", flush=True)
		print(TextColors.WARNING + "FILES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE LINKS START" + TextColors.ENDC, flush=True)
		# Проверяем на отсутвие shadow
		self.toolkit.waitNoShadow()
		printOk("Shadow NO")
		# Удаляем Счета
		self.toolkit.deleteObj('Счета')
		time.sleep(SleepSeconds.TWO)
		printOk("Delete invoices")
		# Удаляем Заказы
		self.toolkit.deleteObj('Заказы')
		time.sleep(SleepSeconds.TWO)
		printOk("Delete orders")
		# Удаляем Активности
		self.toolkit.deleteObj('Активности')
		time.sleep(SleepSeconds.TWO)
		printOk("Delete activity")
		# Удаляем Доп. соглашения
		self.toolkit.deleteObj('Доп. соглашения')
		time.sleep(SleepSeconds.FOUR)
		printOk("Delete supplement")
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
		print(TextColors.WARNING + "test_contracts END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'ContractsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
