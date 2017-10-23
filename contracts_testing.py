# coding=utf-8
import unittest

from rootsLib.roots import *


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
		time.sleep(2)
		# Переходим в Договоры
		self.toolkit.clickByXPATH(menu_button_xpath % 'Договоры')
		printOk("ORDERS button click")
		# Спим
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(6)
		print("----------------------------------------", flush=True)

		"""ОБЩЕЕ"""
		print(TextColors.WARNING + "GENERAL PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Находим поле Типа документа и Вводим тип
		contract_type_name = str(contracts_type_name)
		self.toolkit.fillAttributes(documentTypeID=contract_type_name)
		# Находим и нажимаем в списке нужный тип документа
		time.sleep(2)
		self.toolkit.clickInPopupMenu(contract_type_name)
		printOk("Choose type")
		time.sleep(5)
		# Проставляем дату документа
		self.toolkit.clickByID('docDate')
		time.sleep(1)
		self.toolkit.fillAttributes(docDate=TakeDate.today)
		time.sleep(1)
		self.toolkit.action.send_keys(Keys.ENTER)
		time.sleep(1)
		self.toolkit.fillAttributes(subject=test_text)
		time.sleep(4)
		# Добавляем тег
		self.toolkit.addTag('FAIL')
		# Проверяем на отсутвие shadow
		time.sleep(1)
		self.toolkit.waitNoShadow()
		printOk("NO shadow")
		# Комментарий
		time.sleep(1)
		self.toolkit.addComment()
		# Отправляем на согласование
		self.toolkit.clickByID('_processID_process_panel', "//div[text()='Отправить на согласование']")
		time.sleep(3)
		# Стрингуем Подписанта
		signer_position_name_u = str(signer_position_name)
		signer_name_u = str(signer_name)
		time.sleep(1)
		# Вводим подписанта
		self.toolkit.fillAttributes(signerID=signer_position_name_u)
		time.sleep(2)
		# Выбираем подписанта
		self.toolkit.clickInPopupMenu(signer_name_u)
		printOk("Choose signer")
		# Спим
		time.sleep(2)
		# Добавляем Связь
		self.toolkit.addLinkage(("Заказчик", 'Юр. лицо'), 'Флексби Солюшнс')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GENERAL PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""УЧАСТНИКИ"""
		print(TextColors.WARNING + "MEMBERS PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addMembersAndDelete('Инициатор', 'Согласователь')
		print("", flush=True)
		print(TextColors.WARNING + "MEMBERS PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ГРАФИК ПЛАТЕЖЕЙ"""
		print(TextColors.WARNING + "PAYMENT SCHEDULE PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(1)
		# Нажимаем График Платежей
		self.toolkit.clickTab('График платежей')
		printOk("Payment schedule button click")
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		time.sleep(4)
		# Вводим Переодичность
		self.toolkit.fillAttributes(paymentPeriodID=payment_period_name)
		time.sleep(1)
		self.toolkit.clickInPopupMenu(payment_period_name)
		printOk("Choose payment period")
		time.sleep(1)
		# Вводим Статью бюджета
		self.toolkit.fillAttributes(planTypeID=payment_plan_name)
		self.toolkit.clickInPopupMenu(payment_plan_name)
		printOk("Enter payment plan")
		time.sleep(1)
		self.toolkit.clickByID('cost')
		time.sleep(1)
		# Вводим Итого
		self.toolkit.clearByID('cost', '//input')
		time.sleep(1)
		#
		self.toolkit.fillAttributes(cost=payment_cost_name)
		#
		self.toolkit.fillAttributes(comment=test_text)
		# Спим
		time.sleep(2)
		# Нажимаем ОК
		self.toolkit.clickByXPATH(ok_id_window_button_xpath)
		printOk("OK button click")
		time.sleep(1)
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
		time.sleep(5)
		# Выбираем в деревьях ВСЕ
		self.toolkit.treeClick('Все')
		# Нажимаем карандаш через Enter
		self.toolkit.clickByXPATH(pencil_window_xpath)
		self.toolkit.clickByID('choose')
		printOk("Choose button click")
		# Закрываем окно
		self.toolkit.clickByID('close')
		# Спим
		time.sleep(2)
		printOk("Close window")
		#
		print("", flush=True)
		print(TextColors.WARNING + "SPECIFICATION PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""СЧЕТА"""
		print(TextColors.WARNING + "INVOICES PAGE START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addSimpleInvoice()
		print("", flush=True)
		print(TextColors.WARNING + "INVOICES PAGE END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ЗАКАЗЫ"""
		print(TextColors.WARNING + "ORDER START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addSimpleOrder()
		print("", flush=True)
		print(TextColors.WARNING + "ORDER END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""АКТИВНОСТИ"""
		print(TextColors.WARNING + "ACTIVITY START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		self.toolkit.addSimpleActivity()
		print("", flush=True)
		print(TextColors.WARNING + "ACTIVITY END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""ДОП.СОГЛАШЕНИЯ"""
		print(TextColors.WARNING + "SUPPLEMENT START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Нажимаем Доп. соглашения
		self.toolkit.clickTab('Доп. соглашения')
		printOk("Activities button click")
		time.sleep(2)
		# Нажимаем Добавить
		self.toolkit.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(6)
		# Проставляем дату документа
		self.toolkit.fillAttributes(docDate=TakeDate.tomorrow)
		time.sleep(2)
		# Проставляем дату диактивации
		self.toolkit.fillAttributes(deactivateDate=TakeDate.tomorrow)
		time.sleep(2)
		# Нажимаем OK
		self.toolkit.clickByID('okb')
		printOk("OK button click")
		time.sleep(4)
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
		time.sleep(2)
		printOk("Delete invoices")
		# Удаляем Заказы
		self.toolkit.deleteObj('Заказы')
		time.sleep(2)
		printOk("Delete orders")
		# Удаляем Активности
		self.toolkit.deleteObj('Активности')
		time.sleep(2)
		printOk("Delete activity")
		# Удаляем Доп. соглашения
		self.toolkit.deleteObj('Доп. соглашения')
		time.sleep(4)
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
