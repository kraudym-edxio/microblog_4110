import time
from misc_methods import browser_helper

def before_all(context):
    context.connected = {}

def before_tag(context, tag):
    pass

def before_scenario(context, feature):
    context.driver = browser_helper.get_browser()

def after_scenario(context, feature):
    browser_helper.reset_options()
    context.driver.quit()
