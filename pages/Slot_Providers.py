import time
from tests.base_page import BaseClass
from pages.game_page import Game_Click

class SlotProvider:
    def __init__(self):
        self.page = None
        self.context = None
        self.baseUrl = None
        self.username = None
        self.password = None

    def List_Provisers(self):
        # Ensure slot tab is open
        if not self.page.is_visible("//div[@class='provider-list']"):
            try:
                self.page.click("//button[text()='Slot']")   # adjust selector to your site
                self.page.wait_for_selector("//div[@class='provider-list']", timeout=10000)
            except Exception:
                print("⚠ Could not open slot providers menu")
                return

        providers = self.page.query_selector_all("//div[@class='provider-list']//button")
        for provider in providers:
            provider_name = provider.text_content().strip()
            print(f"Provider: {provider_name}")
            provider.click()

            # Create game page handler with shared context
            game_page = Game_Click()
            game_page.page = self.page
            game_page.context = self.context
            game_page.baseUrl = self.baseUrl
            game_page.username = self.username
            game_page.password = self.password

            # Run games for this provider
            game_page.GamesbtnClick(provider_name)
