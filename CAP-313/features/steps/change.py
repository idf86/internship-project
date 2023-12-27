from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Sign in or create new account')]"))
    )

@when('Log in to the page')
def enter_credentials(context):
    users_counter = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[wized='usersCounter']"))
    )
    while users_counter.text == "-" or users_counter.text.isnumeric() == False:
        users_counter = context.driver.find_element(By.CSS_SELECTOR, "div[wized='usersCounter']")
    email_field = context.driver.find_element(By.ID, "email-2")
    email_field.send_keys('placeholder')

    password_field = context.driver.find_element(By.ID, "field")
    password_field.send_keys('placeholder')
    login_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
    login_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'My menu')]"))
    )

@when('Change the language of the page to Russian. The option will be “Русский” is the list of the languages')
def change_language(context):
    language_switcher = context.driver.find_element(By.CSS_SELECTOR, ".en")
    language_switcher.click()
    russian_language_option = context.driver.find_element(By.ID, "weglot-language-ru")
    russian_language_option.click()
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#weglot-language-ru"), "Русский")
    )

@then('Verify the language has changed')
def verify_language(context):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".main-menu-text"), "Редактировать профиль")
    )
    profile_text_element = context.driver.find_element(By.CSS_SELECTOR, ".main-menu-text")
    assert profile_text_element.text == "Редактировать профиль"
