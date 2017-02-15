# coding=utf-8

import datetime
import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from contacts_elements_config import *
from contacts_content_config import *

# Driver init
driver = webdriver.Chrome()
# Maximaze
driver.maximize_window()
# Action init
action = action_chains.ActionChains(driver)
# Установим тайм для драйвера
wait = WebDriverWait(driver, 40)
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
	EC.element_to_be_clickable((By.XPATH, contacts_menu_button_xpath))).click()
# Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Today date
today = datetime.date.today()
today_str = today.strftime("%d.%m.%Y")
# Tomorrow date
tomorrow = today + datetime.timedelta(days=two_sec)
tomorrow_str = tomorrow.strftime("%d.%m.%Y")
# Birthday date
birthday = today - datetime.timedelta(days=2)
birthday_str = birthday.strftime("%d.%m.%Y")

"""ОБЩЕЕ"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Вводим Name
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, name_input_xpath)))
name_text = unicode(name_text.decode("utf-8"))
search_element.send_keys(name_text)
time.sleep(one_sec)
# Вводим Surname
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, surname_input_xpath)))
surname_text = unicode(surname_text.decode("utf-8"))
search_element.send_keys(surname_text)
time.sleep(one_sec)
# Вводим Patronymic
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, patronymic_input_xpath)))
patronymic_text = unicode(patronymic_text.decode("utf-8"))
search_element.send_keys(patronymic_text)
# Вводим Phone
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, phone_input_xpath)))
search_element.send_keys(phone_text)
# Вводим Email
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, email_input_xpath)))
search_element.send_keys(email_text)
# Выбираем пол
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, gender_div_xpath))).click()
gender_text = unicode(gender_text.decode("utf-8"))
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, popup_menu_select_xpath % gender_text))).click()
time.sleep(one_sec)
# Проставляем Описание
comment_text = unicode(comment_text.decode("utf-8"))
search_element = driver.find_element_by_xpath(comment_textarea_xpath).send_keys(comment_text)
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
	EC.element_to_be_clickable((By.XPATH, commentInput_textarea_xpath))).click()
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
time.sleep(one_sec)
# Нажимаем Должности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, position_button_xpath))).click()
# Нажимаем Добавить
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_button_xpath))).click()
# Нажимаем кнопку выбора Компании
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, company_choose_button_xpath))).click()
# Выбираем Юр. Лицо
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, flexbby_contragent_add_xpath))).click()
time.sleep(one_sec)
action.send_keys(Keys.RETURN).perform()
# Нажимаем кнопку выбора Должности
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, position_choose_button_xpath))).click()
# Выбираем Должность
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, director_contragent_add_xpath))).click()
time.sleep(two_sec)
action.send_keys(Keys.RETURN).perform()
# Нажимаем ОК
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, ok_id_window_button_xpath))).click()

"""ДОПОЛНИТЕЛЬНО"""
# Проверяем на отсутвие shadow
search_element = wait.until(
	EC.invisibility_of_element_located((By.ID, shadow_id)))
# Нажимаем Дополнительно
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, additionally_button_xpath))).click()
# Вводим День Рождения
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, birthday_input_xpath))).send_keys(birthday_str)
# Вводим ИНН
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, inn_input_xpath)))
search_element.send_keys(inn_text)
# Вводим СНИЛС
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, snils_input_xpath)))
search_element.send_keys(snils_text)
# Вводим Диактивацию
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, deactivateDate_input_xpath)))
search_element.send_keys(tomorrow_str)
# Добавить Документ
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_buton_doc_xpath)))
search_element.click()
time.sleep(two_sec)
"""КОСТЫЛЬ начался"""  # TODO: после исправления баги с полями в физ.лице нужно будет это всё переделать!
# Вводим Описание
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, comment_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(comment_input_xpath).send_keys(comment_text)
# Вводим Серию
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, series_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(series_input_xpath).send_keys(series_text)
# Вводим Номер
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, number_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(number_input_xpath).send_keys(number_text)
# Вводим дату выдачи паспорта
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, deliveryDate_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(deliveryDate_input_xpath).send_keys(today_str)
# Вводим дату истечения паспорта
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, expired_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(expired_input_xpath).send_keys(tomorrow_str)
# Вводим Кто Выдал
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, issuer_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(issuer_input_xpath).send_keys(issuer_text)
# Вводим Номер Кто Выдал
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, issuerCode_input_xpath))).click()
time.sleep(one_sec)
search_element = driver.find_element_by_xpath(issuerCode_input_xpath).send_keys(issuerCode_text)
"""КОСТЫЛЬ закончился"""
# Добавить Адрес
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, add_buton_adrr_xpath)))
search_element.click()
time.sleep(one_sec)
#
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, street_name_input_xpath))).click()
time.sleep(one_sec)
adrr_text = unicode(adrr_text.decode("utf-8"))
search_element = driver.find_element_by_xpath(street_name_input_xpath).send_keys(adrr_text)
search_element = driver.find_element_by_xpath(street_name_input_xpath).send_keys(Keys.RETURN)
time.sleep(one_sec)
# Выбираем первый выпавший адрес для активации Google Maps
search_element = wait.until(
	EC.element_to_be_clickable((By.XPATH, proposed_address_div_xpath)))
search_element.click()

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
