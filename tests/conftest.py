import pytest
from selene import browser


@pytest.fixture()
def browser_settings():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
