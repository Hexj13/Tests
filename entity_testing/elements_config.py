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
""""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
submit_button_id = 'enter'
#
get_data_id = 'getCompanyData'
