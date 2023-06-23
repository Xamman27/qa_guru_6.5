import pytest
from selene import browser


@pytest.fixture()
def brouser_settings():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'