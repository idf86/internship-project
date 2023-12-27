from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

def browser_init(context, browser_name="chrome", headless=True, use_browserstack=True, scenario_name=None):
    if use_browserstack:
        bs_user = 'placeholder'
        bs_key = 'placeholder'
        url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

        bstack_options = {
            'os': 'OS X',
            'osVersion': 'Catalina',
            'browserName': browser_name,
            'browserVersion': 'latest',
            'sessionName': scenario_name
        }

        options = ChromeOptions() if browser_name == "chrome" else FirefoxOptions()
        options.set_capability('bstack:options', bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)
    else:
        if browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.headless = True
                options.add_argument("--window-size=1920,1080")  # Max headless
            context.driver = webdriver.Firefox(options=options)
        elif browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")  # Max headless
            context.driver = webdriver.Chrome(options=options)

        if not headless:
            context.driver.maximize_window()  # Maximize not headless

    context.driver.implicitly_wait(4)

def before_scenario(context, scenario):
    print('\\nStarted scenario: ', scenario.name)
    browser_init(context, headless=True, use_browserstack=True, scenario_name=scenario.name)


def before_step(context, step):
    print('\\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
