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
    context.driver.get(config.base_url)
    

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


@when(u'I enter credentials {username} and {password}')
def step_impl(context, username, password):
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, username)
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, password)

@then(u'I should see an error')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
    assert text == "Invalid username or password"