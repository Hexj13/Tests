# coding=utf-8


""""Seconds"""
#
sleep_time = 25
#


""""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
comment_div_id = 'commentTextSystem'
#
submit_button_id = 'enter'
#
ok_button_id = 'okb'
#

""""XPATH"""
#
test_group_button_xpath = "//div[text() = 'Тест-группа']"
#
delegation_button_xpath = "//div[contains(text(), 'Делегировать')]"
#
exit_button_xpath = "//div[contains(@style, 'close.png') and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(" \
                    "ancestor::div[contains(@style,'display: none')])]"
#
delegation_member_xpath = "//div[text()='Чёсов Роман Геннадьевич' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(" \
                          "ancestor::div[contains(@style,'display: none')])]"
#
employee_button_xpath = "//div[text()='Сотрудник' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                        "ancestor::div[contains(@style,'display: none')])]"
#
contracts_xpath = '//div[text()="Договоры"]'
#
barcode_xpath = "//div[text()='Штрих-код']"
#
archive_xpath = "//div[@class='qx-mainmenu']//div[text()='Архив']"
#
contracts_add_button_xpath = ".//div[.='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                             "ancestor::div[contains(@style,'display: none')])] "
#
contracts_type_input_xpath = ".//div[@id='documentTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
                             "not(ancestor::div[contains(@style,'display: none')])]//input "
#
popup_menu_select_xpath = "//div[@class='qx-popup']//div[text()='%s']"
#
doc_date_input_xpath = "//div[@id='docDate']//input"
#
contracts_file_button_xpath = ".//div[contains(text(), 'Файлы') and not(ancestor::div[contains(@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
contracts_template_xpath = "//div[@class='qx-menu-border']//div[text()='По шаблону']"
#
create_template_xpath = "//div[text()='Тест шаблон (1)']"
#
# ok_button_viewer = ".//div[contains(text(), 'OK') and not(ancestor::div[contains(@style,'display:none')])and not(" \
#                    "ancestor::div[contains(@style,'display: none') and not(ancestor::div[contains(@id,'okb')])])] "
#
ok_button_viewer_xpath = "//div[@class='qx-window']//div[text()='OK']"
#
# table_config_button_xpath = ".//img[@src = 'resource/webclient/images/table/table_config.png' and not(
# ancestor::img[" \ "contains(@style,'display:none')])and not(ancestor::img[contains(@style,'display: " \ "none')])] "
# loading_xpath = "div[text()='Передача данных']"
#
remove_radiobutton_xpath = "//div[@id='_removeDocument']//div[@class='qx-radiobutton']"
#
archive_table_include_xpath = ".//div[@class='qooxdoo-table-cell' and (contains(text(), 'Комплексное тестирование')) " \
                              "and not(ancestor::div[contains(" \
                              "@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
contracts_table_xpath = ".//div[contains(text(), 'Комплексное тестирование') and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
close_button_xpath = "//div[@id = 'close' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
linkage_button_xpath = "//div[@id = 'linkageID_selectButton' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
delete_contract_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_delete_contract_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
employee_contragent_add_xpath = "//div[@class = 'qx-menu-border']//div[text() = 'Заказчик']"
#
customer_contragent_add_xpath = "//div[@class = 'qx-menu-border' and not(ancestor::div[contains(@style," \
                                "'display:none')])and " \
                                "not(ancestor::div[contains(@style,'display: none')])]//div[text() = 'Юр. лицо']"
#
flexbby_contragent_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Флексби Солюшнс') and not(" \
                               "ancestor::div[contains(@style," \
                               "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
# delete_contragent_button_xpath = "//div[@id = 'delete-button' and not(ancestor::div[contains(@style," \
#                                  "'display:none')]) and " \
#                                  "not(ancestor::div[contains(@style,'display: none')])]"
delete_contragent_button_xpath = "//div[@class = 'qx-strip-dialog-container-underline' and not(ancestor::div[" \
                                 "contains(@style,'display: none')])][1]//div[@id = 'delete-button']"
