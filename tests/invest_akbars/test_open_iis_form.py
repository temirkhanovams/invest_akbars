import allure
from allure_commons.types import Severity
from data import users
from pages.open_iis_page import OpenIisPage

user_test = users.user_test
user_empty = users.user_empty


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'TemirkhanovaMS')
@allure.feature('Запуск тестов через Selenoid')
@allure.story('story')
@allure.description('Запуск тестов open_iis через Selenoid')
def test_form_open_docs_step1():
    open_iis = OpenIisPage()
    open_iis.open_browser()
    open_iis.open_form()
    open_iis.should_be_visible_block_with_step1()
    open_iis.open_docs_in_step1()


def test_form_open_iis_step1_positive():
    open_iis = OpenIisPage()
    open_iis.open_browser()
    open_iis.open_form()
    open_iis.should_be_visible_block_with_step1()
    open_iis.fill_contacts(user_test)
    open_iis.click_button_step1()
    open_iis.should_be_visible_block_with_step2()


def test_form_open_iis_step1_negative():
    open_iis = OpenIisPage()
    open_iis.open_browser()
    open_iis.open_form()
    open_iis.should_be_visible_block_with_step1()
    open_iis.fill_contacts_all_empty(user_empty)
    open_iis.click_button_step1()
    open_iis.should_be_visible_block_with_step1()


def test_form_open_iis_step2_positive():
    open_iis = OpenIisPage()
    open_iis.open_browser()
    open_iis.open_form()
    open_iis.fill_contacts(user_test)
    open_iis.click_button_step1()
    open_iis.fill_personal_data(user_test)
    open_iis.click_button_step2()
    open_iis.should_be_visible_block_with_step3()


def test_form_open_iis_step3_positive():
    open_iis = OpenIisPage()
    open_iis.open_browser()
    open_iis.open_form()
    open_iis.fill_contacts(user_test)
    open_iis.click_button_step1()
    open_iis.fill_personal_data(user_test)
    open_iis.click_button_step2()
    open_iis.click_button_step3()
    open_iis.should_be_visible_block_with_step4()
