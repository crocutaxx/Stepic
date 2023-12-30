from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_button(browser):
    BUTTON = ('xpath', "(//button[@type='submit'])[2]")
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(BUTTON))
    assert element

