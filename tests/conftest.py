import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver

from utils import attach


@allure.step('Load env')
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = 'https://invest.akbars.ru'
    browser.config.window_width = 1024
    browser.config.window_height = 780
    driver_options = webdriver.ChromeOptions()

    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield browser
    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)
    with allure.step('Add slog'):
        attach.add_logs(browser)
    with allure.step('Add HTML'):
        attach.add_html(browser)
    with allure.step('Add VIDEO'):
        attach.add_video(browser)

    browser.quit()