from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the browser driver
browser = webdriver.Chrome()

@given('I am on the Nike website')
def step_impl(context):
    # Navigate to the Nike website
    browser.get("https://www.nike.com/")

@when('When I search for "{shoe}"')
def step_impl(context, shoe):
    # Find the search bar and enter "Jordan 1"
    element_id = "VisualSearchInput"
    search_input = browser.find_element(By.ID, element_id)
    search_input.clear()
    search_input.send_keys(shoe)
    search_input.send_keys(Keys.RETURN)

@then('I should see the first shoe in the search results')
def step_impl(context):
    # Wait for the search results to load
    WebDriverWait(browser, 10)
    
    # First class in search results
    first_shoe = "product-card__img-link-overlay" # element id should go here
    result = browser.find_element(By.CLASS_NAME, first_shoe)
    result.click()
    WebDriverWait(browser, 10)
