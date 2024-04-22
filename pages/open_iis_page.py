import allure
from selene import browser, be, have
from data.users import User


class OpenIisPage:
    def __init__(self):
        self.open_form_selector = browser.all("[name='openAccountSteps']").element_by(
            have.exact_text('Начать инвестировать'))
        self.last_name_selector = browser.element("#openAccountStepsSnackbar [icon='1'] [name=lastName]")
        self.first_name_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=firstName]")
        self.middle_name_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=middleName]")
        self.phone_number_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=phoneNumber]")
        self.email_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=email]")
        self.agreement_selector = browser.all('#openAccountStepsSnackbar span.MuiButton-label').element_by(
            have.exact_text('согласие на обработку персональных данных'))
        self.recipient_info_selector = browser.all('#openAccountStepsSnackbar span.MuiButton-label').element_by(
            have.exact_text('Информация для получателей финансовых услуг'))

        self.button_step1_selector = browser.element("#openAccountStepsSnackbar [icon='1'] [aria-label=Продолжить]")
        self.button_step2_selector = browser.element("#openAccountStepsSnackbar [icon='2'] [aria-label=Продолжить]")
        self.button_step3_selector = browser.element("#openAccountStepsSnackbar [icon='3'] [aria-label=Продолжить]")
        self.button_step4_selector = browser.element("#openAccountStepsSnackbar [icon='4'] [aria-label=Продолжить]")

        self.block_with_step1_selector = browser.element('#openAccountStepsSnackbar [icon="1"]')
        self.block_with_step2_selector = browser.element('#openAccountStepsSnackbar [icon="2"]')
        self.block_with_step3_selector = browser.element('#openAccountStepsSnackbar [icon="3"]')
        self.block_with_step4_selector = browser.element('#openAccountStepsSnackbar [icon="4"]')

        self.last_name_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=lastName]")
        self.first_name_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=firstName]")
        self.middle_name_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=middleName]")
        self.birth_date_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=birthDate]")
        self.birth_place_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=birthPlace]")
        self.passport_number_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [name=passportNumber]")
        self.passport_issue_date_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [name=passportIssueDate]")
        self.passport_issuer_code_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [name=passportIssuerCode]")
        self.passport_issuer_title_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [name=passportIssuerTitle]")
        self.gender_selector_step2 = browser.all("#openAccountStepsSnackbar [icon='2'] [type=radio]")
        self.registration_address_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [name=registrationAddress]")
        self.data_option_address_selector_step2 = browser.element(
            "#openAccountStepsSnackbar [icon='2'] [role=listbox]:nth-child(1)")
        self.phone_number_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=phoneNumber]")
        self.email_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=email]")
        self.inn_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=inn]")

    @allure.step("Открываем главную страницу сайта ")
    @allure.link('https://invest.akbars.ru', name='Testing')
    def open_browser(self):
        return browser.open_browser('/')

    @allure.step("Нажимаем на кнопку Открыть счёт на главной")
    def open_form(self):
        self.open_form_selector.click()

    @allure.step('Проверяем успешность отображения блока с шагом 1')
    def should_be_visible_block_with_step1(self):
        self.block_with_step1_selector.should(be.visible)

    @allure.step('Заполняем шаг 1 - Контактные данные')
    def fill_contacts(self, user_test: User):
        with allure.step("Заполняем Фамилию"):
            self.last_name_selector.should(be.blank).type(user_test.last_name)
        with allure.step("Заполняем имя"):
            self.first_name_selector.should(be.blank).type(user_test.first_name)
        with allure.step("Заполняем Отчество"):
            self.middle_name_selector.should(be.blank).type(user_test.middle_name)
        with allure.step("Вводим номер телефона"):
            self.phone_number_selector.should(be.blank).type(user_test.phone_number)
        with allure.step("Заполняем email"):
            self.email_selector.should(be.blank).type(user_test.email)

    @allure.step('Заполняем шаг 1 - Оставляем все поля пустыми')
    def fill_contacts_all_empty(self, user_empty: User):
        with allure.step("Фамилия - пусто"):
            self.last_name_selector.should(be.blank).type(user_empty.last_name)
        with allure.step("Имя - пусто"):
            self.first_name_selector.should(be.blank).type(user_empty.first_name)
        with allure.step("Отчество - пусто"):
            self.middle_name_selector.should(be.blank).type(user_empty.middle_name)
        with allure.step("Номер телефона - пусто"):
            self.phone_number_selector.should(be.blank).type(user_empty.phone_number)
        with allure.step("email - пусто"):
            self.email_selector.should(be.blank).type(user_empty.email)

    @allure.step('Открываем ссылки на документы в шаге 1')
    def open_docs_in_step1(self):
        with allure.step('Открываем ссылку на документ - Согласие на обработку ПД'):
            self.agreement_selector.click()
        with allure.step('Открываем ссылку на документ - Информация для получателей финансовых услуг'):
            self.recipient_info_selector.click()

    @allure.step('Нажимаем на кнопку Продолжить - в шаге 1')
    def click_button_step1(self):
        with allure.step('Кнопка Продолжить'):
            self.button_step1_selector().click()

    @allure.step('Проверяем успешность перехода к шагу 2')
    def should_be_visible_block_with_step2(self):
        self.block_with_step2_selector.should(be.visible)

    @allure.step('Заполняем шаг 2 - Личные данные')
    def fill_personal_data(self, test_user: User):
        with allure.step("Вводим дату рождения"):
            self.birth_date_selector_step2.should(be.blank).type(test_user.birth_date)
        with allure.step("Вводим место рождения"):
            self.birth_place_selector_step2.should(be.blank).type(test_user.birth_place)
        with allure.step("Вводим Серию и Номер паспорта"):
            self.passport_number_selector_step2.should(be.blank).type(test_user.passport_number)
        with allure.step("Вводим дату выдачи паспорта"):
            self.passport_issue_date_selector_step2.should(be.blank).type(test_user.passport_issue_date)
        with allure.step("Вводим Код подразделения"):
            self.passport_issuer_code_selector_step2.should(be.blank).type(test_user.passport_issuer_code)
        with allure.step("Вводим Кем выдан"):
            self.passport_issuer_title_selector_step2.should(be.blank).type(test_user.passport_issuer_title)
        with allure.step("Выбираем Пол"):
            self.gender_selector_step2.element_by(have.value(test_user.gender)).click()
        with allure.step("Вводим адрес регистрации"):
            self.registration_address_selector_step2.should(be.blank).type(test_user.registration_address)
            self.data_option_address_selector_step2.click()
        with allure.step("Вводим ИНН"):
            self.inn_selector_step2.should(be.blank).type(test_user.inn)

    @allure.step('Нажимаем на кнопку Продолжить - в шаге 2')
    def click_button_step2(self):
        with allure.step('Кнопка Продолжить в шаге 2'):
            self.button_step2_selector().click()

    def should_be_visible_block_with_step3(self):
        self.block_with_step3_selector.with_(timeout=7).should(be.visible)

    @allure.step('Нажимаем на кнопку Продолжить - в шаге 3')
    def click_button_step3(self):
        with allure.step('Кнопка Продолжить в шаге 3'):
            self.button_step3_selector.click()

    def should_be_visible_block_with_step4(self):
        self.block_with_step4_selector.should(be.visible)
