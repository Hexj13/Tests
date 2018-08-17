# coding=utf-8
import datetime
import time
import re

from roots.content import *
from roots.xpath import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Colors for code highlighting in terminal
class TextColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


# Print and highlighting to log
def printInfo(text):
	try:
		print(TextColors.OKBLUE + str(text) + TextColors.ENDC, flush=True)
	except:
		pass


# Print and highlighting the headings in the log
def printTitle(text, color=TextColors.WARNING):
	try:
		print("", flush=True)
		print(color + str(text) + TextColors.ENDC, flush=True)
		print("", flush=True)
	except:
		pass


# Getting the date and formatting in DD.MM.YYYY
class TakeDate:
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today = today.strftime("%d.%m.%Y")
	tomorrow = tomorrow.strftime("%d.%m.%Y")


# The main class for the interface Flexbby
class UITestToolkit(object):
	def __init__(self):
		# Print start time
		printTitle("Test start at: " + time.ctime())
		# ---------Flags---------
		# chrome_options = Options()
		# chrome_options.add_argument("--start-maximized");
		# chrome_options.add_argument("--disable-infobars");
		# chrome_options.add_argument("--disable-extensions");
		# chrome_options.add_argument("--disable-gpu");
		# chrome_options.add_argument("--test-type");
		# chrome_options.add_argument("--no-startup-window");
		# chrome_options.add_argument("--headless");
		# print(TextColors.BOLD + "Start with flags = " + str(chrome_options._arguments)+ TextColors.ENDC)
		#
		# ---------For Linux start---------
		# chrome_options.binary_location = '/usr/bin/chromium-browser'
		#
		# ---------Choose browser---------
		self.driver = webdriver.Chrome()
		# self.driver = webdriver.Firefox()
		printInfo("Webdriver init")
		# Maximize browser window
		self.driver.maximize_window()
		printInfo("Maximize window")
		# Plug-in webdriver waiting
		self.wait = WebDriverWait(self.driver, 120)
		printInfo("WebDriverWait init")
		# Plug-in action chains
		self.action = action_chains.ActionChains(self.driver)
		printInfo("ActionChains init")

	"""BASIC"""

	# Enter text for the specified xpath. Checks the element for type: input or textarea. It also checks the div attachment for input or textarea. Then makes text input.
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

	# Passes the text / command (click, text) to the element by id (you can specify the parent and/or child's xpath)
	def fillAttributes(self, parent_xpath='', child_xpath='', **kwargs):
		for k, v in kwargs.items():
			self.sendKeysByXPATH(attribute_xpath.format(child=child_xpath, parent=parent_xpath, id=k), v)
			printInfo("Filled attribute with id = " + TextColors.UNDERLINE + str(k) + TextColors.ENDC)

	# Passes text / command (press, text) to the element by id (you can specify the xpath of the parent and/or child). Different from fillAttributes that uses a template textarea_xpath. This allows you to work around the qooxdoo problem with creating duplicate textarea.
	def fillTextarea(self, parent_xpath='', **kwargs):
		for k, v in kwargs.items():
			self.sendKeysByXPATH(textarea_xpath.format(parent=parent_xpath, id=k), v)
			printInfo("Filled textarea with id = " + TextColors.UNDERLINE + str(k) + TextColors.ENDC)

	# Select (click) a row in the table by text
	def selectRowInTable(self, contains_text=''):
		self.clickByXPATH(attribute_xpath.format(text=contains_text))

	# Clears the field and enters data. Takes the element ID and the text you enter.
	def inputByID(self, element_id, text):
		search_element = self.driver.find_element_by_id(element_id)
		printInfo("Find element by ID == " + str(element_id))
		search_element.clear()
		printInfo("Input cleared")
		search_element.send_keys(text)
		printInfo("The text entered")

	# Checks element visibility (by ID) on the stage.
	def visibilityOfAnyElem(self, docID):
		self.wait.until(EC.visibility_of_any_elements_located((By.ID, docID)))

	# Finds (focus) a cell in a table with text
	def findCellByText(self, text):
		self.driver.find_element_by_xpath(cell_in_table_xpath % text).location_once_scrolled_into_view()

	# Clears field by ID
	def clearByID(self, element_id, child_xpath='', parent_xpath=''):
		self.driver.find_element_by_xpath(
			attribute_xpath.format(parent=parent_xpath, child=child_xpath, id=element_id)).clear()
		printInfo("Input/textarea cleared")

	# Checks the visibility of the element. Used element_to_be_clickable to check not only the visibility but also the ability to click
	def checkVisibility(self, xpath):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

	# Parses a URL and returns the internal (!) documentID
	def takeDocID(self):
		url = self.driver.current_url
		hash_tag = url[url.find('#') + 1:]
		params = dict(x.split('=') for x in hash_tag.split('&'))
		obj_id = params['id']
		return obj_id

	# Closing the browser
	def quit(self):
		self.driver.quit()
		print(TextColors.BOLD + "Quit at: " + TextColors.ENDC + TextColors.OKBLUE + time.ctime() + TextColors.ENDC,
		      flush=True)
		print("Browser closed", flush=True)
		print("", flush=True)

	def urlify(self, s):
		# Remove all non-word characters (everything except numbers and letters)
		s = re.sub(r"[^\w\s]", '', s)
		# Replace all runs of whitespace with a single dash
		s = re.sub(r"\s+", '-', s)
		return s

	# Select "responsible" In the settings window. You must pass the id of the field where you want to put the responsible and his name.
	def chooseReferenceInWindow(self, reference_id, text):
		# Click on the button to select the contract
		self.clickByID(reference_id, "//div[@id = 'choose-button']")
		printInfo("'Select' button clicked")
		# Filter in the table
		self.filterInTable(text)
		time.sleep(1)
		# Choose responsible
		self.clickByXPATH(reference_obj_xpath.format(text=text), resetPointerEvents=True)
		self.clickByID('choose')
		printInfo("Contract selected")

	# Login to system. Takes a username and password
	def login(self, login, password):
		self.clickByID('login')
		printTitle("login START")
		self.clearByID('login')
		self.fillAttributes(login=login)
		self.fillAttributes(password=password)
		self.clickByID('enter')
		time.sleep(3.5)
		printTitle("login FINISH")

	# TODO: It is necessary to rework the process of setting parameters
	# Fills in the parameter fields in the document
	# def fillParameter(self, param_name, input_text):
	# # Find in the column with the names of the desired parameters and return it to the third parent
	# 	param_line = self.driver.find_element_by_xpath(
	# 		"//div[@id='DocumentParameterValue_objectID']//parent::div[@class='qx-table-row']//span[text()='%s']" % param_name
	# 	).find_element_by_xpath('../../..')
	# 	printOk("Find target row with name = " + TextColors.HEADER + param_name + TextColors.ENDC)
	# 	# Find the whole line
	# 	rows = param_line.find_elements_by_xpath('../*')
	# 	# Add one to the index. You will need to determine the appropriate line in front of the line with the name.
	# 	indexOfTarget = rows.index(param_line) + 1
	# 	printOk("Index of target = " + TextColors.HEADER + str(indexOfTarget) + TextColors.ENDC)
	# 	# Find the value cell
	# 	value_clm = "//div[@id='DocumentParameterValue_objectID']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[%s]/div[1]" % indexOfTarget  # <---- %s передавать indexOfTarget
	# 	# Clip on the cell to activate the interaction
	# 	self.driver.find_element_by_xpath(value_clm)
	# 	printOk("Find element")
	# 	self.action.click()
	# 	printOk("Click on 'Value' column")
	# 	# time.sleep(5)
	# 	# Inside the cell find the input and put down the value
	# 	# self.driver.find_element_by_xpath(
	# 	# 	"//div[@id='DocumentParameterValue_objectID']//div[@class='qx-table-scroller-focus-indicator']//input").send_keys(
	# 	# 	input_text)
	# 	self.sendKeysByXPATH(
	# 		"//div[@id='DocumentParameterValue_objectID']//div[@class='qx-table-scroller-focus-indicator']//input",
	# 		input_text)
	# 	printOk('Send keys')
	# 	time.sleep(1)
	# 	self.action.send_keys(Keys.ENTER)
	# 	printOk('Enter click')
	# 	# Click the Add comment button
	# 	self.clickByID('newCommentButton')
	# 	printOk("Add Comment button click")
	# 	# Enter the first comment
	# 	self.fillAttributes(commentInput='Параметр ' + param_name + ' был заполнен')
	# 	# Click Save
	# 	self.clickByID('saveComment')
	# 	printOk("Save button click")
	# 	time.sleep(1)

	# Creates a new requisite in accounts and fills in the fields through the dictionary. Use in addBankAccount
	def createSimpleBankObject(self, **kwargs):
		self.clickByID('BankAccount_objectID', '//div[@id="new"]')
		printInfo("'Add' button clicked")
		self.fillAttributes(bik=kwargs.pop('bik'))
		self.fillAttributes(**kwargs)
		self.clickByXPATH(okb_id_window_button_xpath)
		printInfo("'OK' button clicked")

	# Passes the link to the browser
	def setSite(self, url):
		self.driver.get(url)
		printInfo(
			"URL = " + TextColors.UNDERLINE + url + TextColors.ENDC)

	""""ADD ELEMENT"""

	# Adds a comment to the document
	def addComment(self):
		# Enter the first comment and save
		self.fillTextarea(commentTextInput='Test comment')
		self.clickByID('postComment')
		printInfo("Comment posted")
		# Click Edit
		self.clickByID('moreActions')
		self.clickByXPATH(comment_action_button_xpath % 'Редактировать')
		# Enter the second comment and save
		self.action.send_keys("#2")
		self.action.send_keys(Keys.ENTER)
		self.action.send_keys("Second line")
		self.action.perform()
		printInfo("Comment edited")
		self.clickByID(element_id='postComment', parent_xpath="//div[@id='visiblePart']")
		printInfo("Comment posted")
		# delete comment
		self.clickByID('moreActions')
		self.clickByXPATH(comment_action_button_xpath % 'Удалить')
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("Comment deleted")

	# Adds the file pattern in the File inside the document
	def addTestTemplateInFiles(self, template_name):
		self.clickTab('Файлы')
		printInfo("'Files' button clicked")
		time.sleep(2)
		self.clickByXPATH(add_file_button_xpath)
		printInfo("'Add' button clicked")
		self.clickByXPATH(qxmenu_button_xpath % "По шаблону")
		printInfo("'Add template' button clicked")
		self.clickByXPATH(qxmenu_button_xpath % template_name)
		printInfo("Template selected")
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'OK' button clicked")

	# Adds activity within the account
	def addActivity(self):
		# Click Add Activity
		self.clickByID('addActivity')
		printInfo("'Add activity' button clicked")
		# Find the activity Type field
		self.fillAttributes("//div[@id='Activity_objectID']", documentTypeID='Встреча')
		# Find and click in the list the desired type of activity
		self.clickInPopupMenu('Встреча')
		printInfo("Activity type selected")
		# Put down the date of deactivation
		self.clickByID('_stripActivities', child_xpath="//div[@id='deactivateDate']//input")
		printInfo("Deactivate date field clicked")
		self.fillAttributes("//div[@id='_stripActivities']", deactivateDate=TakeDate.tomorrow)
		printInfo("Deactivate date field filled")
		# Click "save" button, Choose
		self.clickByID("responsibleID", child_xpath="//div[@id='choose-button']")
		printInfo("'Choose' button clicked")
		time.sleep(2)
		# Choose a responsible
		self.clickByXPATH("//div[@class='qx-window']//div[text()='Отдел продаж']")
		printInfo("Responsible selected")
		time.sleep(1)
		# Click Select
		self.clickByID('choose')
		printInfo("'Choose' button clicked (In Table)")
		time.sleep(2)
		self.clickByID('_processID_process_panel', child_xpath="//div[text()='Завершить']")
		printInfo("'Finish' button clicked")
		# Click Delete activity
		self.clickByID('Activity_objectID', child_xpath='//div[@id = "delete-button"]')
		printInfo("'Delete activity' button clicked")
		# Click OK
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'OK' button button clicked")

	# Adds a Sale inside the document card
	def addSimpleOppotunity(self, type_name=sales_type_name):
		printTitle("OPPORTUNITIES START")
		type_name = str(type_name)
		self.clickTab(name='Продажи')
		printInfo("'Opportunities' button clicked")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(3)
		self.fillAttributes(documentTypeID=type_name)
		self.clickInPopupMenu(type_name)
		printInfo("Contract selected")
		time.sleep(1)
		self.clickByID('okb')
		printInfo("Opportunities card closed")
		printTitle("OPPORTUNITIES END")

	# Adds SimpleDocument inside the document card
	def addSimpleDocument(self, type_name=simple_document_name):
		printTitle("SIMPLEDOCUMENT START")
		type_name = str(type_name)
		self.clickTab(name='Документы')
		printInfo("'Documents' button clicked")
		self.clickByID('new')
		printInfo("'Add' button click")
		time.sleep(3)
		self.fillAttributes(documentTypeID=type_name)
		self.clickInPopupMenu(type_name)
		time.sleep(1)
		printInfo("Contract selected")
		self.clickByID('okb')
		printInfo("Document card closed")
		printTitle("SIMPLEDOCUMENT END")

	# Adds a specification to the object card
	def addSimpleSpetification(self, product_name):
		printTitle("SPECIFICATION PAGE START")
		self.clickTab('Спецификация')
		printInfo("'Specification' button clicked")
		self.clickByID('createSpecification')
		printInfo("'Add specification' button clicked")
		time.sleep(2)
		self.treeClick('Все')
		printInfo("'All' in tree clicked")
		time.sleep(1)
		self.clickByXPATH(product_name)
		printInfo("Product selected")
		self.clickByID('choose')
		printInfo("'Choose' button clicked")
		time.sleep(1)
		self.clickByID('close')
		printInfo("Specification card closed")
		printTitle("SPECIFICATION PAGE END")

	# Adds the invoice within the document with a binding contract
	def addSimpleInvoiceWithContract(self):
		printTitle("INVOICES START")
		self.clickTab(name='Счета')
		printInfo("'Invoices' button clicked")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(3)
		account_type_name_u = str(account_type_name)
		self.fillAttributes(planTypeID=account_type_name_u)
		self.clickInPopupMenu(account_type_name_u)
		printInfo("Document type selected")
		self.chooseReferenceInWindow('parentID', contracts_type_name)
		time.sleep(1)
		self.clickByID('okb')
		printInfo("Invoices card closed")
		printTitle("INVOICES END")

	# Adds the invoice within the document
	def addSimpleInvoice(self):
		printTitle("INVOICES START")
		self.clickTab('Счета')
		printInfo("'Invoices' button clicked")
		self.clickByID('new')
		printInfo("'Add' button click")
		time.sleep(3)
		self.clickByID('okb')
		printInfo("Invoices card closed")
		printTitle("INVOICES END")

	# Adds activity to the object card
	def addSimpleActivity(self):
		printTitle("ACTIVITY START")
		print("", flush=True)
		self.clickTab('Активности')
		printInfo("'Activities' button clicked")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(3)
		self.fillAttributes(documentTypeID=activity_type_name)
		self.clickInPopupMenu(activity_type_name)
		printInfo("Activity type selected")
		time.sleep(2)
		self.clickByID('okb')
		printInfo("Activity card closed")
		printTitle("ACTIVITY END")

	def addApproval(self):
		printTitle('APPROVALS START')
		self.clickTab(name='Согласование')
		self.clickByID('new')
		printInfo("Add button clicked")
		time.sleep(4)
		self.clickByID('okb')
		printInfo("Approval card closed")
		printTitle('APPROVALS END')

	# Adds a procurement to the object card
	def addSimpleProcurement(self):
		printTitle("PROCUREMENT START")
		self.clickTab(name='Закупки')
		printInfo("'Procurement' button click")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(3)
		self.clickByID('docDate')
		self.fillAttributes(docDate=TakeDate.today)
		self.fillTextarea(subject=test_text)
		printInfo("Fields 'docDate' and 'subject' were filled")
		time.sleep(2)
		self.clickByID('okb')
		printInfo("Procurement card closed")
		printTitle("PROCUREMENT END")

	# Adds a contract to the object card
	def addSimpleContract(self):
		printTitle("CONTRACTS START")
		self.clickTab(name='Договоры')
		printInfo("'Contracts' button clicked")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(3)
		self.fillAttributes(documentTypeID=str(contracts_type_name))
		self.clickInPopupMenu(str(contracts_type_name))
		printInfo("Type selected")
		self.clickByID('docDate')
		self.fillAttributes(docDate=TakeDate.today)
		self.clickByID('activateDate')
		time.sleep(2)
		self.clickByID('okb')
		printInfo("Contract card closed")
		printTitle("CONTRACTS END")

	# Adds a test folder in Files inside the document card
	def addTestFolderInFiles(self):
		printTitle("FILES PAGE START")
		self.clickTab('Файлы')
		self.clickByXPATH(file_dir_button)  # choose view
		self.clickByID('addFileButton')
		printInfo("'Add' button clicked")
		self.clickByXPATH(add_folder_button_xpath)
		printInfo("'Add folder' button clicked")
		self.clickByXPATH(add_new_folder_button_xpath)
		printInfo("'Add new folder' button clicked")
		self.fillAttributes("//div[@class='qx-window']", name=folder_test_name)
		printInfo("Folder name filled")
		self.clickByXPATH(okb_id_window_button_xpath)
		printInfo("'OK' button clicked")
		printTitle("FILES PAGE END")

	# Adds a tag to the object card
	def addTag(self, tag_name):
		self.clickByID('addTag')
		printInfo("'Add Tag' button clicked")
		self.clickByXPATH(selected_tag_xpath % tag_name, resetPointerEvents=True)
		self.clickByID('choose')
		printInfo("Tag selected")
		self.clickByID('close')
		printInfo("Tag window closed")
		self.clickByID("delete-button", "", "//div[@class='qx-strip-dialog-container-tag']", resetPointerEvents=False)
		printInfo("Tag deleted")

	# Adds and removes a member and group
	def addMembersAndDelete(self, first_group_name='Инициатор', second_group_name='Исполнитель'):
		printTitle("MEMBERS PAGE START")
		# Add a document participant
		self.addMember(name='Прокофьев Андрей Викторович', first_group_name=first_group_name,
		               second_group_name='Сотрудник')
		time.sleep(2)
		# then add the group to the participants
		self.clickByXPATH(add_button_xpath)
		printInfo("'Add' button clicked")
		self.clickByXPATH(qx_menu_menu_select_xpath % second_group_name)
		self.clickByXPATH(qx_menu_menu_select_xpath % 'Группа')
		printInfo("'Position' button clicked")
		self.clickByXPATH(cell_in_table_xpath % 'Логистика')
		self.clickByID('choose')
		printInfo("'Logistic' selected")
		self.clickByID('close')
		printInfo("Window closed")
		time.sleep(2)
		self.clickByXPATH(cell_in_table_xpath % second_group_name, resetPointerEvents=True)
		self.clickByID('delete')
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'OK' button click")
		time.sleep(2)
		printTitle("MEMBERS PAGE END")

	# Adds a member
	def addMember(self, name, first_group_name='Согласователь', second_group_name='Сотрудник'):
		printTitle("MEMBERS PAGE START")
		self.clickTab('Участники')
		printInfo("'Members' button clicked")
		self.clickByXPATH(add_button_xpath)
		printInfo("'Add' button clicked")
		self.clickByXPATH(qx_menu_menu_select_xpath % first_group_name)
		self.clickByXPATH(qx_menu_menu_select_xpath % second_group_name)
		printInfo("'Position' button clicked")
		time.sleep(1)
		self.filterInTable(name)
		self.clickByXPATH(reference_xpath % name, resetPointerEvents=True)
		self.clickByID('choose')
		printInfo("Person selected")
		self.clickByID('close')
		printInfo("Window closed")
		printTitle("MEMBERS PAGE END")

	# Adds a supplement to the object card
	def addSupplement(self):
		printTitle("SUPPLEMENT START")
		self.clickTab('Доп. соглашения')
		printInfo("'Supplement' button clicked")
		self.clickByID('new')
		printInfo("'Add' button clicked")
		time.sleep(2)
		self.fillAttributes(docDate=TakeDate.tomorrow)
		self.fillAttributes(deactivateDate=TakeDate.tomorrow)
		self.clickByID('docDate')
		printInfo("Fields 'docDate' and 'deactivateDate' were filled")
		time.sleep(1)
		self.clickByID('okb')
		printInfo("'OK' button clicked")
		printTitle("SUPPLEMENT END")

	# Adds a supplement to the object card
	# Closing the table is automatic
	def addLinkage(self, customer_group_name, customer_name):
		# Press +
		self.clickByID("linkageID_linkages", "//div[@id = 'linkageID_selectButton']", resetPointerEvents=False)
		printInfo("'Add linkage' button clicked")
		if type(customer_group_name) == str:
			# customer_group_name = customer_group_name.encode().decode('utf-8', 'ignore')
			customer_group_name = (customer_group_name,)
		for x in customer_group_name:
			self.clickByXPATH(qxmenu_button_xpath % x, resetPointerEvents=True)
			printInfo("{} click".format(x))
			time.sleep(1)
		self.filterInTable(customer_name)
		self.clickByXPATH(cell_in_table_xpath % customer_name, resetPointerEvents=True)
		printInfo("Customer name clicked")
		time.sleep(1)
		self.clickByID('choose')
		printInfo("'Choose' button clicked")
		time.sleep(1)

	# Filter in table
	def filterInTable(self, name):
		self.clickByID('filter', parent_xpath="//div[@class='qx-window']")
		printInfo("'Filter' button clicked")
		time.sleep(1)
		self.sendKeysByXPATH("//div[@class='qx-popup']//input", name)
		time.sleep(1)
		self.action.send_keys(Keys.ENTER)

	# Add Bank details to the accounts
	def addBankAccount(self):
		printTitle("BANK REQUISITES START")
		self.createSimpleBankObject(
			bik='044525225',
			nameForeign='SBERBANK',
			inn='7707083893',
			kpp='773601001',
			accountNumber='30301810000006000001',
			personalAccount='30301810000006000002',
			deactivateDate=TakeDate.tomorrow
		)
		printTitle("BANK REQUISITES END")

	""""DELETE ELEMENT"""

	# Deletes the document (inside the document via the button)
	def delete_into_doc(self):
		self.clickByID('deleteb')
		printInfo("Delete button clicked")
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'OK' clicked")
		time.sleep(2)

	# Delete inside table (in object)
	def delete_in_table(self):
		self.clickByID('delete')
		printInfo("'Delete' button clicked")
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'ОК' clicked")
		time.sleep(2)

	# Removes a member
	def deleteMember(self, cell_name):
		printTitle("MEMBERS PAGE START")
		self.clickTab('Участники')
		printInfo("'Members' button click")
		self.clickByXPATH(cell_in_table_xpath % cell_name)
		printInfo("Cell in table selected")
		self.clickByID('delete')
		printInfo("'Delete' button clicked")
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo("'OK' button clicked")
		printTitle("MEMBERS PAGE END")

	# Deletes the object in the tab. Pass only the name of the tab.
	def deleteObj(self, obj_name):
		self.clickTab(obj_name)
		self.clickByXPATH(select_row_in_table_xpath, resetPointerEvents=True)
		self.clickByID('delete')
		time.sleep(0.5)
		self.clickByXPATH(ok_close_window_button_xpath)
		printInfo(str(obj_name) + " " + "deleted")

	""""CLICK"""

	# Click the down arrow
	def click_arrow_down(self, value):
		i = value
		while i != 0:
			self.action.send_keys(Keys.ARROW_DOWN).perform()
			time.sleep(1)
			i -= 1
		time.sleep(1)

	# Xpath click
	def clickByXPATH(self, xpath, resetPointerEvents=False):
		time.sleep(0.5)
		# Highlight an item before clicking
		# Find the element
		element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
		if resetPointerEvents:
			self.driver.execute_script("""
				var element = arguments[0];
				for(var i = 0; i < 3; ++i) {
					element.style.pointerEvents = 'auto';
					element = element.parentNode;
				}
			""", element)
		# Keeping the old style
		color = self.driver.execute_script("arguments[0].style.backgroundColor", element)
		# Write on red in color style
		self.driver.execute_script("arguments[0].style.backgroundColor = '#FF4747'", element)
		time.sleep(0.2)
		# Returning the old style
		self.driver.execute_script("arguments[0].style.backgroundColor = arguments[1]", element, color)
		try:
			element.click()
			time.sleep(0.5)
		except Exception:
			# Click through ActionChains
			try:
				element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
				#
				# ---------------------JS script click---------------------
				# self.driver.execute_script("""
				# 	var triggerMouseEvent = function(node, eventType) {
				# 	    var clickEvent = document.createEvent ('MouseEvents');
				# 	    clickEvent.initEvent (eventType, true, true);
				# 	    clickEvent.pointerId = 1;
				# 	    clickEvent.isPrimary = true;
				# 	    clickEvent.getPointerType = function() { return 'touch'; };
				# 	    node.dispatchEvent (clickEvent);
				# 	}
				#     triggerMouseEvent(arguments[0], "mousedown");
				#     triggerMouseEvent(arguments[0], "mouseup");
				# """, element)
				#

				self.action.move_to_element(element)
				self.action.click()
				self.action.perform()
			except:
				print(TextColors.FAIL + "Can't click on element = " + TextColors.WARNING + xpath + TextColors.ENDC)

				def datetime_now(prefix):
					symbols = str(datetime.datetime.now())
					return prefix + "-" + "".join(symbols)

				screen_name = self.urlify(datetime_now('screen')) + '.png'  # Forming a name for a screenshot
				self.driver.save_screenshot(
					'C:/Users/Operator/Desktop/DFCRM/tests/other/screenshots/%s' % screen_name)
				print(TextColors.FAIL + "Screenshot saved" + TextColors.ENDC)
				quit()

	# Click on tab
	def clickTab(self, name):
		time.sleep(0.5)
		self.clickByXPATH(tab_xpath.format(name=name))
		printInfo("Click on " + str(name) + " tab")
		time.sleep(0.5)

	def clickByID(self, element_id, child_xpath='', parent_xpath='', resetPointerEvents=False):
		self.clickByXPATH(attribute_xpath.format(id=element_id, child=child_xpath, parent=parent_xpath),
		                  resetPointerEvents=resetPointerEvents)

	def clickInWindowByIDKey(self, element_id, child_xpath=''):
		self.clickByXPATH(window_attribute_xpath.format(id=element_id, child=child_xpath))

	def clickInPopupMenu(self, text):
		self.clickByXPATH(popup_menu_select_xpath % text, resetPointerEvents=True)
		time.sleep(1)

	def treeClick(self, tree_name):
		self.clickByID('tree-toolbar', child_xpath="//div[@class='qx-circle']", resetPointerEvents=True)
		tree_name = str(tree_name)
		self.clickByID('tree-virtual', child_xpath="//span[text()='%s']" % tree_name, resetPointerEvents=True)
		time.sleep(1)
