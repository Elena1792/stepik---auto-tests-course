    
import time
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket(browser):
    browser.get(link)
#     time.sleep(30)
    assert browser.find_element_by_css_selector('button.btn-add-to-basket')
