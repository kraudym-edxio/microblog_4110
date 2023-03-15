import time
from selenium import webdriver
from misc_methods import reusable_components
from locators import login_locators 
from selenium.webdriver.common.by import By
from misc_methods import config
import random
import string
from selenium.common.exceptions import TimeoutException

status_text = None
prev_fav_count = None
new_fav_count = None


@given(u'I have posted a status update')
def step_impl(context):
    digits = ''.join(random.sample(string.digits, 8))
    chars = ''.join(random.sample(string.ascii_letters, 15))
    status_text = digits + chars
    reusable_components.send_key(context, [By.CSS_SELECTOR, '[id="post"]'], status_text) 
    reusable_components.click_on_element(context, [By.CSS_SELECTOR, '[id="submit"]'])
    time.sleep(2)
    assert reusable_components.get_element(context.driver, [By.XPATH, '//span[text()="{}"]'.format(status_text)]) is not None


@given(u'I create my status updates')
def step_impl(context):
    text = reusable_components.get_text_of_an_element(context, [By.XPATH, '//div/h1'])
    assert 'Hi,' in text


@when(u'I click on the delete button next to the status update I want to delete')
def step_impl(context):
    reusable_components.click_on_element(context, [By.XPATH, '//button[text()="Delete"]'])


@then(u'the status update should be permanently removed from my profile')
def step_impl(context):
    time.sleep(2)
    notFound = None
    try:
        elem = reusable_components.get_element(context.driver, [By.XPATH, '//span[text()="{}"]'.format(status_text)])
        not_found = False
    except:
        not_found = True

    assert not_found



@given(u'I go to explore')
def step_impl(context):
    time.sleep(1)
    reusable_components.click_on_element(context, [By.XPATH, '//a[text()="Explore"]'])
    

@when(u'I click on the fav button next to the status update I want to delete')
def step_impl(context):
    prev_fav_count = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[id="likecount"]'])
    reusable_components.click_on_element(context, [By.CSS_SELECTOR, '[id="likecount"]'])

@then(u'the fav counter next to the react emoji should be updated')
def step_impl(context):
    new_fav_count = reusable_components.get_text_of_an_element(context, [By.CSS_SELECTOR, '[id="likecount"]'])

    print('prev_fav_count',prev_fav_count)
    print('new_fav_count',new_fav_count)
    assert prev_fav_count != new_fav_count