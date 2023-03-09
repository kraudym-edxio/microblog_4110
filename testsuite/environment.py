import os

from misc_methods import browser_helper
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

def before_all(context):
    cleanstart = os.environ.get("CLEANUP")
    if cleanstart == "true":
        browser_helper.cleanup_directory()

    context.notification_count = {}



def before_tag(context, tag):
    pass

def before_feature(context, feature):
    context.driver = browser_helper.get_browser()
    # pass

# def after_feature(context, feature):
#     browser_helper.reset_options()
#     context.driver.quit()


