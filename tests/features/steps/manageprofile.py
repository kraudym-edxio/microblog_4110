import time
from behave import *
from misc_methods import reusable_components
from locators import profile_locators, login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
import string, random

new_name = ''
new_about_me=''

@given(u'I am on my user home page')
def step_impl(context):
    context.driver.get(config.home_page)
    reusable_components.send_keys_to_element(context, login_locators.USERNAME_FIELD, config.user_name)
    reusable_components.send_keys_to_element(context, login_locators.PASSWORD_FIELD, config.user_password)
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)

@given(u'I click Profile')
def step_impl(context):
    time.sleep(2)
    reusable_components.click_on_element(context, [By.XPATH, '//a[text()="Profile"]'])

@given(u'I click Edit Your Profile')
def step_impl(context):
    print("On profile page going to edit profile")
    previous_url = reusable_components.get_current_url(context)
    x = context.driver.find_element_by_link_text('Edit your profile')
    x.click()
    time.sleep(2)

@when(u'I enter new profile information')
def step_impl(context):
    new_about_me = ''.join(random.sample(string.digits, 10))
    new_name = config.user_name
    reusable_components.send_keys_to_element(context, profile_locators.USERNAME_FIELD, new_name)
    reusable_components.send_keys_to_element(context, profile_locators.ABOUTME_FIELD, new_about_me)

@when(u'I click Submit')
def step_impl(context):
    reusable_components.click_on_element(context, profile_locators.SUBMIT_BTN)
    time.sleep(2)

@then(u'I should see a confirmation message at the top')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
    assert text == "Your changes have been saved."

@then(u'When I return to my profile')
def step_impl(context):
    w = context.driver.find_element_by_link_text('Profile')
    w.click()

@then(u'I should see my profile information changed')
def step_impl(context):
    time.sleep(2)
    text = reusable_components.get_text_of_an_element(context, [By.XPATH, '//h1'])
    try:
        assert new_name.lower() in text.lower()
    except:
        print('expected name not found in {}'.format(text))

    assert new_about_me in context.driver.page_source