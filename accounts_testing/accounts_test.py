# coding=utf-8

import datetime
import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from accounts_elements_config import *
from accounts_content_config import *

# Устанавливаем драйвер
driver = webdriver.Chrome()
# Максимайз
driver.maximize_window()
# Устанавливаем экшен
action = action_chains.ActionChains(driver)
# Установим тайм для драйвера
wait = WebDriverWait(driver, 30)
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
time.sleep(two_sec)
# Находим в меню Юр. лица
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, entity_menu_button_xpath))).click()
# Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()

""""ОБЩЕЕ"""
# Вводим ИНН
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
search_element.send_keys(inn)
# Нажимаем кнопку
search_element = driver.find_element_by_id(get_data_id).click()
# Выбираем компанию
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, company_window_xpath.format(inn=inn)))).click()
# Берём ID документа
url = driver.current_url
hash_tag = url[url.find('#') + 1:]
params = dict(x.split('=') for x in hash_tag.split('&'))
doc_id = params['id']
# Проставляем email
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, email_input_xpath)))
search_element.send_keys(email_text)
# Проставляем site
search_element = driver.find_element_by_xpath(site_input_xpath).send_keys(site_example_text)
# Проставляем  phone
search_element = driver.find_element_by_xpath(phone_input_xpath).send_keys(phone_text)
# today date
today = datetime.date.today()
today_str = today.strftime("%d.%m.%Y")
# tomorrow date
tomorrow = today + datetime.timedelta(days=1)
tomorrow_str = tomorrow.strftime("%d.%m.%Y")
# Проставляем дату диактивации
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath)))
search_element.clear()
search_element.send_keys(tomorrow_str)
# Проставляем комментарий
search_element = driver.find_element_by_xpath(comment_input_xpath).send_keys(comment_text)
# Добавляем тег
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_tag_button_xpath))).click()
# Выбираем тег
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, selected_tag_xpath % tag_name))).click()
action.send_keys(Keys.RETURN).perform()
# Закрываем окно с тегами
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, close_window_button_xpath))).click()
time.sleep(two_sec)
# Нажимаем кнопку Добавить Комментарий
search_element = driver.find_element_by_xpath(add_comment_button_xpath).click()
# Находим поле и вводим текст
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, comment_textarea_xpath))).click()
action.send_keys(comment_text).perform()
# Нажимаем Сохранить
search_element = driver.find_element_by_xpath(save_comment_button_xpath).click()
# Спим
time.sleep(two_sec)
# Нажимаем Добавить Автивность
search_element = driver.find_element_by_xpath(activity_add_button_xpath).click()
# Находим поле Типа активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
# Вводим в поле текст
activity_type_text = unicode(activity_type_text.decode("utf-8"))
search_element.send_keys(activity_type_text)
# Находим и нажимаем в списке нужный тип активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % activity_type_text))).click()
time.sleep(two_sec)

""" TODO: Добавление парамов в ОБЩЕМ!!!  """
# # Переходим в Параметры
# search_element = wait.until(
# 	EC.element_to_be_clickable((By.XPATH, params_button_xpath))).click()
# # Нажимаем на поле значения
# search_element = wait.until(
# 	EC.element_to_be_clickable((By.XPATH, empty_table_xpath))).click()
# # Вводим в поле текст
# params_text = unicode(params_text.decode("utf-8"))
# action.send_keys(params_text)
# # Находим и нажимаем в списке нужный тип параметра
# search_element = wait.until(
# 	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % params_text))).click()
#
""""""
# Нажимаем Структура
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, structure_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Спим
time.sleep(two_sec)
# Декод
structure_name = unicode(structure_name.decode("utf-8"))
# Вводим название Структуры
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, structure_name_input_xpath))).send_keys(structure_name)
# Спим
time.sleep(two_sec)
# Нажимаем Ок
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
# Спим
time.sleep(two_sec)

