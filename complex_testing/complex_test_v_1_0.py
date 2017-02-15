# coding=utf-8
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from complex_elements_config import *
from complex_content_config import *

# Откроем Хром
driver = webdriver.Chrome()
driver.maximize_window()
# Добавляем action
action = action_chains.ActionChains(driver)
# Установим тайм для драйвера
wait = WebDriverWait(driver, 60)
# Заходим на сайт
driver.get(site_url)
# Вводим логин
search_element = driver.find_element_by_id(login_id)
search_element.clear()
search_element.send_keys(login_text)
# Вводим пароль
search_element = driver.find_element_by_id(password_id)
search_element.send_keys(password_text)
# Нажимаем Войти
search_element = driver.find_element_by_id(submit_button_id)
search_element.click()
# Проваливаемся на сайт
# Переходим в Договоры
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_xpath))).click()
# Находим и нажимаем "Добавить" новый договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
# Находим поле Типа документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_type_input_xpath)))
# Вводим в поле текст
contract_type_name = unicode(contracts_type_name.decode("utf-8"))
search_element.send_keys(contract_type_name)
# Находим и нажимаем в списке нужный тип документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % contract_type_name))).click()
# Проставляем дату документа
today = date.today()
today = today.strftime("%d.%m.%Y")
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
search_element.send_keys(str(today))
search_element.send_keys(Keys.RETURN)
# Ждём пока не появятся комментарии. Служит обозначением, что внутреннее тестирование началось
search_element = wait.until(
	EC.visibility_of_any_elements_located((By.ID, comment_div_id)))
# Берём ID документа
url = driver.current_url
hash_tag = url[url.find('#') + 1:]
params = dict(x.split('=') for x in hash_tag.split('&'))
doc_id = params['id']
# ID документа созданного по шаблону (060 + ID документа)
barcode_template_doc = "060" + doc_id
#
reg_num = driver.find_element_by_id('regNum')
reg_num = reg_num.get_attribute('innerHTML')
reg_num = reg_num.strip()
# Переходим в раздел с переданным значением
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_file_button_xpath))).click()
# Нажимаем клавишу Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_add_button_xpath))).click()
time.sleep(1)
# Нажимаем на клавишу По шаблону
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_template_xpath)))
search_element.click()
# Выбераем шаблон
search_element = wait.until(
	EC.visibility_of_element_located((By.XPATH, create_template_xpath)))
search_element.click()
# Закрываем просмоторщик созданного файла
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_viewer_xpath))).click()
# Закрываем договор
search_element = wait.until(
	EC.element_to_be_clickable((By.ID, ok_button_id))).click()
time.sleep(5)
# Открываем подменю "Штрих-кода"
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, barcode_xpath))).click()
# Нажимаем Архив
time.sleep(1)
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, archive_xpath))).click()
# Находим поле ввода
time.sleep(1)
search_element = driver.find_element_by_id('barcode')
# Вводим данные
search_element.send_keys(barcode_folder_name)
search_element.send_keys(Keys.RETURN)
time.sleep(1)
search_element.send_keys(barcode_template_doc)
search_element.send_keys(Keys.RETURN)
# Спим (необходимо)
time.sleep(1)
# Проверка на наличие файлов
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, archive_table_include_xpath))
)
# Переключаемся на извлечение
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, remove_radiobutton_xpath))).click()
# Извлекаем
search_element = driver.find_element_by_id('barcode')
search_element.send_keys(barcode_template_doc)
search_element.send_keys(Keys.RETURN)
# Переходим в Договоры
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_xpath))).click()
# Спим
time.sleep(3)
# Переходим в договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_table_xpath))).click()
action.double_click().perform()
# Нажимаем кнопку с группой
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, test_group_button_xpath))).click()
# Нажимаем Делегировать
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delegation_button_xpath))).click()
# Нажимаем Сотрудник
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employee_button_xpath))).click()
# Выбераем сотрудника
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delegation_member_xpath))).click()
time.sleep(1)
action.send_keys(Keys.RETURN).perform()  # Enter
time.sleep(1)
# Закрываем окно с выбором сотрудников
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, close_button_xpath))).click()
# Спим
time.sleep(10)
# Нажимаем кнопку добавления контрагента
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, linkage_button_xpath))).click()
# Нажимаем Заказчик
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employee_contragent_add_xpath))).click()
# Нажимаем Юр. Лицо
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, customer_contragent_add_xpath))).click()
# Выбираем Юр. Лицо
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, flexbby_contragent_add_xpath))).click()
time.sleep(1)
action.send_keys(Keys.RETURN).perform()  # Enter
#TODO: Сделать проверку на инвизибл перед нажатием "удалить" !!!
time.sleep(10)
# Удаляем контрагента
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_contragent_button_xpath))).click()
# Подтверждаем
# Нажимаем Enter
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_delete_contract_xpath))).click()
#
time.sleep(15)
# Делаем скриншот
scr_name = today + "_" + "docID" + doc_id + "_" + "complex" + "_" + "test" + ".png"
driver.save_screenshot('C:\Users\Operator\Desktop\Testing\Tests\screens\\%s' % scr_name)
# Удаить договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_contract_xpath))).click()
# Нажимаем Enter
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_delete_contract_xpath))).click()
# Закрыть Хром
time.sleep(sleep_time)
driver.close()
