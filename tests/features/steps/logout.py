import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
previous_url = ''
@given(u'I am in the login page')
def step_impl(context):
    context.driver.get(config.base_url)
    

@when(u'I click the login button')
def step_impl(context):
    
    reusable_components.click_on_element(context, login_locators.SIGN_IN_BTN)


@then(u'I should be redirected to the main page')
def step_impl(context):
    time.sleep(5)
   

@then(u'when I click the logout button')
def step_impl(context):
    previous_url=reusable_components.get_current_url(context)
    #reusable_components.click_on_element(context, login_locators.LOGOUT_BTN)
    l = context.driver.find_element_by_partial_link_text('Logou')
    l.click()

@then(u'I should be redirected to the Sign In page')
def step_impl(context):
    assert previous_url != reusable_components.get_current_url(context)