# coding=utf-8
import unittest

from rootsLib.roots import *


# noinspection PyUnusedLocal
class RelationsTesting(unittest.TestCase):
	print("----------------------------------------", flush=True)
	print(TextColors.HEADER + "Test 'RelationsTesting' START" + TextColors.ENDC, flush=True)
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

	def test_relations(self):
		self.toolkit.login(login_text, password_text)
		print(TextColors.WARNING + "test_relations START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Настройки
		self.toolkit.clickByXPATH(menu_button_xpath % 'Настройки')
		printOk("Settings button click")

		""""ROLES"""
		print("", flush=True)
		print(TextColors.WARNING + "ROLE ADDING START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Связи
		self.toolkit.clickByXPATH(menu_button_xpath % 'Связи')
		printOk("Relations button click")
		# Переходим в Роли объектов
		self.toolkit.clickByXPATH(menu_button_xpath % 'Роли объектов')
		printOk("Roles button click")
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("ADD button click")
		#
		test_role_text = 'Тестовая роль'
		# Вводим текст
		self.toolkit.fillAttributes(name=test_role_text)
		# Вводим текст
		self.toolkit.fillAttributes(tag='Test')
		# Вводим текст
		self.toolkit.fillAttributes(comment='Test comment')
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Click button ADD")
		# Выбираем ячейку в таблице
		self.toolkit.chooseReferenceInWindow('tableID', 'Company')
		printOk("Add company from table")
		time.sleep(2)
		# Выбираем ячейку в таблице
		self.toolkit.chooseReferenceInWindow('baseTableID', 'CompanyTree')
		printOk("Add CompanyTree from table")
		time.sleep(2)
		#
		self.toolkit.clickByID('nameForeignID')
		printOk("Click on input")
		#
		self.toolkit.action.send_keys('id').perform()
		printOk("Send keys in input")
		time.sleep(2)
		#
		self.toolkit.clickInPopupMenu('id')
		printOk("Choose in popup menu")
		time.sleep(2)
		#
		self.toolkit.clickInWindowByIDKey('okb')
		printOk("Click OK button")
		time.sleep(5)
		print("", flush=True)
		print(TextColors.WARNING + "ROLE ADDING END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

		"""GROUPS"""
		print(TextColors.WARNING + "GROUPS ADDING START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		# Переходим в Роли объектов
		self.toolkit.clickByXPATH(menu_button_xpath % 'Группы')
		printOk("Go to 'groups' in side-menu")
		time.sleep(2)
		# Нажимаем "Добавить"
		self.toolkit.clickByID('new')
		printOk("Click ADD button")
		time.sleep(2)
		#
		test_group_text = 'Тестовая группа'
		#
		self.toolkit.fillAttributes(name=test_group_text)
		time.sleep(2)
		#
		self.toolkit.clickByXPATH('//div[@id="rolesInGroup"]//div[text()="Добавить"]')
		time.sleep(2)
		#
		self.toolkit.clickByXPATH(
			"//div[@class='qx-window'and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')])]//div[@class='qooxdoo-table-cell' and (text()='%s')]" % test_role_text)
		time.sleep(2)
		#
		self.toolkit.clickByID('choose')
		#
		self.toolkit.action.send_keys(Keys.ESCAPE).perform()
		time.sleep(2)
		#
		self.toolkit.clickByID('okb')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "GROUPS ADDING END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)

		"""УДАЛЕНИЕ ССЫЛОК"""
		print(TextColors.WARNING + "DELETE OBJ START" + TextColors.ENDC, flush=True)
		print("", flush=True)
		#
		self.toolkit.clickByXPATH(
			"//div[@class='qooxdoo-table-cell' and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')]) and (text()='%s')]" % test_group_text, resetPointerEvents=True)
		#
		self.toolkit.clickByID('delete')
		#
		self.toolkit.clickByID('ok-button')
		# Переходим в Связи
		self.toolkit.clickByXPATH(menu_button_xpath % 'Роли объектов')
		printOk("Relations button click")
		#
		self.toolkit.clickByXPATH(
			"//div[@class='qooxdoo-table-cell' and not(ancestor::div[contains(@style,'display:none')])and not(" \
			"ancestor::div[contains(@style,'display: none')]) and (text()='%s')]" % test_role_text, resetPointerEvents=True)
		#
		self.toolkit.clickByID('delete')
		#
		self.toolkit.clickByID('ok-button')
		time.sleep(2)
		print("", flush=True)
		print(TextColors.WARNING + "DELETE OBJ END" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.OKGREEN + "Testing" + " " + TextColors.BOLD + "SUCCESS" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)

	def tearDown(self):
		self.toolkit.quit()
		print("Browser closed", flush=True)
		print("----------------------------------------", flush=True)
		print(TextColors.HEADER + "Test 'RelationsTesting' FINISH" + TextColors.ENDC, flush=True)
		print("----------------------------------------", flush=True)
		print("", flush=True)


if __name__ == '__main__':
	unittest.main()
