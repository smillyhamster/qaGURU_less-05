import os

from selene.support.shared import browser
from selene import have, be


def test_fill_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Василий')
    browser.element('#lastName').should(be.blank).type('Тёркин')
    browser.element('#userEmail').should(be.blank).type('Vasya_t@yandex.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).type('7123454321')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1973')
    browser.element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').click().type('English').press_enter().type('Computer Science').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '\images\img_for_upload.png')))
    browser.element('#currentAddress').should(be.blank).type('Some deep place in Russia')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Lucknow').press_enter()
    browser.element('#submit').press_enter()


    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'Василий Тёркин',
        'Vasya_t@yandex.ru',
        'Male',
        '7123454321',
        '11 May,1973',
        'English, Computer Science',
        'Sports, Reading',
        'img_for_upload.png',
        'Some deep place in Russia',
        'Uttar Pradesh Lucknow'
    ))
