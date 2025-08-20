import time
from tests.base_page import BaseClass
from pages.game_page import Game_Click

class SlotProvider:
    def __init__(self):
        self.page = None
        self.context = None  # make sure this is set from main

    def List_Providers(self, start_index=1):
        providers = self.page.query_selector_all(
            "//div[@class='mt-5 flex items-center slot_btn_container w-full overflow-auto light-scrollbar-h pb-[10px]']//button"
        )

        for idx, provider in enumerate(providers[start_index:], start=start_index):
            provider_name = provider.text_content().strip()
            print(f"Provider {idx+1}: {provider_name}")
            provider.click()

            # Create game page handler with shared context
            game_page = Game_Click()
            game_page.page = self.page
            game_page.context = self.context    # ✅ fix NoneType issue
            game_page.baseUrl = self.baseUrl
            game_page.username = self.username
            game_page.password = self.password

            # Run games for this provider
            game_page.GamesbtnClick(provider_name)
