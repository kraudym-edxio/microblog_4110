import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config

@given(u'I am on the registration page')
def step_impl(context):
    print('here')
    pass
    context.driver.get(config.register_url)

@when(u'I enter credentials {username}, {email} and {password}')
def step_impl(context, username, email, password):
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, username)
    reusable_components.send_keys_to_element(context, login_locators.EMAIL_FIELD, email)
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, password)
    reusable_components.send_keys_to_element(context, login_locators.CONFIRMPASSWORD_FIELD, password)

@then(u'click the Register Button')
def step_impl(context):
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)

@then(u'I should be redirected to the Sign In page')
def step_impl(context):
    time.sleep(5)
    assert reusable_components.get_current_url(context) == 'http://127.0.0.1:5000/auth/login'

@then(u'I should see a congratulations')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
    assert text == "Congratulations, you are now a registered user!"

@then(u'I should see an error')
def step_impl(context):
    text = ""
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="help-block"]'])
    assert len(text) is not 0