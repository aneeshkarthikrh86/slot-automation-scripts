import time
from tests.base_page import BaseClass

# pages/home_page.py
class HomePage(BaseClass):
    def click_Slot(self):
        self.page.wait_for_selector("//a[text()=' Slot']",timeout=12000).click()
        time.sleep(1)
    def home_slot(self):
        self.page.wait_for_selector("//a[text()=' Home']",timeout=12000).hover()
        time.sleep(1)