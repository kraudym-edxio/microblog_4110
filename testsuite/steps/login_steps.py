from misc_methods import browser_helper

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('https://google.com')
    browser_helper.get_browser()
    
    # raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I enter my valid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my valid credentials')


@when(u'click the login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click the login button')


@then(u'I should be redirected to the dashboard page')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I should be redirected to the dashboard page')


@then(u'I should see a welcome message with my username')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I should see a welcome message with my username')
