# coding=utf-8


""""Seconds"""
one_sec = 1
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

"""XPATH"""

"""КНОПКИ"""
#
ok_button_window_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
add_button_xpath = "//div[text() ='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                   "ancestor::div[contains(@style,'display: none')])]"
#
contracts_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Договоры')and " \
                         "not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
contacts_menu_button_xpath = "//div[text() = 'Физ. лица']"
#
additionally_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text()," \
                            "'Дополнительно')and not(" \
                            "ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_tag_button_xpath = "//div[@id = 'addTag'and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
close_window_button_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[" \
                            "@id='close'] "
#
activity_add_button_xpath = "//div[@id = 'addActivity' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                            "ancestor::div[contains(@style,'display: none')])]"
#
position_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Должности')and " \
                        "not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_comment_button_xpath = "//div[@id = 'newCommentButton' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
save_comment_button_xpath = "//div[@id = 'saveComment' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
company_choose_button_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@id = " \
                              "'companyID']//div[@id = 'choose-button']"
#
position_choose_button_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                               "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@id = " \
                               "'positionID']//div[@id = 'choose-button']"
#
ok_button_xpath = "//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_id_window_button_xpath = "//div[@class = 'qx-window']//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_buton_doc_xpath = "//div[@id = 'ContactPersonDocument_contactPersonID']//div[text() = 'Добавить']"
#
add_buton_adrr_xpath = "//div[@id = 'Address_objectID']//div[text() = 'Добавить']"
#
orders_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Заказы')and " \
                      "not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
accounts_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Счета')and " \
                        "not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
account_doc_select_button_xpath = "//div[@id = 'parentID']//div[2]"
#
sales_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Продажи')and not(" \
                     "ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
matching_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text()," \
                        "'Согласование')and not(" \
                        "ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
files_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Файлы')and " \
                     "not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_file_button_xpath = "//div[@id = 'addFileButton' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_folder_button_xpath = "//div[@class = 'qx-menu-border' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                          "'Папку'] "
#
delete_button_xpath = "//div[@class = 'qx-button-common-border-middle' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[" \
                      "contains(text(), 'Удалить')] "
#
delete_entity_button_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
overall_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Общее')and not(" \
                       "ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"

"""INPUT"""
#
file_name_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
account_type_input_xpath = ".//div[@id='planTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
                           "not(ancestor::div[contains(@style,'display: none')])]//input"
#
doc_date_input_xpath = "//div[@id='docDate']//input"
#
street_name_input_xpath = "//input[@id = 'streetAddress' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
name_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
                   "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
surname_input_xpath = "//input[@id = 'surname' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
patronymic_input_xpath = "//input[@id = 'patronymic' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
phone_input_xpath = "//input[@id = 'phone' and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
email_input_xpath = "//input[@id = 'email' and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
doc_type_input_xpath = ".//div[@id='documentTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
                       "not(ancestor::div[contains(@style,'display: none')])]//input "
#
birthday_input_xpath = ".//div[@id='birthday' and not(ancestor::div[contains(@style,'display:none')])and " \
                       "not(ancestor::div[contains(@style,'display: none')])]//input "
#
deactivateDate_input_xpath = ".//div[@id='deactivateDate' and not(ancestor::div[contains(@style,'display:none')])and " \
                             "not(ancestor::div[contains(@style,'display: none')])]//input "
#
inn_input_xpath = "//input[@id = 'inn' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
snils_input_xpath = "//input[@id = 'snils' and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
comment_input_xpath = "//input[@id = 'comment' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
series_input_xpath = "//input[@id = 'series' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
number_input_xpath = "//input[@id = 'number' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
issuerCode_input_xpath = "//input[@id = 'issuerCode' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
issuer_input_xpath = "//input[@id = 'issuer' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
deliveryDate_input_xpath = ".//div[@id='deliveryDate' and not(ancestor::div[contains(@style,'display:none')])and " \
                           "not(ancestor::div[contains(@style,'display: none')])]//input "
#
expired_input_xpath = ".//div[@id='expired' and not(ancestor::div[contains(@style,'display:none')])and " \
                      "not(ancestor::div[contains(@style,'display: none')])]//input "

"""OTHER"""
#
select_row_in_table_xpath = "//div[@class = 'qx-table-row' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
proposed_address_div_xpath = "//div[@id = 'proposed_addresses' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//a"
#
commentInput_textarea_xpath = "//textarea[@id = 'commentInput' and not(ancestor::div[contains(@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
gender_div_xpath = "//div[@id = 'gender' and not(ancestor::div[contains(@style," \
                   "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
comment_textarea_xpath = "//textarea[@id = 'comment' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
popup_menu_select_xpath = "//div[@class='qx-popup' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text()='%s']"
#
selected_tag_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@class = " \
                     "'qooxdoo-table-cell']//span[text() = '%s'] "
#
flexbby_contragent_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Флексби Солюшнс') and not(" \
                               "ancestor::div[contains(@style," \
                               "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
director_contragent_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Генеральный директор') and not(" \
                                "ancestor::div[contains(@style," \
                                "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"

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

"""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
submit_button_id = 'enter'
#
shadow_id = 'shadow'
#
