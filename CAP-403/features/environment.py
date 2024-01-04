from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

def browser_init(context, browser_name="firefox", headless=False, mobile_emulation=False):
    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
            options.add_argument("--window-size=1920,1080")  # Max headless
        context.driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        if mobile_emulation:
            mobile_emulation_config = {"deviceName": "iPhone XR"}
            options.add_experimental_option("mobileEmulation", mobile_emulation_config)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")  # Max headless
        context.driver = webdriver.Chrome(options=options)

    if not headless:
        context.driver.maximize_window()

    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\\nStarted scenario: ', scenario.name)
    browser_init(context, browser_name="chrome", headless=True, mobile_emulation=True)


def before_step(context, step):
    print('\\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
