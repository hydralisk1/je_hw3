from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, "helpsearch")
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='help-content']//h1")
SHOPPING_CART = (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']")
EMPTY_CART_MESSAGE = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2")
GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@class='gLFyf gsfi']")
COVID_ALERT = (By.XPATH, "//div[@class='ORNlZd']//span")


@given('Open Amazon Customer Service page')
def open_amazon_customer_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@given('Open Google page')
def open_amazon(context):
    context.driver.get('https://www.google.com')


@when('Search for {keyword} on Amazon Customer Service page')
def search_keyword(context, keyword):
    context.driver.find_element(*SEARCH_FIELD).send_keys(keyword, Keys.ENTER)
    sleep(4)


@when('Search for {keyword} on Google')
def search_keyword(context, keyword):
    context.driver.find_element(*GOOGLE_SEARCH_FIELD).send_keys(keyword, Keys.ENTER)
    sleep(4)


@when('Click on the shopping cart icon')
def click_shopping_cart(context):
    context.driver.find_element(*SHOPPING_CART).click()
    sleep(4)


@then('How to Cancel Items or Order is shown')
def verify_how_to_cancel(context):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    expected_word = "Cancel Items or Orders"
    assert expected_word == results_msg, "Expected word '{}' in message, but got '{}'".format(expected_word, results_msg)


@then('Empty shopping cart is shown')
def verify_empty_cart(context):
    results_msg = context.driver.find_element(*EMPTY_CART_MESSAGE).text
    expected_word = "Your Amazon Cart is empty"
    assert expected_word == results_msg, "Expected word '{}' in message, but got '{}'".format(expected_word, results_msg)


@then('{keyword} alert is shown on the search result page')
def verify_covid_alert(context, keyword):
    try:
        results = context.driver.find_element(*COVID_ALERT)
    except NoSuchElementException:
        results = None

    assert results is not None, "There's no COVID 19 alert"
