from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('Open the main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    time.sleep(4)


@when('Log in to the page')
def enter_credentials(context):
    email_field = context.driver.find_element(By.ID, "email-2")
    email_field.send_keys('fluffyandspeedy@gmail.com')
    password_field = context.driver.find_element(By.ID, "field")
    password_field.send_keys('MeowMeowMeow123')
    login_button = context.driver.find_element(By.XPATH, '//a[@wized="loginButton"]')
    login_button.click()
    time.sleep(3)


@when('Change the language of the page to Russian. The option will be “Русский” is the list of the languages')
def change_language(context):
    language_switcher = context.driver.find_element(By.CSS_SELECTOR, ".en")
    language_switcher.click()
    russian_language_option = context.driver.find_element(By.ID, "weglot-language-ru")
    russian_language_option.click()
    time.sleep(2)



@then('Verify the language has changed')
def verify_language(context):
    assert "Русский" in context.driver.page_source

