import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
import random, string

@given(u'I am on the registration page')
def step_impl(context):
    context.driver.get(config.register_url)

@when(u'I enter {cred_type} registration credentials')
def step_impl(context, cred_type):
    user_name = None
    password = None
    email = None

    print('type', cred_type)
    if cred_type == 'valid':
        digits = ''.join(random.sample(string.digits, 4))
        chars = ''.join(random.sample(string.ascii_letters, 4))
        user_name = digits + chars
        password = digits + chars
        email = user_name + '@gmail.ca'
    else:
        user_name = 'test714'
        password = 'test715'
        email = 'test1@gmail.com'

    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, user_name)
    reusable_components.send_keys_to_element(context, login_locators.EMAIL_FIELD, email)
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, password)
    reusable_components.send_keys_to_element(context, login_locators.CONFIRMPASSWORD_FIELD, password)

@when(u'click the Register Button')
def step_impl(context):
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)

@then(u'I should be redirected to Sign In page')
def step_impl(context):
    time.sleep(5)
    assert 'login' in reusable_components.get_current_url(context)

@then(u'I should see a congratulations')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
    assert text == "Congratulations, you are now a registered user!"

@then(u'I should see an error message')
def step_impl(context):
    text = ""
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="help-block"]'])
    assert len(text) != 0