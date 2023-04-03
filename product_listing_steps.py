from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given(u'that we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(1)

@when(u'we search for "{category}"')
def step_impl(context, category):
    element_id = "twotabsearchtextbox"
    search_input = context.browser.find_element(By.ID, element_id)
    search_input.clear()
    search_input.send_keys(category)
    search_input.send_keys(Keys.RETURN)
    time.sleep(1)

@then(u'we find items from "{vendor}"')
def step_impl(context, vendor):
    page = context.browser.page_source
    assert vendor.upper() in page.upper()
