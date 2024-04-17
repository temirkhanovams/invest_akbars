import allure
from allure_commons.types import Severity

# from data import users
from pages.main_page import OpenIisPage


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'TemirkhanovaMS')
@allure.feature('Запуск тестов через Selenoid')
@allure.story('story')
@allure.description('Запуск тестов open_iis на DEMOQA через Selenoid')
def test_form_open_docs_step1():
    open_iis = OpenIisPage()
    open_iis.open()
    open_iis.open_form()
    open_iis.should_be_visible_block_only_with_step1()
    open_iis.open_pd_agreement_and_recipient_info()


def test_form_open_iis_step1_positive():
    open_iis = OpenIisPage()
    open_iis.open()
    open_iis.open_form()
    open_iis.should_be_visible_block_only_with_step1()
    open_iis.fill_contacts()
    open_iis.click_button_step1()
    open_iis.should_be_visible_block_with_step2()


def test_form_open_iis_step1_negative():
    open_iis = OpenIisPage()
    open_iis.open()
    open_iis.open_form()
    open_iis.should_be_visible_block_only_with_step1()
    open_iis.fill_contacts_all_fields_are_empty()
    open_iis.click_button_step1()
    open_iis.should_be_visible_block_only_with_step1()


def test_form_open_iis_step2_positive():
    open_iis = OpenIisPage()
    open_iis.open()
    open_iis.open_form()
    open_iis.fill_contacts()
    open_iis.click_button_step1()
    open_iis.fill_personal_data()
    open_iis.click_button_step2()
    open_iis.should_be_visible_block_with_step3()


def test_form_open_iis_step3_positive():
    open_iis = OpenIisPage()
    open_iis.open()
    open_iis.open_form()
    open_iis.fill_contacts()
    open_iis.click_button_step1()
    open_iis.fill_personal_data()
    open_iis.click_button_step2()
    open_iis.click_button_step3()
    open_iis.should_be_visible_block_with_step4()
