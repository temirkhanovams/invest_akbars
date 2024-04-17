import allure
from selene import browser, be, by, command, have

# from data.users import User
from qa_guru_project_homework_15 import resource


class OpenIisPage:
    def __init__(self):
        self.open_form_selector = browser.all("[name='openAccountSteps']").element_by(have.exact_text('Начать инвестировать'))
        self.last_name_selector = browser.element("#openAccountStepsSnackbar [icon='1'] [name=lastName]")
        self.first_name_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=firstName]")
        self.middle_name_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=middleName]")
        self.phone_number_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=phoneNumber]")
        self.email_selector = browser.element("#openAccountStepsSnackbar  [icon='1'] [name=email]")
        self.agreement_selector = browser.all('#openAccountStepsSnackbar span.MuiButton-label').element_by(have.exact_text('согласие на обработку персональных данных'))
        self.recipient_info_selector = browser.all('#openAccountStepsSnackbar span.MuiButton-label').element_by(have.exact_text('Информация для получателей финансовых услуг'))

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
        self.passport_number_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=passportNumber]")
        self.passport_issue_date_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=passportIssueDate]")
        self.passport_issuer_code_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=passportIssuerCode]")
        self.passport_issuer_title_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=passportIssuerTitle]")
        self.gender_male_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [value=male]")
        self.gender_female_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [value=female]")
        self.registration_address_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=registrationAddress]")
        self.data_option_address_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [role=listbox] [data-option-index='1']")
        self.phone_number_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=phoneNumber]")
        self.email_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=email]")
        self.inn_selector_step2 = browser.element("#openAccountStepsSnackbar [icon='2'] [name=inn]")


        # self.menu = browser.element('')
        # self.first_name_selector = browser.element("#0.04464266225558178")
        # self.first_name_selector = browser.all("[name='lastName']").element_by(have.exact_text("Фамилия*"))
        # self.last_name_selector = browser.element("[name='given-name']")
        # self.middle_name_selector = browser.element("[name='middleName']")
        # self.email_selector = browser.element('#userEmail')
        # self.gender_selector = browser.all('[name=gender]')
        # self.phone_selector = browser.element('#userNumber')
        # self.year_selector = browser.element('.react-datepicker__year-select')
        # self.month_selector = browser.element('.react-datepicker__month-select')
        # self.day_selector = browser.element('.react-datepicker__month')
        # self.subjects_selector = browser.element('#subjectsInput')
        # self.image_selector = browser.element('#uploadPicture')
        # self.address_selector = browser.element('#currentAddress')
        # self.state_selector = browser.element('#state')
        # self.city_selector = browser.element('#city')
        # self.state_city_value_selector = browser.all('[id^=react-select][id*=option]')
        # self.submit_selector = browser.element('#submit')
        # self.result_selector = browser.element('.table').all('tr td:nth-child(2)')

    @allure.step("Открываем главную страницу сайта https://invest.akbars.ru'")
    @allure.link('https://invest.akbars.ru', name='Testing')
    def open(self):
        return browser.open('/')

    @allure.step("Нажимаем на кнопку Открыть счёт на главной")
    def open_form(self):
        self.open_form_selector.click()

    @allure.step('Проверяем успешность отображения блока с шагом 1')
    def should_be_visible_block_only_with_step1(self):
        self.block_with_step1_selector.should(be.visible)
        self.block_with_step2_selector.should(be.not_.visible)
        self.block_with_step3_selector.should(be.not_.visible)
        self.block_with_step4_selector.should(be.not_.visible)

    @allure.step('Заполняем шаг 1 - Контактные данные')
    def fill_contacts(self):
        with allure.step("Заполняем Фамилию"):
            self.last_name_selector.should(be.blank).type('Тестова')
        with allure.step("Заполняем имя"):
            self.first_name_selector.should(be.blank).type('Тест')
        with allure.step("Заполняем Отчество"):
            self.middle_name_selector.should(be.blank).type('Тестовна')
        with allure.step("Вводим номер телефона"):
            self.phone_number_selector.should(be.blank).type('79999999999')
        with allure.step("Заполняем email"):
            self.email_selector.should(be.blank).type('invest.akbars.qa@gmail.com')

    @allure.step('Заполняем шаг 1 - Оставляем все поля пустыми')
    def fill_contacts_all_fields_are_empty(self):
        with allure.step("Фамилия - пусто"):
            self.first_name_selector.should(be.blank).type('')
        with allure.step("Имя - пусто"):
            self.last_name_selector.should(be.blank).type('')
        with allure.step("Отчество - пусто"):
            self.middle_name_selector.should(be.blank).type('')
        with allure.step("Номер телефона - пусто"):
            self.phone_number_selector.should(be.blank).type('')
        with allure.step("email - пусто"):
            self.email_selector.should(be.blank).type('')
    @allure.step('Открываем ссылки на документы в шаге 1')
    def open_pd_agreement_and_recipient_info(self):
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
        self.block_with_step1_selector.should(be.not_.visible)
        self.block_with_step2_selector.should(be.visible)

    @allure.step('Заполняем шаг 2 - Личные данные')
    def fill_personal_data(self):
        # with allure.step("Вводим фамилию"):
        #     self.last_name_selector_step2.should(be.blank).type('Тестова')
        # with allure.step("Вводим имя"):
        #     self.first_name_selector_step2.should(be.blank).type('Тест')
        # with allure.step("Вводим отчество"):
        #     self.middle_name_selector_step2.should(be.blank).type('Тестовна')
        with allure.step("Вводим дату рождения"):
            self.birth_date_selector_step2.should(be.blank).type('01 01 2000')
        with allure.step("Вводим место рождения"):
            self.birth_place_selector_step2.should(be.blank).type('г.Казань')
        with allure.step("Вводим Серию и Номер паспорта"):
            self.passport_number_selector_step2.should(be.blank).type('0000 000000')
        with allure.step("Вводим дату выдачи паспорта"):
            self.passport_issue_date_selector_step2.should(be.blank).type('01.01.2014')
        with allure.step("Вводим Код подразделения"):
            self.passport_issuer_code_selector_step2.should(be.blank).type('000-000')
        with allure.step("Вводим Кем выдан"):
            self.passport_issuer_title_selector_step2.should(be.blank).type('МВД России по РТ')
        with allure.step("Выбираем Пол"):
            self.gender_female_selector_step2.click()
        with allure.step("Вводим адрес регистрации"):
            self.registration_address_selector_step2.should(be.blank).type('Казань Декабристов 1a')
            self.data_option_address_selector_step2.click()
        # with allure.step("Нажимаем на галочку Фактический адрес..."):
        #     self.last_name_selector.should(be.blank).type('Тест')
        # with allure.step("Вводим фактический адрес проживания"):
        #     self.last_name_selector.should(be.blank).type('Тест')
        # with allure.step("Вводим номер телефона"):
        #     self.phone_number_selector_step2.should(be.blank).type('79999999999')
        # with allure.step("Заполняем email"):
        #     self.email_selector_step2.should(be.blank).type('invest.akbars.qa@gmail.com')
        with allure.step("Вводим ИНН"):
            self.inn_selector_step2.should(be.blank).type('000000000184')

    @allure.step('Нажимаем на кнопку Продолжить - в шаге 2')
    def click_button_step2(self):
        with allure.step('Кнопка Продолжить в шаге 2'):
            self.button_step2_selector().click()

    def should_be_visible_block_with_step3(self):
        self.block_with_step1_selector.should(be.not_.visible)
        self.block_with_step2_selector.should(be.not_.visible)
        self.block_with_step3_selector.should(be.visible)

    @allure.step('Нажимаем на кнопку Продолжить - в шаге 3')
    def click_button_step3(self):
        with allure.step('Кнопка Продолжить в шаге 3'):
            self.button_step3_selector.click()

    def should_be_visible_block_with_step4(self):
        self.block_with_step1_selector.should(be.not_.visible)
        self.block_with_step2_selector.should(be.not_.visible)
        self.block_with_step3_selector.should(be.not_.visible)
        self.block_with_step4_selector.should(be.visible)


    # @allure.step("Заполняем Фамилию")
    # def fill_first_name(self):
    #     self.first_name_selector.should(be.blank).type('Тестова')
    # @allure.step("Заполняем имя")
    # def fill_last_name(self):
    #     self.last_name_selector.should(be.blank).type('Тест')
    # @allure.step("Заполняем Отчество")
    # def fill_middle_name(self):
    #     self.middle_name_selector.should(be.blank).type('Тестовна')
    # @allure.step("Вводим номер телефона")
    # def fill_phone_number(self):
    #     self.phone_number_selector.should(be.blank).type('79999999999')
    # @allure.step("Заполняем email")
    # def fill_email(self):
    #     self.email_selector.should(be.blank).type('invest.akbars.qa@gmail.com')

    # @allure.step("Заполняем email")
    # def fill_email(self, value):
    #     self.email_selector.should(be.blank).type(value)
    #
    # @allure.step("Выбираем пол")
    # def fill_gender(self, value):
    #     self.gender_selector.element_by(have.value(value)).element('..').click()
    #
    # @allure.step("Вводим номер тел.")
    # def fill_phone(self, value):
    #     self.phone_selector.should(be.blank).type(value)
    #
    # @allure.step("Выбираем год, число, месяц рождения")
    # def fill_birthday(self, year, month, day):
    #     browser.element('#dateOfBirthInput').click()
    #     self.year_selector.click()
    #     browser.element(by.text(year)).click()
    #     self.month_selector.click()
    #     browser.element(by.text(month)).click()
    #     self.day_selector.click()
    #     browser.element(by.text(day)).click()
    #
    # @allure.step("Выбираем Subjects")
    # def fill_subjects(self, value):
    #     self.subjects_selector.should(be.blank).type(value).press_enter()
    #
    # @allure.step("Выбираем хобби")
    # def fill_hobbies(self, param):
    #     browser.element('#hobbies-checkbox-2').perform(command.js.scroll_into_view)
    #     browser.all('.custom-checkbox').element_by(have.exact_text(param)).click()
    #
    # @allure.step("Загружаем фото")
    # def fill_image(self, value):
    #     self.image_selector.send_keys(resource.path(value))
    #
    # @allure.step("Вводим адрес")
    # def fill_address(self, value):
    #     self.address_selector.click().type(value)
    #
    # @allure.step("Выбираем штат и город")
    # def fill_state(self, state, city):
    #     self.state_selector.click()
    #     self.state_city_value_selector.element_by(have.exact_text(state)).click()
    #     self.city_selector.click()
    #     self.state_city_value_selector.element_by(have.exact_text(city)).click()
    #
    # @allure.step("Отправляем форму")
    # def submit(self):
    #     self.submit_selector.perform(command.js.click)
    #
    # def fill(self, admin: User):
    #     self.fill_full_name(admin.first_name, admin.last_name)
    #     self.fill_email(admin.email)
    #     self.fill_gender(admin.gender)
    #     self.fill_phone(admin.phone)
    #     self.fill_birthday(admin.year, admin.month, admin.day)
    #     self.fill_subjects(admin.subjects)
    #     self.fill_hobbies(admin.hobbies)
    #     self.fill_image(admin.file)
    #     self.fill_address(admin.address)
    #     self.fill_state(admin.state, admin.city)
    #
    # @allure.step("Проверяем инфо о студенте с введённой им значениями")
    # def should_registered_user_with(self, admin: User):
    #     self.result_selector.should(
    #         have.texts(f'{admin.first_name} {admin.last_name}', {admin.email}, {admin.gender}, {admin.phone},
    #                    {admin.birthday}, {admin.subjects}, {admin.hobbies}, {admin.file}, {admin.address},
    #                    f'{admin.state} {admin.city}'))
