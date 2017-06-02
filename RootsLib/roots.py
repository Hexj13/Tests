# coding=utf-8
import datetime
import time
import os

from RootsLib.content import *
from RootsLib.xpath import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class UITestToolkit(object):
	def inputByID(self, element_id, text):
		search_element = self.driver.find_element_by_id(element_id)
		printOk("Find element by ID == '" + TextColors.BOLD + element_id + TextColors.ENDC + "'")
		search_element.clear()
		printOk("Clear")
		search_element.send_keys(text)
		printOk("Enter text == '" + TextColors.BOLD + text + TextColors.ENDC + "'")

	def visibilityOfAnyElem(self, docID):
		self.wait.until(EC.visibility_of_any_elements_located((By.ID, docID)))

	# TODO : Добавить в документацию
	def click_arrow_down(self, value):
		i = value
		while i != 0:
			self.action.send_keys(Keys.ARROW_DOWN).perform()
			time.sleep(SleepSeconds.ONE)
			i -= 1
		time.sleep(SleepSeconds.ONE)

	# TODO: Добавить в документацию
	def findElement(self, text):
		self.driver.find_element_by_xpath(cell_in_table_xpath % text).location_once_scrolled_into_view()

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

	def fillAttributes(self, parent_xpath='', child_xpath='', **kwargs):
		for k, v in kwargs.items():
			self.sendKeysByXPATH(attribute_xpath.format(child=child_xpath, parent=parent_xpath, id=k), v)
			printOk("Enter " + k)

	def selectRowInTable(self, contains_text=''):
		self.clickByXPATH(attribute_xpath.format(text=contains_text))

	def clickByXPATH(self, xpath):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)),
		                TextColors.FAIL + "Can't click element = " + TextColors.WARNING + xpath + TextColors.ENDC).click()
		time.sleep(SleepSeconds.ONE)

	def clickTab(self, name):
		time.sleep(SleepSeconds.TWO)
		self.clickByXPATH(tab_xpath.format(name=name))

	def clickByID(self, element_id, child_xpath='', parent_xpath=''):
		self.clickByXPATH(attribute_xpath.format(id=element_id, child=child_xpath, parent=parent_xpath))

	def clickInWindowByIDKey(self, element_id, child_xpath=''):
		self.clickByXPATH(window_attribute_xpath.format(id=element_id, child=child_xpath))

	def clickInPopupMenu(self, text):
		time.sleep(SleepSeconds.THREE)
		self.clickByXPATH(popup_menu_select_xpath % text)
		time.sleep(SleepSeconds.ONE)

	def clearByID(self, element_id, child_xpath='', parent_xpath=''):
		self.driver.find_element_by_xpath(
			attribute_xpath.format(parent=parent_xpath, child=child_xpath, id=element_id)).clear()

	def waitNoShadow(self):
		self.wait.until(EC.invisibility_of_element_located((By.ID, 'shadow')))
		time.sleep(SleepSeconds.TWO)

	def checkVisibility(self, xpath):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

	def takeDocID(self):
		url = self.driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		obj_id = params['id']
		return obj_id

	def quit(self):
		self.driver.quit()

	def delete_into_doc(self):
		# Удаить договор
		self.clickByID('deleteb')
		printOk("Delete document")
		time.sleep(SleepSeconds.THREE)
		# Нажимаем Enter
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("ENTER click")
		time.sleep(SleepSeconds.FIVE)

	def delete_in_table(self):
		# Удаить договор
		self.clickByID('delete')
		printOk("Delete document")
		time.sleep(SleepSeconds.THREE)
		# Нажимаем Enter
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("ENTER click")
		time.sleep(SleepSeconds.FIVE)

	def chooseReferenceInWindow(self, reference_id, text):
		# Нажимаем на кнопку для выбора договора
		self.clickByID(reference_id, "//div[@id = 'choose-button']")
		printOk("Select button click")
		time.sleep(SleepSeconds.FOUR)
		# Выбираем договор
		self.clickByXPATH(reference_obj_xpath.format(text=text))
		time.sleep(SleepSeconds.ONE)
		self.clickByID('choose')
		printOk("Choose contract")

	def login(self, login, password):
		print(TextColors.WARNING + "login START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		time.sleep(SleepSeconds.ONE)
		self.clearByID('login')
		self.fillAttributes(login=login)
		self.fillAttributes(password=password)
		self.clickByID('enter')
		printOk("Submit button click")
		time.sleep(SleepSeconds.EIGHT)
		print("", flush=True)
		print(TextColors.WARNING + "login FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def addLinkage(self, customer_group_name, customer_name):
		# Нажимаем +
		self.clickByID("linkageID_linkages", "//div[@id = 'linkageID_selectButton']")
		printOk("Add linkage buton click")
		if type(customer_group_name) == str:
			# customer_group_name = customer_group_name.encode().decode('utf-8', 'ignore')
			customer_group_name = (customer_group_name,)
		for x in customer_group_name:
			# Нажимаем customer_group_name
			self.clickByXPATH(qxmenu_button_xpath % x)
			printOk("{} click".format(x))
			time.sleep(SleepSeconds.ONE)
		# Нажимаем на контрагента в таблице
		self.clickByXPATH(cell_in_table_xpath % customer_name)
		printOk("Customer name click")
		# Нажимаем Выбрать
		self.clickByID('choose')
		printOk("Choose button click")
		time.sleep(SleepSeconds.FOUR)
		"""Закрытие таблицы проиходит автоматом"""

	def fillParameter(self, param_name, input_text):
		param_line = self.driver.find_element_by_xpath(
			"//div[@id='DocumentParameterValue_objectID']//parent::div[@class='qx-table-row']//span[text()='%s']" % param_name
		).find_element_by_xpath('../../..')
		printOk("Find target row with name = " + TextColors.HEADER + param_name + TextColors.ENDC)
		rows = param_line.find_elements_by_xpath('../*')
		indexOfTarget = rows.index(param_line) + 1
		printOk("Index of target = " + TextColors.HEADER + str(indexOfTarget) + TextColors.ENDC)
		time.sleep(SleepSeconds.ONE)
		value_clm = "//div[@id='DocumentParameterValue_objectID']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[%s]/div[1]" % indexOfTarget  # <---- %s передавать indexOfTarget
		time.sleep(SleepSeconds.ONE)
		self.clickByXPATH(value_clm)
		printOk("Click on 'Value' column")
		time.sleep(SleepSeconds.ONE)
		self.driver.find_element_by_xpath(
			"//div[@id='DocumentParameterValue_objectID']//div[@class='qx-table-scroller-focus-indicator']//input").send_keys(
			input_text)
		printOk('Send keys')
		time.sleep(SleepSeconds.TWO)
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
		time.sleep(SleepSeconds.ONE)

	def addBankAccount(self):
		self.createSimpleObject(
			bik='044525225',
			nameForeign='SBERBANK',
			inn='7707083893',
			kpp='773601001',
			accountNumber='30301810000006000001',
			personalAccount='30301810000006000002',
			comment='Test comment',
			deactivateDate=TakeDate.tomorrow
		)

	def addMembers(self, first_group_name='Инициатор', second_group_name='Исполнитель'):
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
		time.sleep(SleepSeconds.TWO)
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
		time.sleep(SleepSeconds.TWO)
		# Выбираем Логистику
		self.clickByXPATH(cell_in_table_xpath % second_group_name)
		printOk("Choose logistic")
		# Нажимаем удалить
		self.clickByID('delete')
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(SleepSeconds.TWO)

	def createSimpleObject(self, **kwargs):
		# Нажимаем Добавить
		self.clickByID('BankAccount_objectID', '//div[@id="new"]')
		printOk("Add button click")
		self.fillAttributes(bik=kwargs.pop('bik'))
		self.fillAttributes(**kwargs)
		# Нажимаем ОК
		time.sleep(SleepSeconds.ONE)
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")

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
		time.sleep(SleepSeconds.TWO)
		printOk("Close tag window")
		self.clickByID("delete-button", "", "//div[@class='qx-strip-dialog-container-tag']")
		printOk("Delete tag")

	def addTestFolderInFiles(self):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Файлы
		self.clickTab('Файлы')
		printOk("Files button click")
		time.sleep(SleepSeconds.TWO)
		# Нажиаем Добавить
		self.clickByXPATH(add_file_button_xpath)
		printOk("Add button click")
		time.sleep(SleepSeconds.ONE)
		# Добавить Папку
		self.clickByXPATH(add_folder_button_xpath)
		printOk("Add folder button click")
		# Спим
		time.sleep(SleepSeconds.TWO)
		# Стрингуем название
		folder_test_name_u = str(folder_test_name)
		# Вводим название Папки
		self.fillAttributes("//div[@class='qx-window']", name=folder_test_name_u)
		printOk("Enter folder name")
		# Спим
		time.sleep(SleepSeconds.ONE)
		# Нажимаем Ок
		self.clickByXPATH(ok_id_window_button_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(SleepSeconds.TWO)

	def treeClick(self, tree_name):
		# Нажимаем рефлеш
		self.clickByID('tree-toolbar', "//div[@class='qx-button-common-border']")
		time.sleep(SleepSeconds.THREE)
		# Нажимаем на необходимый классификатор в дереве
		tree_name = str(tree_name)
		self.clickByID('tree-virtual', "//span[text()='%s']" % tree_name)
		time.sleep(SleepSeconds.TWO)

	def addActivity(self):
		# Нажимаем Добавить Автивность
		self.clickByID('addActivity')
		printOk("'Add activity' button click")
		time.sleep(SleepSeconds.THREE)
		# Находим поле Типа активности
		self.fillAttributes("//div[@id='Activity_objectID']", documentTypeID='Встреча')
		time.sleep(SleepSeconds.TWO)
		# Находим и нажимаем в списке нужный тип активности
		self.clickInPopupMenu('Встреча')
		printOk("Choose activity type")
		time.sleep(SleepSeconds.TWO)
		# Проставляем дату деактивации
		self.clickByID('_stripActivities', "//div[@id='deactivateDate']//input")
		printOk("Click deactivate date")
		time.sleep(SleepSeconds.ONE)
		self.fillAttributes("//div[@id='_stripActivities']", deactivateDate=TakeDate.tomorrow)
		printOk("Fill deactivate date")
		time.sleep(SleepSeconds.TWO)
		# Проставляем описание
		self.clickByID('_stripActivities', "//textarea[@id='subject']")
		printOk("Click subject")
		time.sleep(SleepSeconds.ONE)
		self.fillAttributes("//div[@id='_stripActivities']", subject=test_text)
		printOk("Fill subject")
		time.sleep(SleepSeconds.TWO)
		# Нажимаем кнопку Выбрать
		self.clickByID("responsibleID", "//div[@id='choose-button']")
		printOk("Choose button click")
		time.sleep(SleepSeconds.TWO)
		# Выбираем ответственного
		self.clickByXPATH("//div[@class='qx-window']//div[text()='Отдел продаж']")
		printOk("Choose responsible in table")
		time.sleep(SleepSeconds.ONE)
		# Нажимаем Выбрать
		self.clickByID('choose')
		printOk("Choose button click (In Table)")
		time.sleep(SleepSeconds.TWO)
		# Завершить
		self.clickByID('_processID_process_panel', "//div[text()='Завершить']")
		printOk("Finish button click")
		time.sleep(SleepSeconds.FOUR)
		# Нажимаем Удалить активность
		self.clickByID('Activity_objectID', '//div[@id = "delete-button"]')
		printOk('Delete activity button click')
		time.sleep(SleepSeconds.THREE)
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk('OK button button click')
		time.sleep(SleepSeconds.ONE)

	def addComment(self):
		# Нажимаем кнопку Добавить Комментарий
		self.clickByID('newCommentButton')
		printOk("Add Comment button click")
		# Вводим первый комментарий
		self.fillAttributes(commentInput='Test comment #1')
		# Нажимаем Сохранить
		self.clickByID('saveComment')
		printOk("Save button click")
		time.sleep(SleepSeconds.ONE)
		# Нажимаем Редактировать
		self.clickByXPATH(comment_button_xpath % 'Редактировать')
		printOk("Edit button click")
		time.sleep(SleepSeconds.ONE)
		# Очищаем инпут
		self.clearByID("commentInput")
		printOk("Clear Comment Input")
		time.sleep(SleepSeconds.ONE)
		# Вводим второй комментарий
		self.fillAttributes(commentInput='Test comment #2')
		time.sleep(SleepSeconds.ONE)
		# Нажимаем Сохранить
		self.clickByID('saveComment')
		printOk("Save button click")
		# Удаляем комментарий
		self.clickByXPATH(comment_button_xpath % 'Удалить')
		printOk("Delete button click")
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		time.sleep(SleepSeconds.TWO)

	def addTestTemplateInFiles(self, template_name):
		# Проверяем на отсутвие shadow
		self.waitNoShadow()
		printOk("NO shadow")
		# Нажимаем Файлы
		self.clickTab('Файлы')
		printOk("Files button click")
		time.sleep(SleepSeconds.TWO)
		# Нажиаем Добавить
		self.clickByXPATH(add_file_button_xpath)
		printOk("Add button click")
		time.sleep(SleepSeconds.ONE)
		# Добавить Папку
		self.clickByXPATH(qxmenu_button_xpath % "По шаблону")
		printOk("Add template button click")
		time.sleep(SleepSeconds.ONE)
		# Click in popup menu
		self.clickByXPATH(qxmenu_button_xpath % template_name)
		printOk("Add template button click")
		time.sleep(SleepSeconds.TEN)
		# Нажимаем Ок
		self.clickByXPATH(ok_delete_button_window_xpath)
		printOk("OK button click")
		# Спим
		time.sleep(SleepSeconds.TWO)

	def deleteObj(self, obj_name):
		time.sleep(SleepSeconds.TWO)
		# Переходим в раздел
		self.clickTab(obj_name)
		time.sleep(SleepSeconds.TWO)
		# Выбираем ссылку из списка
		self.clickByXPATH(select_row_in_table_xpath)
		time.sleep(SleepSeconds.TWO)
		# Нажимаем кнопку Удалить
		self.clickByID('delete')
		time.sleep(SleepSeconds.TWO)
		# Нажимаем ОК
		self.clickByXPATH(ok_delete_button_window_xpath)
		# Спим
		time.sleep(SleepSeconds.TWO)

	def __init__(self):
		print("----------------------------------------", flush=True)
		print(TextColors.WARNING + "UITestToolkit init START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		chrome_options = Options()
		chrome_options.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		printOk("Webdriver init")
		self.driver.maximize_window()
		printOk("Maximaze window")
		self.wait = WebDriverWait(self.driver, 120)
		printOk("WebDriverWait init")
		self.action = action_chains.ActionChains(self.driver)
		printOk("ActionChains init")
		print("", flush=True)
		print(TextColors.WARNING + "UITestToolkit init FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def setSite(self, url):
		self.driver.get(url)
		print(
			"Get URL = " + TextColors.UNDERLINE + url + TextColors.ENDC + " ----> " + TextColors.OKGREEN + "OK" + TextColors.ENDC,
			flush=True)
		print("----------------------------------------", flush=True)


def printOk(text):
	try:
		print(str(text) + " " + "---->" + " " + TextColors.OKGREEN + "OK" + TextColors.ENDC, flush=True)
	except:
		pass


class TakeDate:
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today = today.strftime("%d.%m.%Y")
	tomorrow = tomorrow.strftime("%d.%m.%Y")


class SleepSeconds:
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	TWENTY = 20


class TextColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
