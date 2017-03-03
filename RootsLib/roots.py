# coding=utf-8


class SleepSeconds:
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	TWENTY = 20


class TextColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


"""BUTTONS XPATH"""
#
contacts_menu_button_xpath = "//div[text() = 'Физ. лица']"
#
position_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Должности')and " \
                        "not(ancestor::div[contains(@style," \
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
add_buton_doc_xpath = "//div[@id = 'ContactPersonDocument_contactPersonID']//div[text() = 'Добавить']"
#
add_buton_adrr_xpath = "//div[@id = 'Address_objectID']//div[text() = 'Добавить']"
#
delete_entity_button_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
to_matching_button_xpath = "//div[@class='qx-button-common-border' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                           "'Отправить на согласование' ] "
#
archive_button_xpath = "//div[@class='qx-mainmenu']//div[text()='Архив']"
#
contracts_add_button_xpath = ".//div[.='Добавить' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                             "ancestor::div[contains(@style,'display: none')])] "
#
contracts_main_menu_button_xpath = '//div[text()="Договоры"]'
#
barcode_xpath = "//div[text()='Штрих-код']"
#
exit_button_xpath = "//div[contains(@style, 'close.png') and not(ancestor::div[contains(@style," \
                    "'display:none')])and not(" \
                    "ancestor::div[contains(@style,'display: none')])]"
#
activities_menu_button_xpath = "//div[text() = 'Активности']"
#
members_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Участники')and " \
                       "not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
activities_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text()," \
                          "'Активности')and " \
                          "not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_file_button_xpath = "//div[@class = 'qx-button-common-border-left' and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                        "'Добавить'] "
#
add_folder_button_xpath = "//div[@class = 'qx-menu-border' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[text() = " \
                          "'Папку'] "
#
activity_add_button_xpath = "//div[@id = 'addActivity' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                            "ancestor::div[contains(@style,'display: none')])]"
#
overall_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Общее')and not(" \
                       "ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_tag_button_xpath = "//div[@id = 'addTag'and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
params_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Параметры')and not(" \
                      "ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
contracts_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Договоры')and " \
                         "not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
structure_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Структура')and " \
                         "not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
files_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Файлы')and " \
                     "not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
