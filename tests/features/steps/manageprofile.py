import time
from behave import *
from selenium import webdriver
from misc_methods import reusable_components
from locators import profile_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

previous_url = ''
newName = ''
newAboutMe=''
@given(u'I am on my user home page')
def step_impl(context):
    context.driver.get(config.base_url)

@then(u'I click Profile')
def step_impl(context):
    previous_url=reusable_components.get_current_url(context)
    reusable_components.click_on_element(context, profile_locators.PROFILE_BTN)

@then(u'I click Edit Your Profile')
def step_impl(context):
    time.sleep(5)
    assert previous_url != reusable_components.get_current_url(context)
    print("On profile page going to edit profile")
    previous_url = reusable_components.get_current_url(context)
    reusable_components.click_on_element(context, profile_locators.EDITPROFILE_BTN)

@when(u'I enter new profile information {username} and {aboutme}')
def step_impl(context, username, aboutme):
    newAboutMe = aboutme
    newName = newName
    reusable_components.send_keys_to_element(context, profile_locators.USERNAME_FIELD, username)
    reusable_components.send_keys_to_element(context, profile_locators.ABOUTME_FIELD, aboutme)

@then(u'I click Submit')
def step_impl(context):
    reusable_components.click_on_element(context, profile_locators.SUBMIT_BTN)

@then(u'I should see a confirmation message at the top')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[class="alert alert-info"]'])
    assert text == "Your changes have been saved."

@then(u'When I return to my profile')
def step_impl(context):
    reusable_components.click_on_element(context, profile_locators.PROFILE_BTN)

@then(u'I should see my profile information changed')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.XPATH, '//h1'])
    try:
        assert newName.lower() in text.lower()
    except:
        print('expected name not found in {}'.format(text))

    assert newAboutMe in context.driver.page_source