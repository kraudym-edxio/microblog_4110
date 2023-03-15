import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import home_locators, profile_locators, login_locators
from selenium.webdriver.common.by import By
from misc_methods import config

@given(u'I am on the main page')
def step_impl(context):
    context.driver.get(config.base_url)
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, "test502")
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, "@Deathby1411")
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)
    time.sleep(2)

@when(u'I enter the {text} for my post')
def step_impl(context, text):
     reusable_components.send_keys_to_element(context, home_locators.POST_FIELD, text)

@when(u'click submit button')
def step_impl(context):
     time.sleep(2)
     reusable_components.click_on_element(context, home_locators.SUBMIT_BTN)

@then(u'I should be seeing a message saying my post is live')
def step_impl(context):
     text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
     assert text == "Your post is now live!"

@then(u'when I click the explore')
def step_impl(context):
     w = context.driver.find_element_by_link_text('Explore')
     w.click()

@then(u'my {text} should appear in the list')
def step_impl(context, text):
     time.sleep(2)
     assert text in context.driver.page_source