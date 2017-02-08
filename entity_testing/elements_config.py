# coding=utf-8


""""Seconds"""
#
two_sec = 2
#
five_sec = 5
#
ten_sec = 10

""""XPATH"""
#
entity_menu_button_xpath = "//div[text() = 'Юр. лица']"
#
add_button_xpath = ".//div[.='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                   "ancestor::div[contains(@style,'display: none')])]"
#
delete_button_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_delete_button_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
inn_input_xpath = "//input[@id = 'inn' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
company_window_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])][2]"
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
recvisits_button_xpath = "//div[contains(text(),'Реквизиты')and not(ancestor::div[contains(@style," \
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
proposed_address_div_xpath = "//div[@id = 'proposed_addresses' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//a"
#
activity_type_button_xpath = "//div[@id = 'CompanyActivityType_objectID'and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@class = " \
                             "'qx-button-common-border']"
#
code_activity_type_input_xpath = "//input[@id = 'code' and not(ancestor::div[contains(@style," \
                                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
name_activity_type_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
                                 "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
overall_button_xpath = "//div[contains(text(),'Общее')and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
employees_button_xpath = "//div[contains(text(),'Сотрудники')and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
""""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
submit_button_id = 'enter'
#
get_data_id = 'getCompanyData'
