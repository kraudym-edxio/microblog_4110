import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators, home_locators
from selenium.webdriver.common.by import By
from misc_methods import config

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get(config.base_url)
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, "test714")
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, "test714")
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)
    time.sleep(2)

@when(u'I enter {text} for my post')
def step_impl(context, text):
     reusable_components.send_keys_to_element(context, home_locators.POST_FIELD, text)

@when(u'click the submit button')
def step_impl(context):
     reusable_components.click_on_element(context, home_locators.SUBMIT_BTN)

@then(u'I should be see a message saying my post is live')
def step_impl(context):
     time.sleep(5)
     text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
     assert text == "Your post is now live!"