additionally_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Дополнительно')and " \
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
sales_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text(),'Продажи')and not(" \
                     "ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
matching_button_xpath = "//div[@class = 'qx-flexbby-tabview-button-underlined']//div[contains(text()," \
                        "'Согласование')and not(" \
                        "ancestor::div[contains(@style," \
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
delete_button_id_xpath = "//div[@id = 'deleteb' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_button_window_xpath = "//div[@class = 'qx-window']//div[contains(text(), 'OK')]"
#
ok_button_xpath = "//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                  "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
ok_id_window_button_xpath = "//div[@class = 'qx-window']//div[@id = 'okb' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
recvisits_button_xpath = "//div[contains(text(),'Реквизиты')and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
activity_type_button_xpath = "//div[@id = 'CompanyActivityType_objectID'and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[@class = " \
                             "'qx-button-common-border']"
#
delete_button_xpath = "//div[@class = 'qx-button-common-border-middle' and not(ancestor::div[contains(@style," \
                      "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[" \
                      "contains(text(), 'Удалить')] "
#
account_doc_select_button_xpath = "//div[@id = 'parentID']//div[2]"
#
close_window_button_xpath = "//div[@class = 'qx-window' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//div[" \
                            "@id='close'] "
#
add_comment_button_xpath = "//div[@id = 'newCommentButton' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
save_comment_button_xpath = "//div[@id = 'saveComment' and not(ancestor::div[contains(@style," \
                            "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
add_file_button_id_xpath = "//div[@id = 'addFileButton' and not(ancestor::div[contains(@style," \
                           "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
test_group_button_xpath = "//div[text() = 'Тест-группа']"
#
delegation_button_xpath = "//div[contains(text(), 'Делегировать')]"
#
employee_button_xpath = "//div[text()='Сотрудник' and not(ancestor::div[contains(@style,'display:none')])and not(" \
                        "ancestor::div[contains(@style,'display: none')])]"
#
remove_radiobutton_xpath = "//div[@id='_removeDocument']//div[@class='qx-radiobutton']"
#
delete_contragent_button_xpath = "//div[@class = 'qx-strip-dialog-container-underline' and not(ancestor::div[" \
                                 "contains(@style,'display: none')])][1]//div[@id = 'delete-button']"
#
close_button_xpath = "//div[@id = 'close' and not(ancestor::div[contains(@style," \
                     "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
linkage_button_xpath = "//div[@id = 'linkageID_selectButton' and not(ancestor::div[contains(@style," \
                       "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#

"""INPUTS XPATH"""
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
birthday_input_xpath = ".//div[@id='birthday' and not(ancestor::div[contains(@style,'display:none')])and " \
                       "not(ancestor::div[contains(@style,'display: none')])]//input "
#
snils_input_xpath = "//input[@id = 'snils' and not(ancestor::div[contains(@style," \
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
#
responsible_input_xpath = "//div[@id = 'responsibleID'  and not(ancestor::div[contains(@style,'display:none')])and " \
                          "not(ancestor::div[contains(@style,'display: none')])]//div[@id = 'choose-button']"
#
doc_date_input_xpath = "//div[@id='docDate']//input"
#
doc_type_input_xpath = ".//div[@id='documentTypeID' and not(ancestor::div[contains(@style,'display:none')])and " \
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
structure_name_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
file_name_input_xpath = "//input[@id = 'name' and not(ancestor::div[contains(@style," \
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
#

"""OTHER XPATH"""
#
gender_div_xpath = "//div[@id = 'gender' and not(ancestor::div[contains(@style," \
                   "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
director_contragent_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Генеральный директор') and not(" \
                                "ancestor::div[contains(@style," \
                                "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
employee_contragent_add_xpath = "//div[@class = 'qx-menu-border']//div[text() = 'Заказчик']"
#
archive_table_include_xpath = ".//div[@class='qooxdoo-table-cell' and (contains(text(), 'Комплексное тестирование')) " \
                              "and not(ancestor::div[contains(" \
                              "@style," \
                              "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
empty_table_xpath = "//div[@class = 'qooxdoo-table-cell' and (contains(@style," \
                    "'background:  url('resource/webclient/images/table/pencil_selected.png')'))and not(" \
                    "ancestor::div[contains(@style," \
                    "'display:none')])and not(ancestor::div[contains(@style,'display: none')]) and (text() = '')]"
#
comment_textarea_xpath = "//textarea[@id = 'commentInput' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
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
proposed_address_div_xpath = "//div[@id = 'proposed_addresses' and not(ancestor::div[contains(@style," \
                             "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]//a"
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
subject_textarea_xpath = "//textarea[@id = 'subject' and not(ancestor::div[contains(@style," \
                         "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
responsible_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Генеральный директор') and not(" \
                        "ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#
delegation_member_xpath = "//div[text()='Чёсов Роман Геннадьевич' and not(ancestor::div[contains(@style," \
                          "'display:none')])and not(" \
                          "ancestor::div[contains(@style,'display: none')])]"
#
contracts_template_xpath = "//div[@class='qx-menu-border']//div[text()='По шаблону']"
#
create_template_xpath = "//div[text()='Тест шаблон (1)']"
#
contracts_table_xpath = ".//div[contains(text(), 'Комплексное тестирование') and not(ancestor::div[contains(@style," \
                        "'display:none')])and not(ancestor::div[contains(@style,'display: none')])] "
#
customer_contragent_add_xpath = "//div[@class = 'qx-menu-border' and not(ancestor::div[contains(@style," \
                                "'display:none')])and " \
                                "not(ancestor::div[contains(@style,'display: none')])]//div[text() = 'Юр. лицо']"
#
flexbby_contragent_add_xpath = "//div[@class = 'qooxdoo-table-cell' and(text()='Флексби Солюшнс') and not(" \
                               "ancestor::div[contains(@style," \
                               "'display:none')])and not(ancestor::div[contains(@style,'display: none')])]"
#

"""BANK'S REQUISITES XPATH"""
#
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
#

""""ID"""
#
login_id = 'login'
#
password_id = 'password'
#
submit_button_id = 'enter'
#
get_data_by_INN_button_id = 'getCompanyData'
#
shadow_id = 'shadow'
#
comment_div_id = 'commentTextSystem'
#
ok_button_id = 'okb'
#
