# coding=utf-8


#
comment_button_xpath = "//div[@id='Comment_objectID' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@id='visiblePart']//a[text()='%s']"
#
menu_button_xpath = "//div[@class='qx-mainmenu']//div[text()= '%s']"
#
to_matching_button_xpath = "//div[@class='qx-button-common-border' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                           "'Отправить на согласование' ] "
#
add_button_element_xpath = ".//div[.='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                           "ancestor::div[contains(@style,'display: none')])] "
#
tab_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'{name}')and " \
            "not(ancestor::div[contains(@style," \
            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_file_button_xpath = "//div[@class = 'qx-button-common-border-left' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                        "'Добавить'] "
#
edit_file_button_xpath = "//div[@class = 'qx-button-leading-border-middle' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                         "'Редактировать'] "
#
add_folder_button_xpath = "//div[@class = 'qx-menu-border' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                          "'Папку'] "
#
add_button_xpath = "//div[text() ='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                   "ancestor::div[contains(@style,'display: none')])]"
#
ok_delete_button_window_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
pencil_window_xpath = "//div[@class = 'qx-window']//div[@class = 'qooxdoo-table-cell' and (text()='карандаш')]"
#
ok_id_window_button_xpath = "//div[@class = 'qx-window']//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
test_group_button_xpath = "//div[text() = 'Тест-группа']"
#
delegation_button_xpath = "//div[contains(text(), 'Делегировать')]"
#
group_button_xpath = "//div[text()='Группа' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                     "ancestor::div[contains(@style,'display: none')])]"
#
delete_contragent_button_xpath = "//div[@class = 'qx-strip-dialog-container-underline' and not(ancestor::div[" \
                                 "contains(@style,'display: none')])][1]//div[@id = 'delete-button']"
#
attribute_xpath = "{parent}//*[@id = '{id}' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])and not(div[contains(@style," \
                  "'display:none')])and not(div[contains(@style,'display: none')])]{child}"
#
attribute_child_xpath = "//*[@id = '{id}' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])and not(div[contains(@style," \
                        "'display:none')])and not(div[contains(@style,'display: none')])]{child}"
#
window_attribute_xpath = "//div[@class = 'qx-window']//*[@id = '{id}' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])and not(div[contains(@style," \
                         "'display:none')])and not(div[contains(@style,'display: none')])]{child}"
#
employee_contragent_add_xpath = "//div[@class = 'qx-menu-border']//div[text() = 'Заказчик']"
#
close_window_button_xpath = "//div[@class='qx-window']//div[@id='ok-button']"
#
qxmenu_button_xpath = "//div[@class = 'qx-menu-border']//div[text() = '%s']"
#
archive_table_include_xpath = ".//div[@class='qooxdoo-table-cell' and (contains(text(), 'Комплексное тестирование')) " \
                              "and not(ancestor::div[contains(" \
                              "@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
selected_tag_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@class = " \
                     "'qooxdoo-table-cell']//span[text() = '%s'] "
#
employee_table_xpath = "//parent::div[@class = 'qooxdoo-table-cell' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
company_window_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])][2]"
#
popup_menu_select_xpath = "//div[@class='qx-popup' and not(contains(@style," \
                          "'display:none'))and not(contains(@style,'display: none'))]//div[text()='%s']"
#
select_row_in_table_xpath = "//div[@class = 'qx-table-row' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
qx_menu_menu_select_xpath = "//div[@class='qx-menu-border' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text(" \
                            ")='%s'] "
#
delegation_group_xpath = "//div[text()='Логистика' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(" \
                         "ancestor::div[contains(@style,'display: none')])]"
#
contracts_template_xpath = "//div[@class='qx-menu-border']//div[text()='По шаблону']"
#
contracts_table_xpath = ".//div[contains(text(), 'Комплексное тестирование') and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
cell_in_table_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='%s') and not(" \
                      "ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
reference_obj_xpath = "//div[@class='qx-window'and not(div[contains(@style, 'display:none')])and not(div[contains(@style,'display: none')])]//div[@class = 'qooxdoo-table-cell' and(text()='{text}')]"
#
reference_xpath = "//div[@class='qx-window'and not(div[contains(@style, 'display:none')])and not(div[contains(@style,'display: none')])]//div[@class = 'qooxdoo-table-cell' and(text()='%s')]"
#
dialog_attribute_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//*[@id = '{id}']"


