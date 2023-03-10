import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
previous_url = ''
@given(u'I am on the login page')
def step_impl(context):
    print('here 10222')
    pass
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    context.driver.get(config.base_url)
    # headlines = driver.find_elements_by_class_name("story-heading")
    # for headline in headlines:
    #     print(headline.text.strip()) 
    # context.driver = driver

    

@when(u'I enter my valid credentials')
def step_impl(context):
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, "test714")
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, "test714")

@when(u'click the login button')
def step_impl(context):
    previous_url=reusable_components.get_current_url(context)
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)


@then(u'I should be redirected to the dashboard page')
def step_impl(context):
    time.sleep(5)
    assert previous_url != reusable_components.get_current_url(context)



@then(u'I should see a welcome message with my username')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.XPATH, '//h1'])
    try:
        assert 'Hi'.lower() in text
    except:
        print('expected text not found in {}'.format(text))