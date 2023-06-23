from selene import browser, be, have
import os

def test_registration(brouser_settings):
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('Valery')
    browser.element('#lastName').should(be.blank).type('Maksimov')
    browser.element('#userEmail').should(be.blank).type('valery@mail.com')
    browser.element("[value='Male']+label").should(be.clickable).click()
    browser.element('#userNumber').should(be.blank).type('+79993213232')

    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element("[value='4']").should(be.clickable).click()
    browser.element("[value='1989']").should(be.clickable).click()
    browser.element("[value='1989']").should(be.clickable).click()
    browser.element("[aria-label='Choose Monday, May 1st, 1989']").should(be.clickable).click()

    browser.element('#subjectsInput').should(be.blank).type('Eng').press_enter()
    browser.element('[for=hobbies-checkbox-1][class="custom-control-label"]').should(be.clickable).click()
    browser.element('#uploadPicture').set_value(os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'resources/image.jpg')))
    browser.element('#currentAddress').should(be.blank).type('SPB')
