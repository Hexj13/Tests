# coding=utf-8
import datetime
import time

from rootsLib.content import *
from rootsLib.xpath import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Вывод и подцветка в лог
def printOk(text):
	try:
		print(str(text) + " " + "---->" + " " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
	except:
		pass


# Получение даты и форматирование
class TakeDate:
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today = today.strftime("%d.%m.%Y")
	tomorrow = tomorrow.strftime("%d.%m.%Y")


# Цвета для подцветки кода и вывода
class TextColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


# Основной класс для работы с интерфейсом Flexbby
# Сортировано по типу взаимодействия
class UITestToolkit(object):
	def __init__(self):
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "UITestToolkit init START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		chrome_options = Options()
		chrome_options.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		printOk("Webdriver init")
		# Разворачиваем
		self.driver.maximize_window()
		printOk("Maximize window")
		# Подключаем webdriver
		self.wait = WebDriverWait(self.driver, 120)
		printOk("WebDriverWait init")
		# Подключаем action
		self.action = action_chains.ActionChains(self.driver)
		printOk("ActionChains init")
		print("", flush=True)
		print(TextColors.WARNING + "UITestToolkit init FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	"""BASIC"""

	# Передаёт текст по указанному xpath. Проверяет элемент на тип: input, textarea и вложение в div на данный тип, после чего и передаёт ввод текста.
	def sendKeysByXPATH(self, xpath, keys):
		el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
		if el.tag_name == 'input':
			el.send_keys(keys)
		elif el.tag_name == 'textarea':
			el.send_keys(keys)
		elif el.tag_name == 'div':
			el = el.find_element_by_xpath(".//input")
			if el != None:
				el.send_keys(keys)
		elif el.tag_name == 'div':
			el = el.find_element_by_xpath(".//textarea")
			if el != None:
				el.send_keys(keys)
		else:
			print(TextColors.FAIL + 'Error to find element' + TextColors.ENDC)

	# Передаёт данные (нажатие, текст) в элемент по id (можно указать xpath родителя и/или ребёнка)
	def fillAttributes(self, parent_xpath='', child_xpath='', **kwargs):
		for k, v in kwargs.items():
			self.sendKeysByXPATH(attribute_xpath.format(child=child_xpath, parent=parent_xpath, id=k), v)
			printOk("Enter " + k)

	# Выбирает (клик) строку по тексту
	def selectRowInTable(self, contains_text=''):
		self.clickByXPATH(attribute_xpath.format(text=contains_text))

	# Очищает поле и вносит данные по id элемента
	def inputByID(self, element_id, text):
		search_element = self.driver.find_element_by_id(element_id)
		printOk("Find element by ID == '" + TextColors.BOLD + element_id + TextColors.ENDC + "'")
		search_element.clear()
		printOk("Clear")
		search_element.send_keys(text)
		printOk("Enter text == '" + TextColors.BOLD + text + TextColors.ENDC + "'")

	# Проверяет видимость элемента на стейдже по id элемента
	def visibilityOfAnyElem(self, docID):
		self.wait.until(EC.visibility_of_any_elements_located((By.ID, docID)))

	# Находит(делает фокус) ячейку в таблице с текстом
	def findElement(self, text):
		self.driver.find_element_by_xpath(cell_in_table_xpath % text).location_once_scrolled_into_view()

	# Очищает поле по id
	def clearByID(self, element_id, child_xpath='', parent_xpath=''):
		self.driver.find_element_by_xpath(
			attribute_xpath.format(parent=parent_xpath, child=child_xpath, id=element_id)).clear()

	# Заглушка для ощибок выводимых системой
	def waitNoShadow(self):
		self.wait.until(EC.invisibility_of_element_located((By.ID, 'shadow')))
		time.sleep(2)

	# Проверяет визибилити элемента. Использовано element_to_be_clickable для проверки не только на визибил но и на вохможность взаимодействия
	def checkVisibility(self, xpath):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

	# Парсит URL и берёт внутренний id документа
	def takeDocID(self):
		url = self.driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		obj_id = params['id']
		return obj_id

	# Закрытие браузера
	def quit(self):
		self.driver.quit()

	# Выбор "Ответственного" в окне настроек. Необходимо передавать id поля куда нужно проставить ответсвенного и его ФИО.
	def chooseReferenceInWindow(self, reference_id, text):
		# Нажимаем на кнопку для выбора договора
		self.clickByID(reference_id, "//div[@id = 'choose-button']")
		printOk("Select button click")
		time.sleep(4)
		# Выбираем объект
		self.clickByID('filter', parent_xpath="//div[@class='qx-window']")
		printOk("Filter click")
		time.sleep(1)
		# Проставляем значение в поле
		self.sendKeysByXPATH("//div[@class='qx-popup']//input", text)
		time.sleep(1)
		# Выбираем
		self.clickByXPATH(reference_obj_xpath.format(text=text))
		time.sleep(1)
		self.clickByID('choose')
		printOk("Choose contract")

	# Логин в систему. Принимает логин и пароль
	def login(self, login, password):
		print(TextColors.WARNING + "login START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(1)
		# Чистим и запоняем логин
		self.clearByID('login')
		self.fillAttributes(login=login)
		# Запоняем пароль
		self.fillAttributes(password=password)
		self.clickByID('enter')
		printOk("Submit button click")
		time.sleep(8)
		print("", flush=True)
		print(TextColors.WARNING + "login FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	# Заполняет поля параметров в документе
	def fillParameter(self, param_name, input_text):
		# Находим в столбце с названиями параметров нужный и возвращаем его третьего родителя
		param_line = self.driver.find_element_by_xpath(
			"//div[@id='DocumentParameterValue_objectID']//parent::div[@class='qx-table-row']//span[text()='%s']" % param_name
		).find_element_by_xpath('../../..')
		printOk("Find target row with name = " + TextColors.HEADER + param_name + TextColors.ENDC)
		# Находим всю строчку
		rows = param_line.find_elements_by_xpath('../*')
		# Добавляем единицу к индексу. Необходимо будет для определения соответвующей строчки напротив строки с названием.
		indexOfTarget = rows.index(param_line) + 1
		printOk("Index of target = " + TextColors.HEADER + str(indexOfTarget) + TextColors.ENDC)
		time.sleep(1)
		# Находим ячейку значения
		value_clm = "//div[@id='DocumentParameterValue_objectID']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[%s]/div[1]" % indexOfTarget  # <---- %s передавать indexOfTarget
		time.sleep(1)
		# Клип по ячейке для активации
		self.clickByXPATH(value_clm)
		printOk("Click on 'Value' column")
		time.sleep(1)
		# Внутри ячейки находим инпут и проставляем значение
		self.driver.find_element_by_xpath(
			"//div[@id='DocumentParameterValue_objectID']//div[@class='qx-table-scroller-focus-indicator']//input").send_keys(
			input_text)
		printOk('Send keys')
		time.sleep(2)
		# Enter
		self.action.send_keys(Keys.ENTER)
		printOk('Enter click')
		# Нажимаем кнопку Добавить Комментарий
		self.clickByID('newCommentButton')
		printOk("Add Comment button click")
		# Вводим первый комментарий
		self.fillAttributes(commentInput='Параметр ' + param_name + ' был заполнен')
		# Нажимаем Сохранить
		self.clickByID('saveComment')
		printOk("Save button click")
		time.sleep(1)

	# Создаёт новый реквизит в Юр.лицах и заполняет поля через словарь. Использую в addBankAccount
	def createSimpleBankObject(self, **kwargs):
		# Нажимаем Добавить
		self.clickByID('BankAccount_objectID', '//div[@id="new"]')
		printOk("Add button click")
		self.fillAttributes(bik=kwargs.pop('bik'))
		self.fillAttributes(**kwargs)
		# Нажимаем ОК
		time.sleep(1)
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")

	# Передаёт ссылку в браузер.
	def setSite(self, url):
		self.driver.get(url)
		print(
			"Get URL = " + TextColors.UNDERLINE + url + TextColors.ENDC + " ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		print("----------------------------------------", flush=True)

	""""ADD ELEMENT"""

	# Добавляет комметарий в документе
	def addComment(self):
		# Нажимаем кнопку Добавить Комментарий
		self.clickByID('newCommentButton')
		printOk("Add Comment button click")
		# Вводим первый комментарий
		self.fillAttributes(commentInput='Test comment #1')
		# Нажимаем Сохранить
		self.clickByID('saveComment')
		printOk("Save button click")
		time.sleep(1)
		# Нажимаем Редактировать
		self.clickByID('moreActions')
		self.clickByXPATH(comment_action_button_xpath % 'Редактировать')
		printOk("Edit button click")
		time.sleep(1)
		# Очищаем инпут
		self.clearByID("commentInput")
		printOk("Clear Comment Input")
		time.sleep(1)
		# Вводим второй комментарий
		self.fillAttributes(commentInput='Test comment #2')
		time.sleep(1)
		# Нажимаем Сохранить
		self.clickByID('saveComment')
		printOk("Save button click")
		# Удаляем комментарий
		self.clickByID('moreActions')
		self.clickByXPATH(comment_action_button_xpath % 'Удалить')
		printOk("Delete button click")
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		time.sleep(2)

	# Добавляет файлы по шаблону в Файлах внутри документа
	def addTestTemplateInFiles(self, template_name):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Файлы
		self.clickTab('Файлы')
		printOk("Files button click")
		time.sleep(2)
		# Нажиаем Добавить
		self.clickByXPATH(add_file_button_xpath)
		printOk("Add button click")
		time.sleep(1)
		# Добавить Папку
		self.clickByXPATH(qxmenu_button_xpath % "По шаблону")
		printOk("Add template button click")
		time.sleep(1)
		# Click in popup menu
		self.clickByXPATH(qxmenu_button_xpath % template_name)
		printOk("Add template button click")
		time.sleep(10)
		# Нажимаем Ок
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(2)

	# Добавляет активность (маленькую) внутри документа
	def addActivity(self):
		# Нажимаем Добавить Автивность
		self.clickByID('addActivity')
		printOk("'Add activity' button click")
		time.sleep(3)
		# Находим поле Типа активности
		self.fillAttributes("//div[@id='Activity_objectID']", documentTypeID='Встреча')
		time.sleep(2)
		# Находим и нажимаем в списке нужный тип активности
		self.clickInPopupMenu('Встреча')
		printOk("Choose activity type")
		time.sleep(2)
		# Проставляем дату деактивации
		self.clickByID('_stripActivities', "//div[@id='deactivateDate']//input")
		printOk("Click deactivate date")
		time.sleep(1)
		self.fillAttributes("//div[@id='_stripActivities']", deactivateDate=TakeDate.tomorrow)
		printOk("Fill deactivate date")
		time.sleep(2)
		# Проставляем описание
		self.clickByID('_stripActivities', "//textarea[@id='subject']")
		printOk("Click subject")
		time.sleep(1)
		self.fillAttributes("//div[@id='_stripActivities']", subject=test_text)
		printOk("Fill subject")
		time.sleep(2)
		# Нажимаем кнопку Выбрать
		self.clickByID("responsibleID", "//div[@id='choose-button']")
		printOk("Choose button click")
		time.sleep(2)
		# Выбираем ответственного
		self.clickByXPATH("//div[@class='qx-window']//div[text()='Отдел продаж']")
		printOk("Choose responsible in table")
		time.sleep(1)
		# Нажимаем Выбрать
		self.clickByID('choose')
		printOk("Choose button click (In Table)")
		time.sleep(2)
		# Завершить
		self.clickByID('_processID_process_panel', "//div[text()='Завершить']")
		printOk("Finish button click")
		time.sleep(4)
		# Нажимаем Удалить активность
		self.clickByID('Activity_objectID', '//div[@id = "delete-button"]')
		printOk('Delete activity button click')
		time.sleep(3)
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk('OK button button click')
		time.sleep(1)

	# Добавляет счёт внутри документа с привязкой договора
	def addSimpleInvoiceWithContract(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Счета
		self.clickTab(name='Счета')
		printOk("Invoices button click")
		# Нажимаем Добавить
		self.clickByID('new')
		printOk("Add button click")
		time.sleep(3)
		# Находим поле Типа счёта и Вводим тип
		account_type_name_u = str(account_type_name)
		self.fillAttributes(planTypeID=account_type_name_u)
		# Находим и нажимаем в списке нужный тип счёта
		self.clickInPopupMenu(account_type_name_u)
		printOk("Choose document type")
		# Нажимаем на кнопку для выбора договора
		self.chooseReferenceInWindow('parentID', contracts_type_name)
		# Спим
		time.sleep(3)
		# Закрываем счёт
		self.clickByID('okb')
		printOk("Invoices close")
		# Спим
		time.sleep(3)

	# Добавляет счёт внутри документа без привязки договора
	def addSimpleInvoice(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Счета
		self.clickTab('Счета')
		printOk("Invoices button click")
		# Нажимаем Добавить
		self.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(3)
		# Закрываем счёт
		self.clickByID('okb')
		printOk("Invoices close")
		# Спим
		time.sleep(3)

	# Добавляет активность в документе
	def addSimpleActivity(self):
		# Нажимаем Активности
		self.clickTab('Активности')
		printOk("Activities button click")
		# Нажимаем Добавить
		self.clickByID('new')
		printOk("Add button click")
		# Спим
		time.sleep(5)
		# Вводим тип Активности
		self.fillAttributes(documentTypeID=activities_activity_type_name)
		time.sleep(3)
		# Выбираем тип Активности
		self.clickInPopupMenu(activities_activity_type_name)
		printOk("Choose activity type")
		time.sleep(5)
		# Нажимаем OK
		self.clickByID('okb')
		printOk("OK button click")
		time.sleep(2)

	# Добавляет заказ в документе
	def addSimpleOrder(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Заказы
		self.clickTab(name='Заказы')
		printOk("Orders button click")
		# Нажимаем Добавить
		self.clickByID('new')
		printOk("Add button click")
		time.sleep(3)
		# Проставляем дату документа
		self.clickByID('docDate')
		self.fillAttributes(docDate=TakeDate.today)
		# Спим
		time.sleep(5)
		# Закрываем заказ
		self.clickByID('okb')
		printOk("Close order")
		time.sleep(3)

	# Добавляет договор в документе
	def addSimpleContract(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		time.sleep(2)
		# Нажимаем Договоры
		self.clickTab(name='Договоры')
		printOk("Contracts button click")
		time.sleep(2)
		# Нажимаем Добавить
		self.clickByID('new')
		printOk("Add button click")
		time.sleep(5)
		# Находим поле Типа документа и Вводим тип
		self.fillAttributes(documentTypeID=contracts_type_name)
		time.sleep(2)
		# Находим и нажимаем в списке нужный тип документа
		self.clickInPopupMenu(contracts_type_name)
		printOk("Choose type")
		time.sleep(2)
		# Спим
		# Проставляем дату документа
		self.clickByID('docDate')
		time.sleep(1)
		self.fillAttributes(docDate=TakeDate.today)
		self.clickByID('processID.stateID')
		# Спим
		time.sleep(5)
		# Закрываем договор
		self.clickByID('okb')
		printOk("Close contract")
		time.sleep(3)

	# Добавляет тестовую папку в Файлах внутри документа
	def addTestFolderInFiles(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Файлы
		self.clickTab('Файлы')
		printOk("Files button click")
		time.sleep(2)
		# Нажиаем Добавить
		self.clickByXPATH(add_file_button_xpath)
		printOk("Add button click")
		time.sleep(1)
		# Добавить Папку
		self.clickByXPATH(add_folder_button_xpath)
		printOk("Add folder button click")
		# Спим
		time.sleep(2)
		# Стрингуем название
		folder_test_name_u = str(folder_test_name)
		# Вводим название Папки
		self.fillAttributes("//div[@class='qx-window']", name=folder_test_name_u)
		printOk("Enter folder name")
		# Спим
		time.sleep(2)
		# Нажимаем Ок
		self.clickByXPATH(ok_id_window_button_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(2)

	# Добавляет тег в документе
	def addTag(self, tag_name):
		# Добавляем тег
		self.clickByID('addTag')
		printOk("Add Tag button click")
		# Выбираем тег
		self.clickByXPATH(selected_tag_xpath % tag_name)
		self.clickByID('choose')
		printOk("Choose tag")
		# Закрываем окно с тегами
		self.clickByID('close')
		time.sleep(2)
		printOk("Close tag window")
		self.clickByID("delete-button", "", "//div[@class='qx-strip-dialog-container-tag']")
		printOk("Delete tag")

	# Добавляет участника и удаляет его
	def addMembersAndDelete(self, first_group_name='Инициатор', second_group_name='Исполнитель'):
		# Нажимаем Участники
		self.clickTab('Участники')
		printOk("Members button click")
		# Нажимаем Добавить
		self.clickByXPATH(add_button_xpath)
		printOk("Add button click")
		# Нажимаем Инициатор
		self.clickByXPATH(qx_menu_menu_select_xpath % first_group_name)
		# Нажимаем Должность
		self.clickByXPATH(qx_menu_menu_select_xpath % 'Сотрудник')
		printOk("Position button click")
		# Выбираем Генерального директора
		self.clickByXPATH(cell_in_table_xpath % 'Генеральный директор')
		self.clickByID('choose')
		printOk("Choose director")
		# Нажимаем закрыть окно
		self.clickByID('close')
		printOk("Close window")
		# Спим
		time.sleep(2)
		# Нажимаем Добавить
		self.clickByXPATH(add_button_xpath)
		printOk("Add button click")
		# Нажимаем Исполнитель
		self.clickByXPATH(qx_menu_menu_select_xpath % second_group_name)
		# Нажимаем Группа
		self.clickByXPATH(qx_menu_menu_select_xpath % 'Группа')
		printOk("Position button click")
		# Выбираем Логистика
		self.clickByXPATH(cell_in_table_xpath % 'Логистика')
		self.clickByID('choose')
		printOk("Choose logistic")
		# Нажимаем закрыть окно
		self.clickByID('close')
		printOk("Close window")
		# Спим
		time.sleep(2)
		# Выбираем Логистику
		self.clickByXPATH(cell_in_table_xpath % second_group_name)
		printOk("Choose logistic")
		# Нажимаем удалить
		self.clickByID('delete')
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(2)

	# Добавляет участника
	def addMember(self, name, first_group_name='Согласователь', second_group_name='Сотрудник'):
		# Нажимаем Участники
		self.clickTab('Участники')
		printOk("Members button click")
		# Нажимаем Добавить
		self.clickByXPATH(add_button_xpath)
		printOk("Add button click")
		# Нажимаем Инициатор
		self.clickByXPATH(qx_menu_menu_select_xpath % first_group_name)
		# Нажимаем Должность
		self.clickByXPATH(qx_menu_menu_select_xpath % second_group_name)
		printOk("Position button click")
		time.sleep(3)
		# Выбираем Генерального директора
		self.clickByXPATH(reference_xpath % name)
		self.clickByID('choose')
		printOk("Choose person")
		# Нажимаем закрыть окно
		self.clickByID('close')
		printOk("Close window")

	# Добавляет связь в документе
	def addLinkage(self, customer_group_name, customer_name):
		# Нажимаем +
		self.clickByID("linkageID_linkages", "//div[@id = 'linkageID_selectButton']")
		printOk("Add linkage button click")
		if type(customer_group_name) == str:
			# customer_group_name = customer_group_name.encode().decode('utf-8', 'ignore')
			customer_group_name = (customer_group_name,)
		for x in customer_group_name:
			# Нажимаем customer_group_name
			self.clickByXPATH(qxmenu_button_xpath % x)
			printOk("{} click".format(x))
			time.sleep(1)
		# Выбираем объект
		self.clickByID('filter', parent_xpath="//div[@class='qx-window']")
		printOk("Filter click")
		time.sleep(1)
		# Вводим контрагента
		self.sendKeysByXPATH("//div[@class='qx-popup']//input", customer_name)
		time.sleep(1)
		# Нажимаем на контрагента в таблице
		self.clickByXPATH(cell_in_table_xpath % customer_name)
		printOk("Customer name click")
		time.sleep(3)
		# Нажимаем Выбрать
		self.clickByID('choose')
		printOk("Choose button click")
		time.sleep(3)

	# Закрытие таблицы проиходит автоматом

	# Добавляем реквизиты банка в Юр.лицах
	def addBankAccount(self):
		self.createSimpleBankObject(
			bik='044525225',
			nameForeign='SBERBANK',
			inn='7707083893',
			kpp='773601001',
			accountNumber='30301810000006000001',
			personalAccount='30301810000006000002',
			comment='Test comment',
			deactivateDate=TakeDate.tomorrow
		)

	""""DELETE ELEMENT"""

	# Удаляет документ (внутри документа через кнопку)
	def delete_into_doc(self):
		# Удаить договор
		self.clickByID('deleteb')
		printOk("Delete document")
		time.sleep(3)
		# Нажимаем Enter
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("ENTER click")
		time.sleep(5)

	# Удаляет в таблице в объекте
	def delete_in_table(self):
		# Удаить договор
		self.clickByID('delete')
		printOk("Delete document")
		time.sleep(3)
		# Нажимаем Enter
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("ENTER click")
		time.sleep(5)

	# Удаляет участника
	def deleteMember(self, cell_name):
		# Нажимаем Участники
		self.clickTab('Участники')
		printOk("Members button click")
		# Выбираем ячейку с именем
		self.clickByXPATH(cell_in_table_xpath % cell_name)
		printOk("Choose logistic")
		# Нажимаем удалить
		self.clickByID('delete')
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(2)

	# Удаляет объект во вкладке. Передавать только название вкладки.
	def deleteObj(self, obj_name):
		time.sleep(2)
		# Переходим в раздел
		self.clickTab(obj_name)
		time.sleep(2)
		# Выбираем ссылку из списка
		self.clickByXPATH(select_row_in_table_xpath)
		time.sleep(2)
		# Нажимаем кнопку Удалить
		self.clickByID('delete')
		time.sleep(2)
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		# Спим
		time.sleep(4)

	""""CLICK"""

	# Клик стрелки вниз
	def click_arrow_down(self, value):
		i = value
		while i != 0:
			self.action.send_keys(Keys.ARROW_DOWN).perform()
			time.sleep(1)
			i -= 1
		time.sleep(1)

	# Клик по xpath
	def clickByXPATH(self, xpath):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)),
		                TextColors.FAIL + "Can't click element = " + TextColors.WARNING + xpath + TextColors.ENDC).click()
		time.sleep(1)

	# Клик по вкладке
	def clickTab(self, name):
		time.sleep(2)
		self.clickByXPATH(tab_xpath.format(name=name))

	# Клик по id элемента
	def clickByID(self, element_id, child_xpath='', parent_xpath=''):
		self.clickByXPATH(attribute_xpath.format(id=element_id, child=child_xpath, parent=parent_xpath))

	# Клик в окне по id элемента
	def clickInWindowByIDKey(self, element_id, child_xpath=''):
		self.clickByXPATH(window_attribute_xpath.format(id=element_id, child=child_xpath))

	# Клик по элементу в popup
	def clickInPopupMenu(self, text):
		time.sleep(3)
		self.clickByXPATH(popup_menu_select_xpath % text)
		time.sleep(1)

	# Клик в дереве
	def treeClick(self, tree_name):
		# Нажимаем рефлеш
		self.clickByID('tree-toolbar', "//div[@class='qx-button-common-border']")
		time.sleep(3)
		# Нажимаем на необходимый классификатор в дереве
		tree_name = str(tree_name)
		self.clickByID('tree-virtual', "//span[text()='%s']" % tree_name)
		time.sleep(2)