""""РЕКВИЗИТЫ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Реквизиты
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, recvisits_button_xpath))).click()
# Вводим ОКПО
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, okpo_input_xpath)))
search_element.send_keys(okpo_text)
# Вводим Сокращённое имя
search_element = driver.find_element_by_xpath(foreign_short_name_input_xpath).send_keys(foreign_short_name_text)
# Вводим Полное имя
search_element = driver.find_element_by_xpath(foreign_name_input_xpath).send_keys(foreign_name_text)
# Enter по адресу
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, street_name_input_xpath)))
search_element.send_keys(Keys.RETURN)
# Выбираем первый выпавший адрес для активации Google Maps
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, proposed_address_div_xpath)))
search_element.click()
# Спим
time.sleep(two_sec)
# Нажимаем Добавить вид активности
search_element = driver.find_element_by_xpath(activity_type_button_xpath)
search_element.click()
# Вводим код активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, code_activity_type_input_xpath)))
search_element.send_keys(activity_code)
# Вводим имя активности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, name_activity_type_input_xpath)))
search_element.send_keys(activity_name_text)
# Вводим коммент
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, comment_input_xpath)))
search_element.send_keys(comment_text)

"""БАНКОВСКИЕ РЕКВИЗИТЫ"""
# Нажимаем Добавить банковский реквизит
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_bank_button_xpath))).click()
# Вводим БИК
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, bik_bank_xpath)))
search_element.send_keys(bik_number_text)
# Вводим Имя банка
search_element = driver.find_element_by_xpath(name_foreign_bank_xpath).send_keys(bank_name_text)
# Вводим ИНН
search_element = driver.find_element_by_xpath(inn_bank_xpath).send_keys(inn_bank_text)
# Вводим КПП
search_element = driver.find_element_by_xpath(kpp_bank_xpath).send_keys(kpp_bank_text)
# Вводим Р/с Банка
search_element = driver.find_element_by_xpath(rs_bank_xpath).send_keys(rs_bank_text)
# Вводим Л/с Банка
search_element = driver.find_element_by_xpath(ls_bank_xpath).send_keys(ls_bank_text)
# Проставляем Основной счёт
search_element = driver.find_element_by_xpath(main_bank_xpath).click()
# Вводим дату диактивации
search_element = driver.find_element_by_xpath(deactivateDate_bank_xpath).send_keys(tomorrow_str)
# Вводим коммент
search_element = driver.find_element_by_xpath(text_comment_bank_xpath).send_keys(comment_text)
# Нажимаем ОК
search_element = driver.find_element_by_xpath(ok_button_window_xpath).click()

"""ДОГОРОВЫ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Договоры в меню
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Находим поле Типа документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
# Вводим в поле текст
contract_type_name = unicode(contracts_type_name.decode("utf-8"))
search_element.send_keys(contract_type_name)
# Находим и нажимаем в списке нужный тип документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % contract_type_name))).click()
# Проставляем дату документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
search_element.send_keys(today_str)
search_element.send_keys(Keys.RETURN)
# Спим
time.sleep(five_sec)
# Закрываем договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
time.sleep(three_sec)

"""ЗАКАЗЫ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Заказы в меню
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, orders_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Проставляем дату документа
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_date_input_xpath)))
search_element.send_keys(today_str)
search_element.send_keys(Keys.RETURN)
# Спим
time.sleep(five_sec)
# Закрываем заказ
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
time.sleep(three_sec)

"""СЧЕТА"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Счета в меню
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, accounts_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Находим поле Типа счёта
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, account_type_input_xpath)))
# Вводим в поле текст
account_type_name = unicode(account_type_name.decode("utf-8"))
search_element.send_keys(account_type_name)
# Находим и нажимаем в списке нужный тип счёта
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % account_type_name))).click()
# Нажимаем на кнопку для выбора договора
search_element = driver.find_element_by_xpath(account_doc_select_button_xpath).click()
#
time.sleep(two_sec)
# Выбираем договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
action.send_keys(Keys.RETURN).perform()
# Спим
time.sleep(three_sec)
# Закрываем счёт
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
# Спим
time.sleep(three_sec)

"""ПРОДАЖИ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Продажи в меню
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, sales_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Находим поле Типа продажи
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, doc_type_input_xpath)))
# Вводим в поле текст
sales_type_name = unicode(sales_type_name.decode("utf-8"))
search_element.send_keys(sales_type_name)
# Находим и нажимаем в списке нужный тип продажи
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % sales_type_name))).click()
# Спим
time.sleep(three_sec)
# Закрываем продажи
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
# Спим
time.sleep(three_sec)

"""СОГЛАСОВАНИЕ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Согласование в меню
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, matching_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Спим
time.sleep(four_sec)
# Закрываем продажи
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_xpath))).click()
# Спим
time.sleep(three_sec)

"""ФАЙЛЫ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Файлы
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, files_button_xpath))).click()
# Нажиаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_file_button_xpath))).click()
# Добавить Папку
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_folder_button_xpath))).click()
# Спим
time.sleep(two_sec)
# Вводим название Папки
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, file_name_input_xpath))).send_keys(structure_name)
# Спим
time.sleep(two_sec)
# Нажимаем Ок
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_id_window_button_xpath))).click()
# Спим
time.sleep(two_sec)

"""УДАЛЕНИЕ ССЫЛОК"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Удаляем Договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, contracts_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
time.sleep(four_sec)
# Удаляем Заказ
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, orders_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
time.sleep(four_sec)
# Удаляем Счёт
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, accounts_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
time.sleep(four_sec)
# Удаляем Продажу
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, sales_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
time.sleep(four_sec)
# Удаляем Согласование
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, matching_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, select_row_in_table_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
time.sleep(four_sec)
# Прохоим в Общее
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, overall_button_xpath))).click()
# Проходим в Сотрудники
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employees_button_xpath))).click()
# Выбираем сотрудника ссылающегося на док
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employee_table_xpath))).click()
# Нажимаем Удалить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
# Нажимаем ОК
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
# Спим
time.sleep(two_sec)
# Проходим в Структуру
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, structure_button_xpath))).click()
# Выбираем структуру ссылающегося на док
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, employee_table_xpath))).click()
# Нажимаем Удалить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_button_xpath))).click()
# Нажимаем ОК
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
# Спим
time.sleep(two_sec)

"""Delete&Screen&Close"""
# Делаем скриншот
scr_name = today_str + "_" + "docID" + doc_id + "_" + "entity" + "_" + "test" + ".png"
driver.save_screenshot('C:\Users\Operator\Desktop\Testing\Tests\screens\\%s' % scr_name)
time.sleep(two_sec)
# Удаить договор
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, delete_entity_button_xpath))).click()
# Нажимаем Enter
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_button_window_xpath))).click()
# Закрыть Хром
time.sleep(two_sec)
driver.close()
