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
    email_field.send_keys('placeholder email')

    password_field = context.driver.find_element(By.ID, "field")
    password_field.send_keys('placeholder password')
    login_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
    login_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'My menu')]"))
    )

@when('Change the language of the page to Russian. The option will be “RU” is the list of the languages')
def change_language(context):
    profile_finder = context.driver.find_element(By.CSS_SELECTOR, ".menu-img-agent-listing")
    profile_finder.click()
    language_switcher = WebDriverWait(context.driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wg-dd-1-togle-3.w-dropdown-toggle"))
    )
    language_switcher.click()
    russian_language_option = WebDriverWait(context.driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wg-dropdown-1-link-2.w-dropdown-link"))
    )
    russian_language_option.click()

@then('Verify the language has changed')
def verify_language(context):
    language_element = context.driver.find_element(By.ID, "w-dropdown-toggle-0")
    language_text = language_element.find_element(By.TAG_NAME, "div").text
    assert language_text == "RU", f"Expected language to be 'RU', but found '{language_text}'"



