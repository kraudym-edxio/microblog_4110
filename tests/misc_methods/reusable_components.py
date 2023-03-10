import time
from random import randrange

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotInteractableException

app = 'hubspot'

def get_element(driver, locator, timeout=10):
    if app in locator:
        try:
            return (
                WebDriverWait(driver, timeout)
                .until(
                    EC.visibility_of_element_located(
                        (locator[app][0], locator[app][1])
                    )
                )
            )
        except ElementNotInteractableException:
              print("Element {} not interactable", locator)
        except NoSuchElementException:
              print("Error finding element", locator)
    else:
        return (
            WebDriverWait(driver, timeout)
            .until(
                EC.visibility_of_element_located(
                    (
                        locator[0], locator[1]
                    )
                )
            )
        )


def get_elements(driver, locator, timeout=10):
    if app in locator:
        return (
            WebDriverWait(driver, timeout)
            .until(
                EC.presence_of_all_elements_located(
                    (locator[app][0], locator[app][1])
                )
            )
        )
    else:
        return (
            WebDriverWait(driver, timeout)
            .until(
                EC.presence_of_all_elements_located(
                    (
                        locator[0], locator[1]
                    )
                )
            )
        )


def get_element_without_wait(driver, locator, timeout=10):
    if app in locator:
        return (
            driver.find_element(locator[app][0], locator[app][1])
        )
    else:
        return (
            driver.find_element(locator[0], locator[1])
        )


def get_locator(driver, locator, timeout=10):
    if app in locator:
        return (
            locator[app][0], locator[app][1]
        )
    else:
        return (
            locator[0], locator[1]
        )


def wait_for_element_visibility(self, locator, timeout=10):
    return (
        WebDriverWait(self.driver, timeout)
        .until(
            EC.visibility_of_element_located(
                get_locator(self.driver, locator, timeout)
            )
        )
    )


def wait_for_element_clickable(self, locator, timeout=10):
    return (
        WebDriverWait(self.driver, timeout)
        .until(
            EC.element_to_be_clickable(
                get_element(self.driver, locator, timeout)
            )
        )
    )


def get_element_attribute(self, locator, attribute, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    return (
        element.get_attribute(attribute)
    )


def verify_element_is_present(self, locator, timeout=10):
    try:
        get_element_without_wait(self.driver, locator, timeout)
    except NoSuchElementException:
        return False
    return True
    

def verify_all_elements_are_present(self, locator, timeout=10):
    return WebDriverWait(self.driver, timeout).until(
        EC.presence_of_all_elements_located(
            locator[app][0], locator[app][1]
        )
    ).is_displayed()


def verify_element_with_specific_text_is_present(self, text, timeout=10):
    locator = '//*[contains(text(),"{placeholder}")]'.replace("{placeholder}", text)
    return WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located(
            (By.XPATH, locator)
        )
    ).is_displayed()


def click_on_element(self, locator, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    element.click()


def from_list_click_on_random_element(self, locator, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    time.sleep(1)
    elements[randrange(len(elements))].click()

def from_list_click_on_element_on_specific_index(self, locator, index, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    elements[index].click()

def from_list_click_on_first_element(self, locator, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    elements[0].click()

def from_list_get_elements_size(self, locator, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    return len(elements)

def click_on_element_js(self, locator, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    self.driver.execute_script("arguments[0].click();", element)

def from_list_click_on_element_js(self, locator, timeout=10):
    self.driver.execute_script("arguments[0].click();", get_elements(self.driver, locator, timeout)[0])

def from_list_click_on_valid_element_js(self, locator, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    for element in elements:
        try:
            self.driver.execute_script("arguments[0].click();", element)
        except:
            pass

def from_list_click_on_valid_element(self, locator, timeout=10):
    elements = get_elements(self.driver, locator, timeout)
    for element in elements:
        try:
            element.click()
        except:
            pass


def element_is_displayed(self, locator, timeout=10):
    return get_element(self.driver, locator, timeout).is_displayed()


def send_keys_to_element(self, locator, input_value, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    element.clear()
    element.click()
    ActionChains(self.driver).move_to_element(element).click().key_down(
        Keys.CONTROL
    ).send_keys("a").key_up(Keys.CONTROL).send_keys(input_value).perform()


def send_key(self, locator, Key, timeout=10):
    get_element(self.driver, locator, timeout).send_keys(Key)


def get_text_of_an_element(self, locator, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    return element.text


def scroll_into_element(self, locator, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    self.driver.execute_script("arguments[0].scrollIntoView();", element)


def switch_to_default(self):
    self.driver.switch_to.default_content()


def switch_window(self):
    curr_win = self.driver.current_window_handle
    tabs = self.driver.window_handles
    for tab in tabs:
        if tab != curr_win:
            self.driver.switch_to.window(tab)


def switch_tab_by_title(self, title):
    for tab in self.driver.window_handles:
        if tab != self.driver.current_window_handle:
            self.driver.switch_to.window(tab)
            if self.driver.title == title or title in self.driver.title:
                break

def scroll_to_top_of_page(self):
    self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

def scroll_to_bottom_of_page(self):
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def open_tab(self):
    self.driver.execute_script("window.open('');")


def close_tab(self):
    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])


def switch_tab(self):
    for tab in self.driver.window_handles:
        self.driver.switch_to.window(tab)
        if self.driver.title != "Spekit Sidebar":
            self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])


def get_current_url(self):
    return self.driver.current_url


def open_spekit_url(self):
    url = settings.BASE_URL
    self.driver.get(url)


def refresh_tab(self):
    self.driver.refresh()
    time.sleep(2)


def open_url(self, url):
    self.driver.get(url)


def wait_for_page_load(self, desired_url):
    try:
        WebDriverWait(self.driver, 30).until(
            lambda driver: driver.current_url == desired_url
        )
    except ValueError as e:
        print("Another URL has been displayed i.e. " + str(e))


def switch_to_default(self):
    self.driver.switch_to.default_content()
    time.sleep(2)


def switch_to_iframe(self, locator, timeout=10):
    switch_to_default(self)
    spek_modal = self.driver.find_element_by_css_selector(locator)
    self.driver.switch_to.frame(spek_modal)

def hover_on_element(self, locator, timeout=10):
    if type(locator) == list:
        element = get_element(self.driver, locator, timeout)
    else:
        element = locator
    time.sleep(1.5)
    action = ActionChains(self.driver)
    action.move_to_element(element).perform()

