# coding=utf-8


""""Seconds"""
#
two_sec = 2
#
three_sec = 3
#
four_sec = 4
#
five_sec = 5
#
ten_sec = 10

""""XPATH"""

"""КНОПКИ"""

#
overall_button_xpath = "//div[contains(text(),'Общее')and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
contracts_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Договоры')and " \
                         "not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
accounts_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Счета')and " \
                        "not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
orders_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Заказы')and " \
                      "not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
employees_button_xpath = "//div[contains(text(),'Сотрудники')and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
entity_menu_button_xpath = "//div[text() = 'Юр. лица']"
#
add_button_xpath = "//div[text() ='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                   "ancestor::div[contains(@style,'display: none')])]"
#
delete_button_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_button_window_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
ok_button_xpath = "//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
recvisits_button_xpath = "//div[contains(text(),'Реквизиты')and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
activity_type_button_xpath = "//div[@id = 'CompanyActivityType_objectID'and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@class = " \
                             "'qx-button-common-border']"
#
employee_delete_button_xpath = "//div[@class = 'qx-button-common-border-middle' and not(ancestor::div[contains(@style," \
                               "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[" \
                               "contains(text(), 'Удалить')] "
"""ИНПУТЫ"""
#
doc_date_input_xpath = "//div[@id='docDate']//input"
#
contracts_type_input_xpath = ".//div[@id='documentTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
                             "not(ancestor::div[contains(@style,'display: none')])]//input "
#
account_type_input_xpath = ".//div[@id='planTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
                           "not(ancestor::div[contains(@style,'display: none')])]//input"
#
inn_input_xpath = "//input[@id = 'inn' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
site_input_xpath = "//input[@id = 'url' and not(ancestor::div[contains(@style," \
                   "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
phone_input_xpath = "//input[@id = 'phone' and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
email_input_xpath = "//input[@id = 'email' and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
deactivateDate_input_xpath = "//div[@id = 'deactivateDate' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input"
#
comment_input_xpath = "//input[@id = 'comment' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
okpo_input_xpath = "//input[@id = 'okpo' and not(ancestor::div[contains(@style," \
                   "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
foreign_short_name_input_xpath = "//input[@id = 'foreignLegalShortName' and not(ancestor::div[contains(@style," \
                                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
foreign_name_input_xpath = "//input[@id = 'foreignLegalName' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
street_name_input_xpath = "//input[@id = 'streetAddress' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
code_activity_type_input_xpath = "//input[@id = 'code' and not(ancestor::div[contains(@style," \
                                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
name_activity_type_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
                                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"

"""ОСТАЛЬНОЕ"""
#
employee_table_xpath = "//parent::div[@class = 'qooxdoo-table-cell' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
company_window_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])][2]"
#
proposed_address_div_xpath = "//div[@id = 'proposed_addresses' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//a"
#
popup_menu_select_xpath = "//div[@class='qx-popup' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text()='%s']"

"""БАНКОВСКИЕ РЕКВИЗИТЫ XPATH"""

add_bank_button_xpath = "//div[@class = 'qx-button-leading-border-left' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                        "'Добавить'] "
#
text_comment_bank_xpath = "//textarea[@id = 'comment' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
inn_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = 'inn']"
#
bik_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = 'bik']"
#
kpp_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = 'kpp']"
#
inn_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = 'inn']"
#
rs_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = " \
                "'accountNumber']"
#
ls_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = " \
                "'personalAccount']"
#
name_foreign_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//input[@id = " \
                          "'nameForeign']"
#
main_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@id = " \
                  "'main']"
#
deactivateDate_bank_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@id = " \
                            "'deactivateDate']//input"
""""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
submit_button_id = 'enter'
#
get_data_id = 'getCompanyData'
#
shadow_id = 'shadow'
#
